

#from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

SRC_PATH = '../Parametric-avar2/'

DST_PATH = '../Parametric-avar2/'

SOURCES = [

    'RobotoA2-wght400.ufo',
    'RobotoA2-XOFI27.ufo',
    'RobotoA2-XOFI180.ufo',
    'RobotoA2-XOLC27.ufo',
    'RobotoA2-XOLC170.ufo',
    'RobotoA2-XOPQ2.ufo',    'RobotoA2-XOPQ310.ufo',
    'RobotoA2-XOUC27.ufo',
    'RobotoA2-XOUC175.ufo',
    'RobotoA2-XTFI252.ufo',
    'RobotoA2-XTFI488.ufo',
    'RobotoA2-XTLC222.ufo',
    'RobotoA2-XTLC486.ufo',
    'RobotoA2-XTRA323.ufo',
    'RobotoA2-XTRA603.ufo',
    'RobotoA2-XTUC323.ufo',
    'RobotoA2-XTUC603.ufo',
    'RobotoA2-YOPQ25.ufo',
    'RobotoA2-YOPQ135.ufo',
    'RobotoA2-YTAS665.ufo',
    'RobotoA2-YTAS875.ufo',
    'RobotoA2-YTDE-100.ufo',
    'RobotoA2-YTDE-310.ufo',
    'RobotoA2-YTFI560.ufo',
    'RobotoA2-YTFI788.ufo',
    'RobotoA2-YTLC426.ufo',
    'RobotoA2-YTLC584.ufo',
    'RobotoA2-YTUC528.ufo',
    'RobotoA2-YTUC778.ufo',
            
]

glyphsToFix = ['five']

def decomposeGlyphs(fonts):

    for font in fonts:
        
        dst_fontName = DST_PATH + font
        dst_font = OpenFont(dst_fontName, showInterface=False)
        
        for glyph in glyphsToFix:
            
            #dst_font[glyph].unicode = hex(0x04D2)
            #dst_font[glyph].clear()
            #dst_font[glyph].appendComponent("Schwa")
            #dst_font[glyph].width = dst_font['Schwa'].width
            
            dst_font[glyph].width = 1156
            
        #dst_font.features.text = 'include(features/RobotoA2.fea)'
        dst_font.save()
        print('Fixed glyphs at ' + dst_fontName)



decomposeGlyphs(SOURCES)

