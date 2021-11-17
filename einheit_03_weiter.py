# Modell zum Auswaehlen, weiter
# MP, 2021-11-08

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

# Modell erstellen
# ------------------------------------------------------------------
model_name = 'geometrie-sachen'

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

# linke Kante in Set: a) mit findAt, b) mit getByBoundingBox
part.Set(name='links', edges=part.edges.findAt(coordinates=[[0,h/2,0]]))
part.Set(name='links', edges=part.edges.getByBoundingBox(xMax=TOL))

# nur edges mit Laenge h in Liste (Koordinaten)

# Vriante mit Schleife
size_12_list = []

for edge in part.edges:
    print(edge)
    edge_size = edge.getSize()
    #print(edge.pointOn)
    edge_coord_list = list(edge.pointOn[0])
    if edge_size == h:
        size_12_list = size_12_list + [edge_coord_list]

# Set aus diesen Edges
part.Set(name='aussen-edges-schleife', 
         edges=part.edges.findAt(coordinates=size_12_list))

# mit list comprehension in nur einer Zeile das Gleiche wie Schleife
size_12_list = [list(i.pointOn[0]) for i in part.edges if i.getSize()==h]

# Set aus diesen Edges
part.Set(name='aussen-edges-direkt', 
         edges=part.edges.findAt(coordinates=size_12_list))

# Referenzpunkte sind etwas umstaendlich
rp = model.parts['Platte'].ReferencePoint(point=(0,0,0))
part.Set(name='RP', referencePoints=(part.referencePoints[rp.id], ))

# datum planes auch ;-)
dp1 = part.DatumPlaneByPrincipalPlane(offset=10.0, principalPlane=YZPLANE)
part.PartitionFaceByDatumPlane(datumPlane=part.datums[dp1.id],
				               faces=part.faces)

# Error zurueckgeben und Skriptausfuehrung abbrechen
# Praktisch zum Testen des Skripts
raise ValueError('alles in Ordnung?')	

mdb.saveAs('test.cae')