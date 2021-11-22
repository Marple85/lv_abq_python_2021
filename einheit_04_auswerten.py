# Modell zum Auswaehlen, & Auswerten
# MP, 2021-11-22

from abaqus import *
from abaqusConstants import *
from caeModules import *

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

vp = session.viewports['Viewport: 1']

# open the odb with the odb_name
odb = session.openOdb(name=odb_name+'.odb')

# Bild ausgeben
# ------------------------------------------------------------------
vp.setValues(displayedObject=odb)
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

vp.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT,
                                 refinement=(COMPONENT, 'S11'),)

# Change size of viewport (e.g. 200x200 pixel)
vp.restore()
# position of the viewport
vp.setValues(origin=(50,-100))
vp.setValues(width=200, height=200)

# change the legend and what is displayed
vp.viewportAnnotationOptions.setValues(legendFont=
       '-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')
vp.viewportAnnotationOptions.setValues(triad=OFF, state=OFF,
    legendBackgroundStyle=MATCH,annotations=OFF,compass=OFF,
    title=OFF)

# manuell hindrehen/zoomen und View speichern
session.View(name='User-1', nearPlane=55.904, farPlane=88.692, width=18.825, 
    height=18.358, projection=PERSPECTIVE, cameraPosition=(10.8, 6.8331, 
    72.298), cameraUpVector=(0, 1, 0), cameraTarget=(10.8, 6.8331, 0), 
    viewOffsetX=-0.31964, viewOffsetY=3.5499, autoFit=OFF)

vp.view.setValues(session.views['User-1'])

# output image
session.printOptions.setValues(reduceColors=False, vpDecorations=OFF)
# set a bigger image size: 3000 x 2000 pixels
session.pngOptions.setValues(imageSize=(2000, 2000))
session.printToFile(fileName=odb_name+'_sx', format=PNG,
		    canvasObjects=(vp,))

# auf FieldOutput zugreifen
## ------------------------------------------------------------------

# alle Elemente, deren Integrationspunkte und die Mises Spannung dort
[[i.elementLabel,i.integrationPoint,i.mises] for i in odb.steps['innendruck'].frames[1].fieldOutputs['S'].values]

# maximale Spannung an den Integrationspunkten erhalten
s11_max = max([i.data[0] for i in odb.steps['innendruck'].frames[1].fieldOutputs['S'].values])

# Variante mit BulkData Blocks: Ergebnisse werden nach Elementtyp eingeteilt
# (naeheres unter martinpletz.com/fe-scripting-4)
s_field = odb.steps['innendruck'].frames[1].fieldOutputs['S']
bulk_data = s_field.bulkDataBlocks
