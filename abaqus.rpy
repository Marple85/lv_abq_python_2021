# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by p1340760 on Tue Nov 30 09:28:22 2021
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=146.451553344727, 
    height=188.066665649414)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
cliCommand("""# Modell mit Loechern, bis zum Rechnen""")
cliCommand("""# MP, 2021-11-29""")
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""TOL = 1e-4""")
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,
        		         recoverGeometry=COORDINATE)""")
cliCommand("""# Parameter vom Modell (N-mm-s)""")
cliCommand("""# ------------------------------------------------------""")
cliCommand("""b,h = 20.,12.""")
cliCommand("""r = 2.""")
cliCommand("""cent_list = ((6.,6.),(12.,8.))""")
cliCommand("""E = 210000.""")
cliCommand("""nu = 0.3""")
cliCommand("""sig_y = 300.""")
cliCommand("""E_pl = 15000.""")
cliCommand("""el_size = 0.5""")
cliCommand("""# Modell erstellen""")
cliCommand("""# ------------------------------------------------------------------""")
cliCommand("""model_name = 'geometrie-sachen'""")
cliCommand("""Mdb()""")
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: mdb
cliCommand("""mdb.models.changeKey(fromName='Model-1', toName=model_name)""")
\
    cliCommand("""model = mdb.models[model_name]""")
cliCommand("""# unser Material erzeugen""")
cliCommand("""mat = model.Material(name='steel')""")
cliCommand("""mat.Elastic(table=((E,nu), ))""")
#: mdb.models['geometrie-sachen'].materials['steel'].elastic
cliCommand("""mat.Plastic(table=((sig_y, 0.0), (sig_y+E_pl, 1.0)))""")
#: mdb.models['geometrie-sachen'].materials['steel'].plastic
cliCommand("""# Platte mit loechern zeichnen""")
cliCommand("""# -------------------------------------------""")
cliCommand("""s = model.ConstrainedSketch(name='platte', sheetSize=200.0)""")
\
    cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(b,h))""")
cliCommand("""# Schleife ueber alle Kreise""")
cliCommand("""for cent in cent_list:
	s.CircleByCenterPerimeter(center=cent, point1=(cent[0]+r,cent[1]))
""")
#: mdb.models['geometrie-sachen'].sketches['platte'].geometry.findAt((4.0, 6.0),)
#: mdb.models['geometrie-sachen'].sketches['platte'].geometry.findAt((10.0, 8.0),)
cliCommand("""# 2d Part erstellen, part nennen""")
cliCommand("""part = model.Part(dimensionality=TWO_D_PLANAR, name='Platte', type=DEFORMABLE_BODY)""")
cliCommand("""part.BaseShell(sketch=s)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].features['Shell planar-1']
cliCommand("""# Sets erstellen""")
cliCommand("""# -------------------------------------------""")
cliCommand("""part.Set(name='all',faces=part.faces)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['all']
cliCommand("""part.Set(name='links', edges=part.edges.getByBoundingBox(xMax=TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['links']
cliCommand("""part.Set(name='unten', edges=part.edges.getByBoundingBox(yMax=TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['unten']
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(coordinates=((b,h,0))))""")
#* TypeError: keyword error on vertices
p = mdb.models['geometrie-sachen'].parts['Platte']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.7103, 
    farPlane=52.5849, width=22.0653, height=27.965, viewOffsetX=-0.0524662, 
    viewOffsetY=-0.131239)
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(((20,12,0))))""")
#* TypeError: keyword error on vertices
cliCommand("""part.vertices.findAt(((20,12,0)))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].vertices.findAt((20.0, 12.0, 0.0),)
cliCommand("""type(part.vertices.findAt(((20,12,0))))""")
#: <type 'Vertex'>
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(((20,12,0)),))""")
#* TypeError: keyword error on vertices
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(((20,12,0),),))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['rechts-oben']
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(coordinates=((b,h,0),)))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['rechts-oben']
cliCommand("""# Modell mit Loechern, bis zum Rechnen""")
cliCommand("""# MP, 2021-11-29""")
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""TOL = 1e-4""")
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,
        		         recoverGeometry=COORDINATE)""")
cliCommand("""# Parameter vom Modell (N-mm-s)""")
cliCommand("""# ------------------------------------------------------""")
cliCommand("""b,h = 20.,12.""")
cliCommand("""r = 2.""")
cliCommand("""cent_list = ((6.,6.),(12.,8.))""")
cliCommand("""E = 210000.""")
cliCommand("""nu = 0.3""")
cliCommand("""sig_y = 300.""")
cliCommand("""E_pl = 15000.""")
cliCommand("""el_size = 0.5""")
cliCommand("""# Modell erstellen""")
cliCommand("""# ------------------------------------------------------------------""")
cliCommand("""model_name = 'geometrie-sachen'""")
cliCommand("""Mdb()""")
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: mdb
cliCommand("""mdb.models.changeKey(fromName='Model-1', toName=model_name)""")
\
    cliCommand("""model = mdb.models[model_name]""")
