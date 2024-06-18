
from fontTools.designspaceLib import (DesignSpaceDocument, AxisDescriptor,
                                      SourceDescriptor, InstanceDescriptor)

PATH = '../source/Parametric-avar2/'

ds = DesignSpaceDocument.fromfile('../source/Parametric-avar2/RobotoAvar2-avar2-clean.designspace')


for source in ds.sources:
    
    fontName = PATH + source.filename
    font = OpenFont(fontName, showInterface=False)
    
    # Familyname
    #font.info.familyName = 'RobotoAvar2'
    
    # Features
    #font.features.text = "include(features/RobotoAvar2.fea)"
    
    
    #Metrics
    font.info.ascender = 1456
    font.info.descender = -416
    
    font.info.openTypeHheaAscender = 1456
    font.info.openTypeHheaDescender = -416
    
    font.info.openTypeOS2TypoAscender = 1456
    font.info.openTypeOS2TypoDescender = -416
    
    font.info.openTypeOS2WinAscent = 1456
    font.info.openTypeOS2WinDescent = 416
    
    
    font.save()
    font.close()
    
    print ('Updated source at: ' + fontName)

