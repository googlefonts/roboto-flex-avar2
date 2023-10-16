# menuTitle: build Roboto Flex avar2 designspaces

from importlib import reload
import variableValues.measurements
reload(variableValues.measurements)

import os, glob, shutil
import ufoProcessor
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, AxisMappingDescriptor
from variableValues.measurements import FontMeasurements

'''
Objects to build designspace files for Roboto Flex avar2.

0. default
   parametric axes
   9 instances for 5 axes extrema

1. default
   parametric axes
   blended axes (avar2)

2. default
   parametric axes
   9 sources for 5 axes extrema*

3. default
   9 sources for 5 axes extrema*

* axes extrema:               current values:

  | axis |  min |  max |      |  min |  max |
  |------|------|------|      |------|------|
  | Opsz |    6 |  144 |  ->  |    8 |  144 |
  | Wght |  200 |  700 |  ->  |  100 | 1000 |
  | Wdth |   75 |  125 |  ->  |   25 |  151 |
  | Slnt |      |  -10 |      |      |  -10 | ✔
  | Grad |  -50 |   50 |  ->  | -200 |  150 | ✔

'''

def permille(value, unitsPerEm):
    '''Convert an absolute value in font units to a relative value in permille units.'''
    return round(value * 1000 / unitsPerEm)


class RobotoFlexDesignSpaceBuilder:

    baseFolder           = os.path.dirname(os.getcwd())
    sourcesFolder        = os.path.join(baseFolder,    'sources')
    extremaFolder        = os.path.join(sourcesFolder, 'extrema')
    instancesFolder      = os.path.join(sourcesFolder, 'instances')
    measurementsPath     = os.path.join(sourcesFolder, 'measurements.json')
    defaultUFO           = os.path.join(sourcesFolder, 'RobotoFlex_wght400.ufo')
    designspacePath      = os.path.join(sourcesFolder, 'RobotoFlex0.designspace')
    familyName           = 'Roboto Flex'
    blendedAxes          = 'opsz wght wdth'.split()
    parametricAxes       = 'XOPQ XTRA YOPQ YTAS YTDE YTUC YTLC YTFI'.split() # XOUC XOLC XOFI XTUC XTLC XTFI 
    parametricAxesHidden = False

    def __init__(self):
        # collect parametric sources + extrema
        self.sourcesParametric = glob.glob(f'{self.sourcesFolder}/*.ufo')
        self.sourcesExtrema    = glob.glob(f'{self.extremaFolder}/*.ufo')
        # get measurements for default source
        f = OpenFont(self.defaultUFO, showInterface=False)
        self.unitsPerEm = f.info.unitsPerEm
        self.measurementsDefault = FontMeasurements()
        self.measurementsDefault.read(self.measurementsPath)
        self.measurementsDefault.measure(f)
        f.close()

    @property
    def defaultLocation(self):
        '''Return the location of the default source.'''
        L = { name: permille(self.measurementsDefault.values[name], self.unitsPerEm) for name in self.parametricAxes }
        L['slnt'] = 0
        L['GRAD'] = 0
        L['XTSP'] = 0
        return L

    def addParametricAxes(self):
        '''
        Add parametric axes to the designspace.
        The min/max values for each axis are taken from source file names. (File names are based on measurements.)

        slnt, GRAD, XTSP are added separately

        '''
        # add slant axis
        a = AxisDescriptor()
        a.name    = 'slnt'
        a.tag     = 'slnt'
        a.minimum = -10
        a.maximum = 0
        a.default = 0
        self.designspace.addAxis(a)

        # add grades axis
        a = AxisDescriptor()
        a.name    = 'GRAD'
        a.tag     = 'GRAD'
        a.minimum = -200
        a.maximum = 150
        a.default = 0
        self.designspace.addAxis(a)

        # add spacing axis
        a = AxisDescriptor()
        a.name    = 'XTSP'
        a.tag     = 'XTSP'
        a.minimum = -100
        a.maximum = 100
        a.default = 0
        self.designspace.addAxis(a)

        # add parametric axes
        for name in self.parametricAxes:
            # get min/max values from file names
            values = []
            for ufo in self.sourcesParametric:
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
            a.default = permille(self.measurementsDefault.values[name], self.unitsPerEm)
            a.hidden  = self.parametricAxesHidden
            self.designspace.addAxis(a)

    def addDefaultSource(self):
        # add default source
        src = SourceDescriptor()
        src.path       = self.defaultUFO
        src.familyName = self.familyName
        src.location   = self.defaultLocation.copy()
        self.designspace.addSource(src)

    def addParametricSources(self):
        '''
        Add sources to the designspace.
        Source locations are taken from file names. (File names are based on measurements.)

        '''
        # add slnt source
        L = self.defaultLocation.copy()
        L['slnt'] = -10
        src = SourceDescriptor()
        src.path       = os.path.join(self.sourcesFolder, 'RobotoFlex_slnt-10.ufo')
        src.familyName = self.familyName
        src.location   = L
        self.designspace.addSource(src)

        # add GRAD sources
        for gradeValue in [-200, 150]:
            L = self.defaultLocation.copy()
            L['GRAD'] = gradeValue
            src = SourceDescriptor()
            src.path       = os.path.join(self.sourcesFolder, f'RobotoFlex_GRAD{gradeValue}.ufo')
            src.familyName = self.familyName
            src.location   = L
            self.designspace.addSource(src)

        # add XTSP sources
        for spacingValue in [-100, 100]:
            L = self.defaultLocation.copy()
            L['XTSP'] = spacingValue
            src = SourceDescriptor()
            src.path       = os.path.join(self.sourcesFolder, f'RobotoFlex_XTSP{spacingValue}.ufo')
            src.familyName = self.familyName
            src.location   = L
            self.designspace.addSource(src)

        # add parametric sources
        for name in self.parametricAxes:
            for ufo in self.sourcesParametric:
                if name in ufo:
                    src = SourceDescriptor()
                    src.path       = ufo
                    src.familyName = self.familyName            
                    L = self.defaultLocation.copy()
                    value = int(os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][4:])
                    L[name] = value
                    src.location = L
                    self.designspace.addSource(src)

    def addInstances(self):
        '''
        Add instances to the designspace.
        Instance locations are taken from measurements of RobotoFlex sources (extrema).

        '''
        # prepare to measure fonts
        M = FontMeasurements()
        M.read(self.measurementsPath)

        for blendedAxisName in self.blendedAxes:
            for ufoPath in self.sourcesExtrema:
                if blendedAxisName in ufoPath:
                    # get measurements
                    f = OpenFont(ufoPath, showInterface=False)
                    M.measure(f)

                    # create instance location from default + measurements
                    L = self.defaultLocation.copy()
                    value = int(os.path.splitext(os.path.split(ufoPath)[-1])[0].split('_')[-1][4:])
                    valuePermill = permille(value, f.info.unitsPerEm)
                    L[blendedAxisName] = valuePermill
                    for measurementName in self.parametricAxes:
                        valuePermill = permille(int(M.values[measurementName]), f.info.unitsPerEm)
                        L[measurementName] = valuePermill                        

                    # add instance to designspace
                    I = InstanceDescriptor()
                    I.familyName     = self.familyName
                    I.styleName      = f.info.styleName.replace(' ', '')
                    I.name           = f.info.styleName.replace(' ', '')
                    I.designLocation = L
                    I.filename       = os.path.join('instances', os.path.split(ufoPath)[-1])
                    self.designspace.addInstance(I)

    def build(self):
        '''Build the designspace object.'''
        self.designspace = DesignSpaceDocument()
        self.addParametricAxes()
        self.addDefaultSource()
        self.addParametricSources()
        self.addInstances()

    def save(self):
        '''Save the designspace to a .designspace file.'''
        self.designspace.write(self.designspacePath)

    def buildInstances(self, clear=True):
        '''Build UFOs for all instances in the designspace.'''
        if clear:
            instances = glob.glob(f'{self.instancesFolder}/*.ufo')
            for instance in instances:
                shutil.rmtree(instance)
        ufoProcessor.build(self.designspacePath)


