# Modell zum Auswaehlen
# MP, 2021-11-08

from __future__ import division
from abaqus import *
from abaqusConstants import *
from caeModules import *

TOL = 1e-4
session.journalOptions.setValues(replayGeometry=COORDINATE,
        		         recoverGeometry=COORDINATE)

# Parameter vom Modell (N-mm-s)
b,h = 20.,12.
r = 2.
cent_list = ((6.,6.),(12.,8.))

# Modell erstellen
model_name = 'geometrie-sachen'

Mdb()
mdb.models.changeKey(fromName='Model-1', toName=model_name)
model = mdb.models[model_name]

# Platte mit loechern zeichnen
s = model.ConstrainedSketch(name='platte', sheetSize=200.0)

s.rectangle(point1=(0.0, 0.0), point2=(b,h))

# Schleife ueber alle Kreise
for cent in cent_list:
	s.CircleByCenterPerimeter(center=cent, point1=(cent[0]+r,cent[1]))
	
# 2d Part erstellen, part nennen
part = model.Part(dimensionality=TWO_D_PLANAR, name='Platte', type=DEFORMABLE_BODY)
part.BaseShell(sketch=s)

# linke Kante in Set: a) mit findAt, b) mit getByBoundingBox
part.Set(name='links', edges=part.edges.findAt(coordinates=[[0,h/2,0]]))
part.Set(name='links', edges=part.edges.getByBoundingBox(xMax=TOL))

mdb.saveAs('test.cae')