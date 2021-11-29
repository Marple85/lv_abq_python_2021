# Modell zum Auswaehlen, & Auswerten
# MP, 2021-11-29

from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

TOL = 1e-4

# Parameter vom Modell (N-mm-s)
# ------------------------------------------------------
b,h = 20.,12.
r = 2.
cent_list = ((6.,6.),(12.,8.))
E = 210000.
nu = 0.3
sig_y = 300.
E_pl = 15000.

odb_name = 'platte-manuell'

# open the odb with the odb_name
odb = session.openOdb(name=odb_name+'.odb')
vp = session.viewports['Viewport: 1']

# Pfad erstellen & auswerten
# -----------------------------------------------------------------
path = session.Path(name='halbe-hoehe', type=POINT_LIST,
                    expression=((0,h/2.,0), (b,h/2.,0)))

vp.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT,
                                 refinement=(INVARIANT, 'Max. Principal'),)

xy1 = xyPlot.XYDataFromPath(path=path, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=100, 
    projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE_X, 
    removeDuplicateXYPairs=True, includeAllElements=False)

x_max_princ = np.array(xy1.data)
np.savetxt('platte-pfad-s1.dat',x_max_princ,delimiter=',',
           header='x-position (mm), max. princ. s. 75avg (MPa)')

# History Output auswerten
# -----------------------------------------------------------------
step = odb.steps['innendruck']
hr = step.historyRegions.values()[1]

u1 = np.array(hr.historyOutputs['U1'].data)
u2 = np.array(hr.historyOutputs['U2'].data)[:,1]

# stack np.arrays in 2nd direction
out_arr = np.c_[u1,u2]

np.savetxt('platte-u-rechts_oben.dat',out_arr,delimiter=',',
           header='t (s), u1 (mm), u2 (mm)')

kerb_typ = 'ecke' # 'rund', 'spline'

# Baustein fuer das selbststaendige Beispiel
#  --> Optionen der Kerbgeometrie

if kerb_typ == 'ecke':
    None
elif kerb_typ == 'rund':
    pass
    # rundung zeichnen
else:
    # spline zeichnen
    pass
