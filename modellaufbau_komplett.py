# Modell mit Loechern, bis zum Rechnen
# MP, 2021-11-29

from abaqus import *
from abaqusConstants import *
from caeModules import *

TOL = 1e-4
session.journalOptions.setValues(replayGeometry=COORDINATE,
        		         recoverGeometry=COORDINATE)

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

# Modell erstellen
# ------------------------------------------------------------------
model_name = 'lochplatte-druck'

Mdb()
mdb.models.changeKey(fromName='Model-1', toName=model_name)
model = mdb.models[model_name]

# unser Material erzeugen
mat = model.Material(name='steel')
mat.Elastic(table=((E,nu), ))
mat.Plastic(table=((sig_y, 0.0), (sig_y+E_pl, 1.0)))

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

ass = model.rootAssembly
inst = ass.Instance(name='Platte-1', part=part, dependent=ON)

# Material und Section
# -------------------------------------------
mat = model.Material(name='stahl')
mat.Elastic(table=((E,nu),))
# plastisches Verhalten noch nicht drinnen

# Section erstellen und zuweisen
model.HomogeneousSolidSection(material='stahl', name='stahl', thickness=None)
part.SectionAssignment(region=part.sets['all'], sectionName='stahl',
                       thicknessAssignment=FROM_SECTION)

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

# Modell speicher, Job erstellen und rechnen
mdb.saveAs(model_name)
job = mdb.Job(name=model_name, model=model_name, type=ANALYSIS)
job.submit()

