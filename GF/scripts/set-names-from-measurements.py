from importlib import reload
import variableValues.measurements
reload(variableValues.measurements)

import os, glob, shutil
from variableValues.measurements import FontMeasurements

baseFolder       = os.path.dirname(os.getcwd())
sourcesFolder    = os.path.join(baseFolder, 'sources')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')

allUFOs = glob.glob(f'{sourcesFolder}/*.ufo')

ignoreTags = ['slnt', 'wght', 'GRAD']

for ufo in allUFOs:
    tag = os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][:4]
    if tag in ignoreTags:
        continue

    print(f'measuring {tag} in {os.path.split(ufo)[-1]}...')
    f = OpenFont(ufo, showInterface=False)
    m = FontMeasurements()
    m.read(measurementsPath)
    m.measure(f)
    newValue = m.values[tag]
    newValue1000 = round(newValue * 1000 / f.info.unitsPerEm)
    print(f'\tactual value: {newValue}')
    print(f'\tpermil value: {newValue1000}')

    # set style name
    newStyleName = f'{tag}{newValue1000}'
    if newStyleName != f.info.styleName:
        print(f'\tstyle name: {f.info.styleName} --> {newStyleName}' )
        f.info.styleName = newStyleName

    # rename file name
    newFileName = f'RobotoFlex_{newStyleName}.ufo'
    newFilePath = os.path.join(sourcesFolder, newFileName)
    f.save()
    f.close()
    if ufo != newFilePath:
        print(f'\tfile name: {os.path.split(ufo)[-1]} --> {newFileName}' )
        shutil.move(ufo, newFilePath)   

    print()
