
from fontTools.designspaceLib import (DesignSpaceDocument, AxisDescriptor,
                                      SourceDescriptor, InstanceDescriptor)

PATH = '../source/Parametric-avar2/'

ds = DesignSpaceDocument.fromfile('../source/Parametric-avar2/Roboto-Delta.designspace')

sources = [

# 'Roboto-Delta-STLI2.ufo',# 'Roboto-Delta-STLI412.ufo',# 'Roboto-Delta-STLO2.ufo',# 'Roboto-Delta-STLO426.ufo',# 'Roboto-Delta-STUI2.ufo',# 'Roboto-Delta-STUI736.ufo',# 'Roboto-Delta-STUO2.ufo',# 'Roboto-Delta-STUO722.ufo',# 'Roboto-Delta-VANG-3.ufo',# 'Roboto-Delta-VANG13.ufo',# 'Roboto-Delta-wght400.ufo',# 'Roboto-Delta-XOAC50.ufo',# 'Roboto-Delta-XOFI2.ufo',# 'Roboto-Delta-XOFI300.ufo',# 'Roboto-Delta-XOLC2.ufo',# 'Roboto-Delta-XOLC294.ufo',# 'Roboto-Delta-XOPQ2.ufo',# 'Roboto-Delta-XOPQ310.ufo',# 'Roboto-Delta-XOUC2.ufo',# 'Roboto-Delta-XOUC310.ufo',# 'Roboto-Delta-XTFI244.ufo',# 'Roboto-Delta-XTFI741.ufo',# 'Roboto-Delta-XTLC244.ufo',# 'Roboto-Delta-XTLC741.ufo',# 'Roboto-Delta-XTRA244-opsz144-wdth25-wght100.ufo',# 'Roboto-Delta-XTRA244.ufo',# 'Roboto-Delta-XTRA741-SO.ufo',# 'Roboto-Delta-XTRA741.ufo',# 'Roboto-Delta-XTSP-100.ufo',# 'Roboto-Delta-XTSP100.ufo',# 'Roboto-Delta-XTTW0.ufo',# 'Roboto-Delta-XTTW30.ufo',# 'Roboto-Delta-XTUC244.ufo',# 'Roboto-Delta-XTUC741.ufo',# 'Roboto-Delta-YOPQ2.ufo',# 'Roboto-Delta-YOPQ280.ufo',# 'Roboto-Delta-YTAS665.ufo',# 'Roboto-Delta-YTAS875.ufo',# 'Roboto-Delta-YTDE-100.ufo',# 'Roboto-Delta-YTDE-310.ufo',# 'Roboto-Delta-YTFI270.ufo',# 'Roboto-Delta-YTFI793.ufo',# 'Roboto-Delta-YTLC426.ufo',# 'Roboto-Delta-YTLC584.ufo',# 'Roboto-Delta-YTOS0.ufo',# 'Roboto-Delta-YTOS50.ufo',# 'Roboto-Delta-YTTL0.ufo',# 'Roboto-Delta-YTTL50.ufo',# 'Roboto-Delta-YTUC528.ufo',# 'Roboto-Delta-YTUC778.ufo', 

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

