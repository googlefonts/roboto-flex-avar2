

from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

SRC_PATH = '../Parametric-avar2/'

DST_PATH = '../Parametric-avar2/'

SOURCES = [

    #'RobotoA2-wght400.ufo',
    'RobotoAvar2-XOAC50.ufo', 
    'RobotoAvar2-XOFI2.ufo', 
    'RobotoAvar2-XOFI300.ufo', 
    'RobotoAvar2-XOLC2.ufo', 
    'RobotoAvar2-XOLC294.ufo', 
    'RobotoAvar2-XOPQ2.ufo', 
    'RobotoAvar2-XOPQ310.ufo', 
    'RobotoAvar2-XOUC2.ufo', 
    'RobotoAvar2-XOUC310.ufo', 
    'RobotoAvar2-XTFI252.ufo', 
    'RobotoAvar2-XTFI488.ufo', 
    'RobotoAvar2-XTLC222.ufo', 
    'RobotoAvar2-XTLC486.ufo', 
    'RobotoAvar2-XTRA244.ufo', 
    'RobotoAvar2-XTRA605.ufo', 
    'RobotoAvar2-XTSP-100.ufo', 
    'RobotoAvar2-XTSP100.ufo', 
    'RobotoAvar2-XTUC323.ufo', 
    'RobotoAvar2-XTUC603.ufo', 
    'RobotoAvar2-YOPQ2.ufo', 
    'RobotoAvar2-YOPQ280.ufo', 
    'RobotoAvar2-YTAS665.ufo', 
    'RobotoAvar2-YTAS875.ufo', 
    'RobotoAvar2-YTDE-100.ufo', 
    'RobotoAvar2-YTDE-310.ufo', 
    'RobotoAvar2-YTFI560.ufo', 
    'RobotoAvar2-YTFI788.ufo', 
    'RobotoAvar2-YTLC426.ufo', 
    'RobotoAvar2-YTLC584.ufo', 
    'RobotoAvar2-YTOS-50.ufo', 
    'RobotoAvar2-YTOS0.ufo', 
    'RobotoAvar2-YTOS50.ufo', 
    'RobotoAvar2-YTUC528.ufo', 
    'RobotoAvar2-YTUC778.ufo',
    
]

#glyphsToFix = ['five']

txtGlyphConstruction = '''\
Ghe = Gamma | 0x0413
Gje = Gamma + acutecomb.case@top | 0x0403
Ghestroke = Gamma + horizontalbar@center | 0x0492
ecircumflexdotbelow=e+circumflexcomb@top+dotbelowcomb@e:bottom | 0x1ec7
'''

constructions = ParseGlyphConstructionListFromString(txtGlyphConstruction)

def updateGlyphs(fonts):

    for font in fonts:
        
        dst_fontName = DST_PATH + font
        dst_font = OpenFont(dst_fontName, showInterface=False)
        
        for construction in constructions:
            
            constructionGlyph = GlyphConstructionBuilder(construction, dst_font)
            glyph = dst_font[constructionGlyph.name]
            glyph.clear(contours=True, components=True, anchors=False, guidelines=False, image=True)
            constructionGlyph.draw(glyph.getPen())
            glyph.name = constructionGlyph.name
            glyph.unicode = constructionGlyph.unicode
            glyph.width = constructionGlyph.width
        
            
        #dst_font.features.text = 'include(features/RobotoA2.fea)'
        dst_font.save()
        print('Updated glyphs at ' + dst_fontName)



updateGlyphs(SOURCES)

