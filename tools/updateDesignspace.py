
from fontTools.designspaceLib import (DesignSpaceDocument, AxisDescriptor,
                                      SourceDescriptor, InstanceDescriptor)

PATH = '../source/Parametric-avar2/'

ds = DesignSpaceDocument.fromfile('../source/Parametric-avar2/RobotoAvar2-avar2.designspace')

sources = [

# 'RobotoAvar2-STLI2.ufo',# 'RobotoAvar2-STLI412.ufo',# 'RobotoAvar2-STLO2.ufo',# 'RobotoAvar2-STLO426.ufo',# 'RobotoAvar2-STUI2.ufo',# 'RobotoAvar2-STUI736.ufo',# 'RobotoAvar2-STUO2.ufo',# 'RobotoAvar2-STUO722.ufo',# 'RobotoAvar2-VANG-3.ufo',# 'RobotoAvar2-VANG13.ufo',# 'RobotoAvar2-wght400.ufo',# 'RobotoAvar2-XOAC50.ufo',# 'RobotoAvar2-XOFI2.ufo',# 'RobotoAvar2-XOFI300.ufo',# 'RobotoAvar2-XOLC2.ufo',# 'RobotoAvar2-XOLC294.ufo',# 'RobotoAvar2-XOPQ2.ufo',# 'RobotoAvar2-XOPQ310.ufo',# 'RobotoAvar2-XOUC2.ufo',# 'RobotoAvar2-XOUC310.ufo',# 'RobotoAvar2-XTFI244.ufo',# 'RobotoAvar2-XTFI741.ufo',# 'RobotoAvar2-XTLC244.ufo',# 'RobotoAvar2-XTLC741.ufo',# 'RobotoAvar2-XTRA244-opsz144-wdth25-wght100.ufo',# 'RobotoAvar2-XTRA244.ufo',# 'RobotoAvar2-XTRA741-SO.ufo',# 'RobotoAvar2-XTRA741.ufo',# 'RobotoAvar2-XTSP-100.ufo',# 'RobotoAvar2-XTSP100.ufo',# 'RobotoAvar2-XTTW0.ufo',# 'RobotoAvar2-XTTW30.ufo',# 'RobotoAvar2-XTUC244.ufo',# 'RobotoAvar2-XTUC741.ufo',# 'RobotoAvar2-YOPQ2.ufo',# 'RobotoAvar2-YOPQ280.ufo',# 'RobotoAvar2-YTAS665.ufo',# 'RobotoAvar2-YTAS875.ufo',# 'RobotoAvar2-YTDE-100.ufo',# 'RobotoAvar2-YTDE-310.ufo',# 'RobotoAvar2-YTFI270.ufo',# 'RobotoAvar2-YTFI793.ufo',# 'RobotoAvar2-YTLC426.ufo',# 'RobotoAvar2-YTLC584.ufo',# 'RobotoAvar2-YTOS0.ufo',# 'RobotoAvar2-YTOS50.ufo',# 'RobotoAvar2-YTTL0.ufo',# 'RobotoAvar2-YTTL50.ufo',# 'RobotoAvar2-YTUC528.ufo',# 'RobotoAvar2-YTUC778.ufo', 

]

# ds.sources

for source in ds.sources:
    
    fontName = PATH + source.filename
    font = OpenFont(fontName, showInterface=False)
    
    # Familyname
    #font.info.familyName = 'RobotoAvar2'
    
    # Features
    #font.features.text = "include(features/RobotoAvar2.fea)"
    
    
    #Metrics
    font.info.ascender = 1900
    font.info.descender = -500
    
    font.info.openTypeHheaAscender = 1900
    font.info.openTypeHheaDescender = -500
    
    font.info.openTypeOS2TypoAscender = 1900
    font.info.openTypeOS2TypoDescender = -500
    
    font.info.openTypeOS2WinAscent = 2461
    font.info.openTypeOS2WinDescent = 600
    
    # font['hyphentwo'].components[0].baseGlyph = 'hyphen'
    # font['softhyphen'].components[0].baseGlyph = 'hyphen'
    
    font.save()
    font.close()
    
    print ('Updated source at: ' + fontName)