class RobotoFlexDesignSpaceBuilder1(RobotoFlexDesignSpaceBuilder):

    designspacePath = os.path.join(RobotoFlexDesignSpaceBuilder.sourcesFolder, 'RobotoFlex1.designspace')

    # blended axes data
    axesDefaults = {
        'opsz' : 14,
        'wght' : 400,
        'wdth' : 100,
    }
    axesNames = {
        'opsz' : 'Optical size',
        'wght' : 'Weight',
        'wdth' : 'Width',            
    }

    def addBlendedAxes(self):

        # load measurement definitions
        M = FontMeasurements()
        M.read(self.measurementsPath)

        for tag in self.blendedAxes:
            # get min/max values from file names
            values = []
            for ufo in self.sourcesExtrema:
                if tag in ufo:
                    value = int(os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][4:])
                    values.append(value)
            assert len(values)
            values.sort()

            # create axis
            a = AxisDescriptor()
            a.name    = self.axesNames[tag]
            a.tag     = tag
            a.minimum = values[0]
            a.maximum = values[1]
            a.default = self.axesDefaults[tag]
            self.designspace.addAxis(a)

    def addMappings_avar2(self):

        # load measurement definitions
        M = FontMeasurements()
        M.read(self.measurementsPath)


        for name in self.blendedAxes:
            m = AxisMappingDescriptor()

            for ufo in self.sourcesExtrema:
                if name in ufo:
                    # get input value from file name
                    inputLocation = {}
                    value = int(os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][4:])
                    inputLocation[self.axesNames[name]] = value

                    # get output value from measurements
                    f = OpenFont(ufo, showInterface=False)
                    M.measure(f)
                    outputLocation = {}
                    for measurementName in self.parametricAxes:
                        outputLocation[measurementName] = int(M.values[measurementName])

                    m.inputLocation  = inputLocation
                    m.outputLocation = outputLocation

            self.designspace.addAxisMapping(m)

    def build(self):
        self.designspace = DesignSpaceDocument()
        self.addBlendedAxes()
        self.addParametricAxes()
        self.addMappings_avar2()
        self.addDefaultSource()
        self.addParametricSources()
        

