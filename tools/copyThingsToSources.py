

#from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

SRC_PATH = '../source/Parametric-avar2/'

DST_PATH = '../source/Parametric-avar2/'

SOURCES = [
            'Roboto-Delta-STLI2.ufo',            'Roboto-Delta-STLI412.ufo',            'Roboto-Delta-STLO2.ufo',            'Roboto-Delta-STLO426.ufo',            'Roboto-Delta-STUI2.ufo',            'Roboto-Delta-STUI736.ufo',            'Roboto-Delta-STUO2.ufo',            'Roboto-Delta-STUO722.ufo',            'Roboto-Delta-VANG-3.ufo',            'Roboto-Delta-VANG13.ufo',            'Roboto-Delta-VROT13.ufo',            'Roboto-Delta-XOAC50.ufo',            'Roboto-Delta-XOFI2.ufo',            'Roboto-Delta-XOFI300.ufo',            'Roboto-Delta-XOLC2.ufo',            'Roboto-Delta-XOLC294.ufo',            'Roboto-Delta-XOPQ2.ufo',            'Roboto-Delta-XOPQ310.ufo',            'Roboto-Delta-XOUC2.ufo',            'Roboto-Delta-XOUC310.ufo',            'Roboto-Delta-XTFI244.ufo',            'Roboto-Delta-XTFI741.ufo',            'Roboto-Delta-XTLC244.ufo',            'Roboto-Delta-XTLC741.ufo',            'Roboto-Delta-XTRA244-opsz144-wdth25-wght100.ufo',            'Roboto-Delta-XTRA244.ufo',            'Roboto-Delta-XTRA741-opsz144-wdth151-wght100.ufo',            'Roboto-Delta-XTRA741.ufo',            'Roboto-Delta-XTSP-100.ufo',            'Roboto-Delta-XTSP100.ufo',            'Roboto-Delta-XTTW0.ufo',            'Roboto-Delta-XTTW30.ufo',            'Roboto-Delta-XTUC244.ufo',            'Roboto-Delta-XTUC741.ufo',            'Roboto-Delta-XTUD741.ufo',            'Roboto-Delta-YOPQ2.ufo',            'Roboto-Delta-YOPQ280.ufo',            'Roboto-Delta-YTAS665.ufo',            'Roboto-Delta-YTAS875.ufo',            'Roboto-Delta-YTDE-100.ufo',            'Roboto-Delta-YTDE-310.ufo',            'Roboto-Delta-YTFI270.ufo',            'Roboto-Delta-YTFI793.ufo',            'Roboto-Delta-YTLC426.ufo',            'Roboto-Delta-YTLC584.ufo',            'Roboto-Delta-YTOS0.ufo',            'Roboto-Delta-YTOS50.ufo',            'Roboto-Delta-YTTL0.ufo',            'Roboto-Delta-YTTL50.ufo',            'Roboto-Delta-YTUC528.ufo',            'Roboto-Delta-YTUC778.ufo',
]

DEFAULT_PATH = SRC_PATH + 'Roboto-Delta-wght400.ufo'

## cent, ordfeminine, ordmasculine, Thorn, germandbls, thorn, eth, ringcomb, six, nine, Euro,
#glyphsToCopy = [  'brevecomb', 'breveinvertedcomb', 'brevebelowcomb', 'brevecomb-stack', 'breveinvertedcomb.stack', 'brevecomb.case', 'breveinvertedcomb.case', 'brevebelowcomb.case', 'brevecombstack.case', 'brevecomb-stack.case', 'breveinvertedcomb-stack.case', ]

##glyphsToCopy = [  'circumflexcomb.case', 'caroncomb.case', 'circumflexcombstack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case',  ]

##glyphsToCopy = [  'L', 'l', 'diagonalbarl'  ]

##glyphsToCopy = [  'Germandbls', 'germandbls'  ]

##glyphsToCopy = [  'four.prop', 'foursuperior'  ]

# glyphsToCopy = [  'sha.bgr', ]

# glyphsToCopy = [  'eta', ]

# glyphsToCopy = [  'upsilon', ]

# glyphsToCopy = [  'horizontalbar', 'horizontalbarlc', ]

# glyphsToCopy = [  'dcroat' ]

# glyphsToCopy = [  'horizontalbar', 'Eth', 'Dcroat', 'Tbar', ]

# glyphsToCopy = [  'Ghestroke' ]

# glyphsToCopy = [  'd', 'h', 'dcroat', 'hbar', ]

# glyphsToCopy = [ 'emspace', 'threeperemspace', 'fourperemspace', 'sixperemspace', 'figurespace', 'hairspace', 'figuredash', 'threequartersemdash', ]

def copyGlyphsToSources(fonts):

    for font in fonts:
    
        src_fontName = DEFAULT_PATH
        src_font = OpenFont(src_fontName, showInterface=False)
        
        dst_fontName = DST_PATH + font
        dst_font = OpenFont(dst_fontName, showInterface=False)
        
        for glyph in glyphsToCopy:
            
            width_glyph = src_font[glyph].width
            dst_font[glyph] = src_font[glyph]
            dst_font[glyph].width = width_glyph

        dst_font.save()
        print('Copied glyphs at ' + dst_fontName)



# copyGlyphsToSources(SOURCES)


def setGlyphOrderToSources(fonts):
    
    for font in fonts:
    
        src_fontName = DEFAULT_PATH
        src_font = OpenFont(src_fontName, showInterface=False)
        
        dst_fontName = DST_PATH + font
        dst_font = OpenFont(dst_fontName, showInterface=False)
        
        if not dst_font.glyphOrder == src_font.glyphOrder:

            dst_font.glyphOrder = src_font.glyphOrder
            dst_font.save()
            
            print('Updated glyphOrder at ' + dst_fontName)
    
setGlyphOrderToSources(SOURCES)



