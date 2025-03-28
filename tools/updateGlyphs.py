

from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

SRC_PATH = '../Parametric-avar2/'

DST_PATH = '../Parametric-avar2/'

SOURCES = [

    #'RobotoA2-wght400.ufo',
    'Roboto-Delta-XOAC50.ufo', 
    'Roboto-Delta-XOFI2.ufo', 
    'Roboto-Delta-XOFI300.ufo', 
    'Roboto-Delta-XOLC2.ufo', 
    'Roboto-Delta-XOLC294.ufo', 
    'Roboto-Delta-XOPQ2.ufo', 
    'Roboto-Delta-XOPQ310.ufo', 
    'Roboto-Delta-XOUC2.ufo', 
    'Roboto-Delta-XOUC310.ufo', 
    'Roboto-Delta-XTFI252.ufo', 
    'Roboto-Delta-XTFI488.ufo', 
    'Roboto-Delta-XTLC222.ufo', 
    'Roboto-Delta-XTLC486.ufo', 
    'Roboto-Delta-XTRA244.ufo', 
    'Roboto-Delta-XTRA605.ufo', 
    'Roboto-Delta-XTSP-100.ufo', 
    'Roboto-Delta-XTSP100.ufo', 
    'Roboto-Delta-XTUC323.ufo', 
    'Roboto-Delta-XTUC603.ufo', 
    'Roboto-Delta-YOPQ2.ufo', 
    'Roboto-Delta-YOPQ280.ufo', 
    'Roboto-Delta-YTAS665.ufo', 
    'Roboto-Delta-YTAS875.ufo', 
    'Roboto-Delta-YTDE-100.ufo', 
    'Roboto-Delta-YTDE-310.ufo', 
    'Roboto-Delta-YTFI560.ufo', 
    'Roboto-Delta-YTFI788.ufo', 
    'Roboto-Delta-YTLC426.ufo', 
    'Roboto-Delta-YTLC584.ufo', 
    'Roboto-Delta-YTOS-50.ufo', 
    'Roboto-Delta-YTOS0.ufo', 
    'Roboto-Delta-YTOS50.ufo', 
    'Roboto-Delta-YTUC528.ufo', 
    'Roboto-Delta-YTUC778.ufo',
    
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