class RobotoFlexDesignSpaceBuilder2(RobotoFlexDesignSpaceBuilder1):

    designspacePath = os.path.join(RobotoFlexDesignSpaceBuilder.sourcesFolder, 'RobotoFlex2.designspace')

    @property
    def defaultLocation(self):
        L = { name: permille(self.measurementsDefault.values[name], self.unitsPerEm) for name in self.parametricAxes }
        L['Optical size'] = 14
        L['Weight'] = 400
        L['Width'] = 100
        L['slnt'] = 0
        L['GRAD'] = 0
        L['XTSP'] = 0
        return L

    def addBlendedAxes(self):

        # load measurement definitions
        M = FontMeasurements()
        M.read(self.measurementsPath)

        for tag in self.blendedAxes:
            # get min/max values from file names
            values = []
            for ufo in self.sourcesExtrema:
                if tag in ufo:
                    value = int(os.path.splitext(os.path.split(ufo)[-1])[0].split('_')[-1][4:])
                    values.append(value)
            assert len(values)
            values.sort()

            # create axis
            a = AxisDescriptor()
            a.name    = self.axesNames[tag]
            a.tag     = tag 
            a.minimum = values[0]
            a.maximum = values[1]
            a.default = self.axesDefaults[tag]
            self.designspace.addAxis(a)

    def addBlendedSources(self):
        M = FontMeasurements()
        M.read(self.measurementsPath)

        for blendedAxisTag in self.blendedAxes:
            for ufoPath in self.sourcesExtrema:
                if blendedAxisTag in ufoPath:
                    blendedAxisName = self.axesNames[blendedAxisTag]
                    # get measurements
                    f = OpenFont(ufoPath, showInterface=False)
                    M.measure(f)

                    # create instance location from default + measurements
                    L = self.defaultLocation.copy()
                    value = int(os.path.splitext(os.path.split(ufoPath)[-1])[0].split('_')[-1][4:])
                    L[blendedAxisName] = value # valuePermill

                    # add instance to designspace
                    src = SourceDescriptor()
                    src.path       = ufoPath
                    src.familyName = self.familyName
                    src.location   = L
                    self.designspace.addSource(src)

    def build(self):
        self.designspace = DesignSpaceDocument()
        self.addBlendedAxes()
        self.addParametricAxes()
        self.addDefaultSource()
        self.addBlendedSources()
        self.addParametricSources()


class RobotoFlexDesignSpaceBuilder3(RobotoFlexDesignSpaceBuilder2):

    designspacePath = os.path.join(RobotoFlexDesignSpaceBuilder.sourcesFolder, 'RobotoFlex3.designspace')

    def addParametricAxes(self):

        # add slant axis
        a = AxisDescriptor()
        a.name    = 'slnt'
        a.tag     = 'slnt'
        a.minimum = -10
        a.maximum = 0
        a.default = 0
        self.designspace.addAxis(a)

        # add grades axis
        a = AxisDescriptor()
        a.name    = 'GRAD'
        a.tag     = 'GRAD'
        a.minimum = -200
        a.maximum = 150
        a.default = 0
        self.designspace.addAxis(a)

    def addParametricSources(self):

        # add slnt source
        L = self.defaultLocation.copy()
        L['slnt'] = -10
        src = SourceDescriptor()
        src.path       = os.path.join(self.sourcesFolder, 'RobotoFlex_slnt-10.ufo')
        src.familyName = self.familyName
        src.location   = L
        self.designspace.addSource(src)

        # add GRAD sources
        for gradeValue in [-200, 150]:
            L = self.defaultLocation.copy()
            L['GRAD'] = gradeValue
            src = SourceDescriptor()
            src.path       = os.path.join(self.sourcesFolder, f'RobotoFlex_GRAD{gradeValue}.ufo')
            src.familyName = self.familyName
            src.location   = L
            self.designspace.addSource(src)

# -----
# build
# -----

if __name__ == '__main__':
    
    D = RobotoFlexDesignSpaceBuilder()
    D.build()
    D.save()
    # D.buildInstances(clear=True)
    
    D1 = RobotoFlexDesignSpaceBuilder1()
    D1.build()
    D1.save()

    D2 = RobotoFlexDesignSpaceBuilder2()
    D2.build()
    D2.save()

    D3 = RobotoFlexDesignSpaceBuilder3()
    D3.build()
    D3.save()
