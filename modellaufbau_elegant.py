# Modell mit Loechern, bis zum Rechnen
# MP, 2021-11-29

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os,shutil
import numpy as np

DIR0 = os.path.abspath('')
TOL = 1e-4
session.journalOptions.setValues(replayGeometry=COORDINATE,
        		         recoverGeometry=COORDINATE)

# Funktionen zur Modellerstellung
# ------------------------------------------------------------------

def reset_model(model_name):
    Mdb()
    mdb.models.changeKey(fromName='Model-1', toName=model_name)
    model = mdb.models[model_name]
    return model

def make_geom_sets(model,b,h,r,cent_list,el_size):

    # Platte mit loechern zeichnen
    # -------------------------------------------
    s = model.ConstrainedSketch(name='platte', sheetSize=200.0)
    s.rectangle(point1=(0.0, 0.0), point2=(b,h))

    # Schleife ueber alle Kreise
    for cent in cent_list:
        s.CircleByCenterPerimeter(center=cent, point1=(cent[0]+r,cent[1]))

    # 2d Part erstellen, part nennen
    part = model.Part(dimensionality=TWO_D_PLANAR, name='Platte', type=DEFORMABLE_BODY)
    part.BaseShell(sketch=s)

    # Sets erstellen
    # -------------------------------------------

    part.Set(name='all',faces=part.faces)

    part.Set(name='links', edges=part.edges.getByBoundingBox(xMax=TOL))
    part.Set(name='unten', edges=part.edges.getByBoundingBox(yMax=TOL))
    part.Set(name='rechts-oben',vertices=part.vertices.findAt(coordinates=((b,h,0),)))

    part.Surface(name='loecher',side1Edges=part.edges.getByBoundingBox(xMin=TOL,xMax=b-TOL))

    # Part vernetzen, assembly
    # -------------------------------------------

    part.seedPart(size=el_size)
    part.setMeshControls(regions=part.faces, elemShape=QUAD, algorithm=MEDIAL_AXIS)
    # lineare elemente mit red. int: MTM geht net!
    part.setElementType(regions=(part.faces,), elemTypes=(mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD),
                                                    mesh.ElemType(elemCode=CPS6, elemLibrary=STANDARD)))
    part.generateMesh()
    return part

def make_assembly(model,part,E,nu,sig_y,E_pl):
    ass = model.rootAssembly
    inst = ass.Instance(name='Platte-1', part=part, dependent=ON)

    # unser Material erzeugen
    mat = model.Material(name='stahl')
    mat.Elastic(table=((E,nu), ))
    #mat.Plastic(table=((sig_y, 0.0), (sig_y+E_pl, 1.0)))

    # Section erstellen und zuweisen
    model.HomogeneousSolidSection(material='stahl', name='stahl', thickness=None)
    part.SectionAssignment(region=part.sets['all'], sectionName='stahl',
                        thicknessAssignment=FROM_SECTION)
    return inst

def make_loads(model,inst,p_innen):
    # Step und loads
    # -------------------------------------------

    model.StaticStep(name='load', previous='Initial', maxNumInc=1000, initialInc=1, 
                    minInc=1e-08, maxInc=1, nlgeom=OFF)

    model.HistoryOutputRequest(name='H-Output-2', createStepName='load', variables=('U1','U2'),
                            region=inst.sets['rechts-oben'])

    model.DisplacementBC(name='xsym', createStepName='Initial', region=inst.sets['links'],
                        u1=0)
    model.DisplacementBC(name='ysym', createStepName='Initial', region=inst.sets['unten'],
                        u2=0)

    model.Pressure(name='pressure', createStepName='load', region=inst.surfaces['loecher'],
                magnitude=p_innen)
    return

def run_model(job_name,if_run=0):
    # Modell speicher, Job erstellen und rechnen
    mdb.saveAs(job_name)
    job = mdb.Job(name=job_name, model=job_name, type=ANALYSIS)
    if if_run:
        job.submit()
        job.waitForCompletion()
    return

def eval_model(odb_name):
    odb = session.openOdb(name=odb_name+'.odb')
    vp = session.viewports['Viewport: 1']

    step = odb.steps['innendruck']
    hr = step.historyRegions.values()[1]

    u1 = np.array(hr.historyOutputs['U1'].data)
    u2 = np.array(hr.historyOutputs['U2'].data)[:,1]

    # stack np.arrays in 2nd direction
    out_arr = np.c_[u1,u2]

    np.savetxt(odb_name+'-res-u.dat',out_arr,delimiter=',',
            header='t (s), u1 (mm), u2 (mm)')
    return

# insert more parameters after run_folder
def create_model(run_dir,model_name,b,h,r,cent_list,el_size,E,nu,sig_y,E_pl,p_innen,if_run=1):
    #
    dir_name = os.path.join('results',run_dir)
    # delete folder if it exists
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    # create folder
    os.mkdir(dir_name)
    # go into folder
    os.chdir(dir_name)
    # model setup, run and evaluation
    model = reset_model(model_name)
    part = make_geom_sets(model,b,h,r,cent_list,el_size)
    inst = make_assembly(model,part,E,nu,sig_y,E_pl)

    make_loads(model,inst,p_innen)
    run_model(model_name,if_run)
    #
    eval_model(model_name)
    # go back to initial folder
    os.chdir(DIR0)
    return

# Parameter vom Modell (N-mm-s)
# ------------------------------------------------------
b,h = 20.,12.
r = 2.
cent_list = ((6.,6.),(12.,8.))
E = 210000.
nu = 0.3
sig_y = 300.
E_pl = 15000.

p_innen = 10.
el_size = 0.5

# Funktionen aufrufen
# ------------------------------------------------------------------
model_name = 'lochplatte-druck'
run_dir = 'beta-1'

create_model(run_dir,model_name,b,h,r,cent_list,el_size,E,nu,sig_y,E_pl,p_innen,if_run=0)

# model = reset_model(model_name)
# part = make_geom_sets(model,b,h,r,cent_list,el_size)
# inst = make_assembly(model,part,E,nu,sig_y,E_pl)

# make_loads(model,inst,p_innen)
# run_model(model_name,if_run=0)


