
SRC_PATH = '../source/Parametric-avar2/'

DST_PATH = '../source/Parametric-avar2/'

glyphs = ['exclam', 'quotedbl', 'numbersign', 'dollar', 'percent', 'ampersand', 'quotesingle', 'parenleft', 'parenright', 'asterisk', 'plus', 'comma', 'hyphen', 'period', 'slash', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'colon', 'semicolon', 'less', 'equal', 'greater', 'question', 'at', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore', 'grave', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'braceleft', 'bar', 'braceright', 'asciitilde', 'zerosuperior', 'fraction', 'gravecomb', 'idotless', 'jdotless', ]

ufos = [
        'RobotoAvar2-wght400.ufo', 
        'RobotoAvar2-STUO722.ufo', 
        'RobotoAvar2-STUO2.ufo', 
        'RobotoAvar2-STUI736.ufo', 
        'RobotoAvar2-STUI2.ufo', 
        'RobotoAvar2-STLO426.ufo', 
        'RobotoAvar2-STLO2.ufo', 
        'RobotoAvar2-STLI412.ufo', 
        'RobotoAvar2-STLI2.ufo', 
        'RobotoAvar2-VANG13.ufo', 
        'RobotoAvar2-VANG13-opsz144.ufo', 
        'RobotoAvar2-VANG13-opsz144-wght1000.ufo', 
        'RobotoAvar2-VANG13-opsz144-wght100.ufo', 
        'RobotoAvar2-VANG-3.ufo', 
        'RobotoAvar2-XOFI2.ufo', 
        'RobotoAvar2-XOFI300.ufo', 
        'RobotoAvar2-XOLC2.ufo', 
        'RobotoAvar2-XOLC294.ufo', 
        'RobotoAvar2-XOPQ2.ufo', 
        'RobotoAvar2-XOPQ310.ufo', 
        'RobotoAvar2-XOUC2.ufo', 
        'RobotoAvar2-XOUC310.ufo', 
        'RobotoAvar2-XTFI244.ufo', 
        'RobotoAvar2-XTFI741.ufo', 
        'RobotoAvar2-XTLC244.ufo', 
        'RobotoAvar2-XTLC741.ufo', 
        'RobotoAvar2-XTRA244-opsz144-wdth25-wght100.ufo', 
        'RobotoAvar2-XTRA244.ufo', 
        'RobotoAvar2-XTRA741.ufo', 
        'RobotoAvar2-XTSP-100.ufo', 
        'RobotoAvar2-XTSP100.ufo', 
        'RobotoAvar2-XTTW0.ufo', 
        'RobotoAvar2-XTTW30.ufo', 
        'RobotoAvar2-XTUC244.ufo', 
        'RobotoAvar2-XTUC741.ufo', 
        'RobotoAvar2-YOPQ2.ufo', 
        'RobotoAvar2-YOPQ280.ufo', 
        'RobotoAvar2-YTAS665.ufo', 
        'RobotoAvar2-YTAS875.ufo', 
        'RobotoAvar2-YTDE-100.ufo', 
        'RobotoAvar2-YTDE-310.ufo', 
        'RobotoAvar2-YTFI270.ufo', 
        'RobotoAvar2-YTFI793.ufo', 
        'RobotoAvar2-YTLC426.ufo', 
        'RobotoAvar2-YTLC584.ufo', 
        'RobotoAvar2-YTOS0.ufo', 
        'RobotoAvar2-YTOS50.ufo', 
        'RobotoAvar2-YTTL0.ufo', 
        'RobotoAvar2-YTTL50.ufo', 
        'RobotoAvar2-YTUC528.ufo', 
        'RobotoAvar2-YTUC778.ufo', 

    ]


def makeShearTransformGlyphs(dst_fonts, glyphs):

    # src_fontName = SRC_PATH + src_font
    # src_font = OpenFont(src_fontName, showInterface=False)
    
    for dst_font in dst_fonts:
        
        dst_fontName = DST_PATH + dst_font
        dst_font = OpenFont(dst_fontName, showInterface=False)

        for glyph in glyphs:
        
            dst_font.newGlyph( glyph + '.ital' )

            newGlyph =  dst_font[glyph + '.ital']

            newGlyph.width = dst_font[glyph].width

            newGlyph.appendComponent(glyph)

            newGlyph.transformBy((1, 0, 0.21255656167002213, 1, 0, 0), origin=( newGlyph.width / 2, 728))
            
            ## offset , origin=( (newGlyph.width / 2) ), 0)
            
        dst_font.save()
        print('Made shear transform glyphs at ' + dst_fontName)

def printRules(glyphs):
    
    for glyph in glyphs:
        
        print( '<sub name="' + glyph + '" with="' + glyph + '.ital"/>' )

## make glyphs wit shear transformations to ufoslist 
#makeShearTransformGlyphs(ufos, glyphs)

## XTUD SPARSE
makeShearTransformGlyphs(['RobotoAvar2-XTUD741.ufo', ], ['A', 'I', 'K', 'L', 'M', 'N', 'V', 'W', 'AE', 'naira', 'won', 'naira.rvrn', 'won.rvrn', 'numero', 'J', ] )

## print designspace rules for inclusion
#printRules(glyphs)
