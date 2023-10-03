import os, glob
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor
from variableValues.measurements import FontMeasurements

# ---------
# functions
# ---------

def permille(value, unitsPerEm):
    return round(value * 1000 / unitsPerEm)

# --------
# settings
# --------

baseFolder       = os.path.dirname(os.getcwd())
sourcesFolder    = os.path.join(baseFolder, 'sources')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')
defaultUFO       = os.path.join(sourcesFolder, 'RobotoFlex_wght400.ufo')
designspacePath  = os.path.join(sourcesFolder, 'RobotoFlex.designspace')

familyName = 'Roboto Flex'

# parametric axes
names = 'XOPQ XOUC XOLC XOFI XTRA XTUC XTLC XTFI YOPQ YTAS YTDE YTUC YTLC YTFI'.split()

# -----
# setup
# -----

allUFOs = glob.glob(f'{sourcesFolder}/*.ufo')

# get default measurements
f = OpenFont(defaultUFO, showInterface=False)
unitsPerEm = f.info.unitsPerEm
M = FontMeasurements()
M.read(measurementsPath)
M.measure(f)
f.close()

doc = DesignSpaceDocument()

#----------
# add axes
#----------

# add slant axis
a = AxisDescriptor()
a.name    = 'slnt'
a.tag     = 'slnt'
a.minimum = -10
a.maximum = 0
a.default = 0
doc.addAxis(a)

# add grades axis
a = AxisDescriptor()
a.name    = 'GRAD'
a.tag     = 'GRAD'
a.minimum = -200
a.maximum = 150
a.default = 0
doc.addAxis(a)

# add spacing axis
a = AxisDescriptor()
a.name    = 'SPAC'
a.tag     = 'SPAC'
a.minimum = -100
a.maximum = 100
a.default = 0
doc.addAxis(a)

# add parametric axes
for name in names:
    # get min/max values
    values = []
    for ufo in allUFOs:
        if name in ufo:
            value = int(os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][4:])
            values.append(value)
    assert len(values)
    values.sort()
    # create axis
    a = AxisDescriptor()
    a.name    = name
    a.tag     = name
    a.minimum = values[0]
    a.maximum = values[1]
    a.default = permille(M.values[name], unitsPerEm)
    doc.addAxis(a)

#-------------
# add sources
#-------------

# add default source
L = { name : permille(M.values[name], unitsPerEm) for name in names }
L['slnt'] = 0
L['GRAD'] = 0
L['SPAC'] = 0
src = SourceDescriptor()
src.path       = defaultUFO
src.familyName = familyName
src.location   = L
doc.addSource(src)

# add slnt source
L2 = L.copy()
L2['slnt'] = -10
src = SourceDescriptor()
src.path       = os.path.join(sourcesFolder, 'RobotoFlex_slnt-10.ufo')
src.familyName = familyName
src.location   = L2
doc.addSource(src)

# add GRAD sources
for gradeValue in [-200, 150]:
    LG = L.copy()
    LG['GRAD'] = gradeValue
    src = SourceDescriptor()
    src.path       = os.path.join(sourcesFolder, f'RobotoFlex_GRAD{gradeValue}.ufo')
    src.familyName = familyName
    src.location   = LG
    doc.addSource(src)

# add SPAC sources
for spacingValue in [-100, 100]:
    LS = L.copy()
    LS['SPAC'] = spacingValue
    src = SourceDescriptor()
    src.path       = os.path.join(sourcesFolder, f'RobotoFlex_SPAC{spacingValue}.ufo')
    src.familyName = familyName
    src.location   = LS
    doc.addSource(src)

# add parametric sources
for name in names:
    for ufo in allUFOs:
        if name in ufo:
            src = SourceDescriptor()
            src.path       = ufo
            src.familyName = familyName            
            L4 = L.copy()
            value = int(os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][4:])
            L4[name] = value
            L4['slnt'] = 0
            L4['GRAD'] = 0
            src.location = L4
            doc.addSource(src)

# save .designspace file
doc.write(designspacePath)