cliCommand("""# unser Material erzeugen""")
cliCommand("""mat = model.Material(name='steel')""")
cliCommand("""mat.Elastic(table=((E,nu), ))""")
#: mdb.models['geometrie-sachen'].materials['steel'].elastic
cliCommand("""mat.Plastic(table=((sig_y, 0.0), (sig_y+E_pl, 1.0)))""")
#: mdb.models['geometrie-sachen'].materials['steel'].plastic
cliCommand("""# Platte mit loechern zeichnen""")
cliCommand("""# -------------------------------------------""")
cliCommand("""s = model.ConstrainedSketch(name='platte', sheetSize=200.0)""")
\
    cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(b,h))""")
cliCommand("""# Schleife ueber alle Kreise""")
cliCommand("""for cent in cent_list:
	s.CircleByCenterPerimeter(center=cent, point1=(cent[0]+r,cent[1]))
""")
#: mdb.models['geometrie-sachen'].sketches['platte'].geometry.findAt((4.0, 6.0),)
#: mdb.models['geometrie-sachen'].sketches['platte'].geometry.findAt((10.0, 8.0),)
cliCommand("""# 2d Part erstellen, part nennen""")
cliCommand("""part = model.Part(dimensionality=TWO_D_PLANAR, name='Platte', type=DEFORMABLE_BODY)""")
cliCommand("""part.BaseShell(sketch=s)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].features['Shell planar-1']
cliCommand("""# Sets erstellen""")
cliCommand("""# -------------------------------------------""")
cliCommand("""part.Set(name='all',faces=part.faces)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['all']
cliCommand("""part.Set(name='links', edges=part.edges.getByBoundingBox(xMax=TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['links']
cliCommand("""part.Set(name='unten', edges=part.edges.getByBoundingBox(yMax=TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['unten']
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(coordinates=((b,h,0),)))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['rechts-oben']
cliCommand("""part.Surface(name='loecher',side1Edges=part.edges.getByBoundingBox(xMin=TOL,xMax=b-TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].surfaces['loecher']
cliCommand("""# Part vernetzen, assembly""")
cliCommand("""# -------------------------------------------""")
cliCommand("""part.seedPart(size=el_size)""")
cliCommand("""part.setMeshControls(regions=part.faces, elemShape=QUAD, algorithm=MEDIAL_AXIS)""")
cliCommand("""# lineare elemente mit red. int: MTM geht net!""")
cliCommand("""part.setElementType(regions=(part.faces,), elemTypes=(mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD),
                                                mesh.ElemType(elemCode=CPS6, elemLibrary=STANDARD)))""")
cliCommand("""part.generateMesh()""")
cliCommand("""ass = model.rootAssembly""")
cliCommand("""inst = ass.Instance(name='Platte-1', part=part, dependent=ON)""")
cliCommand("""# Material und Section""")
cliCommand("""# -------------------------------------------""")
cliCommand("""mat = model.Material(name='stahl')""")
cliCommand("""mat.Elastic(table=((E,nu),))""")
#: mdb.models['geometrie-sachen'].materials['stahl'].elastic
cliCommand("""# plastisches Verhalten noch nicht drinnen""")
cliCommand("""# Section erstellen und zuweisen""")
cliCommand("""model.HomogeneousSolidSection(material='stahl', name='stahl', thickness=None)""")
#: mdb.models['geometrie-sachen'].sections['stahl']
cliCommand("""part.SectionAssignment(region=part.sets['all'], sectionName='stahl',
                       thicknessAssignment=FROM_SECTION)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sectionAssignments[0]
cliCommand("""# Step und loads""")
cliCommand("""# -------------------------------------------""")
cliCommand("""model.StaticStep(name='load', previous='Initial', maxNumInc=1000, initialInc=1, 
                 minInc=1e-08, maxInc=1, nlgeom=OFF)""")
#: mdb.models['geometrie-sachen'].steps['load']
cliCommand("""model.HistoryOutputRequest(name='H-Output-2', createStepName='load', variables=('U1','U2'),
                           region=inst.sets['rechts-oben'])""")
#: mdb.models['geometrie-sachen'].historyOutputRequests['H-Output-2']
cliCommand("""model.DisplacementBC(name='xsym', createStepName='load', region=inst.sets['links'],
                     u1=0)""")
#: mdb.models['geometrie-sachen'].boundaryConditions['xsym']
cliCommand("""model.DisplacementBC(name='ysym', createStepName='load', region=inst.sets['unten'],
                     u2=0)""")
#: mdb.models['geometrie-sachen'].boundaryConditions['ysym']
cliCommand("""""\"
model.


mdb.saveAs(spec_type+'_calc')
job = mdb.Job(name=spec_type+'_calc', model='Model-1', type=ANALYSIS)
job.submit()
""\"""")
#: "\nmodel.\n\n\nmdb.saveAs(spec_type+'_calc')\njob = mdb.Job(name=spec_type+'_calc', model='Model-1', type=ANALYSIS)\njob.submit()\n"
cliCommand("""# Error zurueckgeben und Skriptausfuehrung abbrechen""")
cliCommand("""# Praktisch zum Testen des Skripts""")
p = mdb.models['geometrie-sachen'].parts['Platte']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['geometrie-sachen'].parts['Platte']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
cliCommand("""raise ValueError('alles in Ordnung?')	""")
#* ValueError: alles in Ordnung?
a = mdb.models['geometrie-sachen'].rootAssembly
a.regenerate()
a = mdb.models['geometrie-sachen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='load')
a = mdb.models['geometrie-sachen'].rootAssembly
region = a.instances['Platte-1'].surfaces['loecher']
mdb.models['geometrie-sachen'].Pressure(name='Load-1', createStepName='load', 
    region=region, distributionType=UNIFORM, field='', magnitude=10.0, 
    amplitude=UNSET)
cliCommand("""# Modell mit Loechern, bis zum Rechnen""")
cliCommand("""# MP, 2021-11-29""")
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""TOL = 1e-4""")
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,
        		         recoverGeometry=COORDINATE)""")
cliCommand("""# Parameter vom Modell (N-mm-s)""")
cliCommand("""# ------------------------------------------------------""")
cliCommand("""b,h = 20.,12.""")
cliCommand("""r = 2.""")
cliCommand("""cent_list = ((6.,6.),(12.,8.))""")
cliCommand("""E = 210000.""")
cliCommand("""nu = 0.3""")
cliCommand("""sig_y = 300.""")
cliCommand("""E_pl = 15000.""")
cliCommand("""p_innen = 10.""")
cliCommand("""el_size = 0.5""")
cliCommand("""# Modell erstellen""")
cliCommand("""# ------------------------------------------------------------------""")
cliCommand("""model_name = 'geometrie-sachen'""")
cliCommand("""Mdb()""")
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: mdb
cliCommand("""mdb.models.changeKey(fromName='Model-1', toName=model_name)""")
\
    cliCommand("""model = mdb.models[model_name]""")
cliCommand("""# unser Material erzeugen""")
cliCommand("""mat = model.Material(name='steel')""")
cliCommand("""mat.Elastic(table=((E,nu), ))""")
#: mdb.models['geometrie-sachen'].materials['steel'].elastic
cliCommand("""mat.Plastic(table=((sig_y, 0.0), (sig_y+E_pl, 1.0)))""")
#: mdb.models['geometrie-sachen'].materials['steel'].plastic
cliCommand("""# Platte mit loechern zeichnen""")
cliCommand("""# -------------------------------------------""")
cliCommand("""s = model.ConstrainedSketch(name='platte', sheetSize=200.0)""")
\
    cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(b,h))""")
cliCommand("""# Schleife ueber alle Kreise""")
cliCommand("""for cent in cent_list:
	s.CircleByCenterPerimeter(center=cent, point1=(cent[0]+r,cent[1]))
""")
#: mdb.models['geometrie-sachen'].sketches['platte'].geometry.findAt((4.0, 6.0),)
#: mdb.models['geometrie-sachen'].sketches['platte'].geometry.findAt((10.0, 8.0),)
cliCommand("""# 2d Part erstellen, part nennen""")
cliCommand("""part = model.Part(dimensionality=TWO_D_PLANAR, name='Platte', type=DEFORMABLE_BODY)""")
cliCommand("""part.BaseShell(sketch=s)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].features['Shell planar-1']
cliCommand("""# Sets erstellen""")
cliCommand("""# -------------------------------------------""")
cliCommand("""part.Set(name='all',faces=part.faces)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['all']
cliCommand("""part.Set(name='links', edges=part.edges.getByBoundingBox(xMax=TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['links']
cliCommand("""part.Set(name='unten', edges=part.edges.getByBoundingBox(yMax=TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['unten']
cliCommand("""part.Set(name='rechts-oben',vertices=part.vertices.findAt(coordinates=((b,h,0),)))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sets['rechts-oben']
cliCommand("""part.Surface(name='loecher',side1Edges=part.edges.getByBoundingBox(xMin=TOL,xMax=b-TOL))""")
#: mdb.models['geometrie-sachen'].parts['Platte'].surfaces['loecher']
cliCommand("""# Part vernetzen, assembly""")
cliCommand("""# -------------------------------------------""")
cliCommand("""part.seedPart(size=el_size)""")
cliCommand("""part.setMeshControls(regions=part.faces, elemShape=QUAD, algorithm=MEDIAL_AXIS)""")
cliCommand("""# lineare elemente mit red. int: MTM geht net!""")
cliCommand("""part.setElementType(regions=(part.faces,), elemTypes=(mesh.ElemType(elemCode=CPS8R, elemLibrary=STANDARD),
                                                mesh.ElemType(elemCode=CPS6, elemLibrary=STANDARD)))""")
cliCommand("""part.generateMesh()""")
cliCommand("""ass = model.rootAssembly""")
cliCommand("""inst = ass.Instance(name='Platte-1', part=part, dependent=ON)""")
cliCommand("""# Material und Section""")
cliCommand("""# -------------------------------------------""")
cliCommand("""mat = model.Material(name='stahl')""")
cliCommand("""mat.Elastic(table=((E,nu),))""")
#: mdb.models['geometrie-sachen'].materials['stahl'].elastic
cliCommand("""# plastisches Verhalten noch nicht drinnen""")
cliCommand("""# Section erstellen und zuweisen""")
cliCommand("""model.HomogeneousSolidSection(material='stahl', name='stahl', thickness=None)""")
#: mdb.models['geometrie-sachen'].sections['stahl']
cliCommand("""part.SectionAssignment(region=part.sets['all'], sectionName='stahl',
                       thicknessAssignment=FROM_SECTION)""")
#: mdb.models['geometrie-sachen'].parts['Platte'].sectionAssignments[0]
cliCommand("""# Step und loads""")
cliCommand("""# -------------------------------------------""")
cliCommand("""model.StaticStep(name='load', previous='Initial', maxNumInc=1000, initialInc=1, 
                 minInc=1e-08, maxInc=1, nlgeom=OFF)""")
#: mdb.models['geometrie-sachen'].steps['load']
cliCommand("""model.HistoryOutputRequest(name='H-Output-2', createStepName='load', variables=('U1','U2'),
                           region=inst.sets['rechts-oben'])""")
#: mdb.models['geometrie-sachen'].historyOutputRequests['H-Output-2']
cliCommand("""model.DisplacementBC(name='xsym', createStepName='Initial', region=inst.sets['links'],
                     u1=0)""")
#: mdb.models['geometrie-sachen'].boundaryConditions['xsym']
cliCommand("""model.DisplacementBC(name='ysym', createStepName='Initial', region=inst.sets['unten'],
                     u2=0)""")
#: mdb.models['geometrie-sachen'].boundaryConditions['ysym']
cliCommand("""model.Pressure(name='pressure', createStepName='load', region=inst.surfaces['loecher'],
               magnitude=p_innen)""")
#: mdb.models['geometrie-sachen'].loads['pressure']
cliCommand("""# Modell speicher, Job erstellen und rechnen""")
cliCommand("""mdb.saveAs(model_name)""")
#: The model database has been saved to "C:\Users\p1340760\Desktop\Python-Projekte\GitHub\lv_abq_python_2021\geometrie-sachen.cae".
cliCommand("""job = mdb.Job(name=model_name, model='Model-1', type=ANALYSIS)""")
#* Job must refer to a valid model.
a = mdb.models['geometrie-sachen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a.regenerate()
a = mdb.models['geometrie-sachen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
cliCommand("""# Modell speicher, Job erstellen und rechnen""")
cliCommand("""mdb.saveAs(model_name)""")
#: The model database has been saved to "C:\Users\p1340760\Desktop\Python-Projekte\GitHub\lv_abq_python_2021\geometrie-sachen.cae".
cliCommand("""job = mdb.Job(name=model_name, model=model_name, type=ANALYSIS)""")
cliCommand("""job.submit()""")
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.59284, 
    farPlane=5.40716, width=5.09761, height=6.46058, viewOffsetX=0.336315, 
    viewOffsetY=-0.497377)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
o1 = session.openOdb(
    name='C:/Users/p1340760/Desktop/Python-Projekte/GitHub/lv_abq_python_2021/geometrie-sachen.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/p1340760/Desktop/Python-Projekte/GitHub/lv_abq_python_2021/geometrie-sachen.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.9458, 
    farPlane=83.9936, width=21.0681, height=25.6656, viewOffsetX=0.505425, 
    viewOffsetY=0.214319)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
