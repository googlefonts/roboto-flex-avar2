
SRC_PATH = '../source/Parametric-avar2/'

DST_PATH = '../source/Parametric-avar2/'

# ## ASCII
# glyphs = ['exclam', 'quotedbl', 'numbersign', 'dollar', 'percent', 'ampersand', 'quotesingle', 'parenleft', 'parenright', 'asterisk', 'plus', 'comma', 'hyphen', 'period', 'slash', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'colon', 'semicolon', 'less', 'equal', 'greater', 'question', 'at', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore', 'grave', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'braceleft', 'bar', 'braceright', 'asciitilde', 'zerosuperior', 'fraction', 'gravecomb', 'idotless', 'jdotless', ]

# ## FULL REPERTOIRE
selectedGlyphs = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Germandbls', 'germandbls', 'paragraph', 'dollar', 'sterling', 'yen', 'numbersign', 'Euro', 'franc', 'lira', 'naira', 'peseta', 'won', 'dong', 'rupeeIndian', 'liraTurkish', 'manat', 'ruble', 'numero', 'commercialMinusSign', 'florin', 'coloncurrency', 'uni20AD', 'uni20B1', 'uni20B2', 'uni20B5', 'hryvnia', 'tenge', 'dollar.rvrn', 'cent.rvrn', 'coloncurrency.rvrn', 'naira.rvrn', 'won.rvrn', 'uni20B1.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.prop', 'one.prop', 'two.prop', 'three.prop', 'four.prop', 'five.prop', 'six.prop', 'seven.prop', 'eight.prop', 'nine.prop', 'cent', 'ordfeminine', 'ordmasculine', 'less', 'greater', 'equal', 'at', 'plus', 'percent', 'grave', 'period', 'semicolon', 'colon', 'quotesingle', 'quotedbl', 'ampersand', 'questiondown', 'question', 'exclamdown', 'exclam', 'parenleft', 'slash', 'parenright', 'bracketleft', 'backslash', 'bracketright', 'braceleft', 'bar', 'braceright', 'brokenbar', 'asterisk', 'comma', 'periodcentered', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotedblleft', 'quotedblright', 'quotedblbase', 'guilsinglleft', 'guilsinglright', 'guillemotleft', 'guillemotright', 'underscore', 'hyphen', 'hyphentwo', 'endash', 'emdash', 'softhyphen', 'trademark', 'asciicircum', 'asciitilde', 'zerosuperior', 'onesuperior', 'twosuperior', 'threesuperior', 'foursuperior', 'fraction', 'divisionslash', 'primemod', 'doubleprimemod', 'apostrophemod', 'horizontalbar', 'minute', 'second', 'leftanglebracket', 'rightanglebracket', ]
selectedGlyphs += [ 'gravecomb', 'acutecomb', 'circumflexcomb', 'tildecomb', 'macroncomb', 'brevecomb', 'dotaccentcomb', 'dieresiscomb', 'hookabovecomb', 'ringcomb', 'hungarumlautcomb', 'caroncomb', 'breveinvertedcomb', 'dblgravecomb', 'horncomb', 'dotbelowcomb', 'dieresisbelowcomb', 'commaaccentcomb', 'cedillacomb', 'ogonekcomb', 'brevebelowcomb', 'macronbelowcomb', 'commaaccentturnedcomb', 'gravecomb-stack', 'acutecomb-stack', 'dieresiscomb-stack', 'macroncomb-stack', 'circumflexcomb-stack', 'caroncomb-stack', 'brevecomb-stack', 'dotaccentcomb-stack', 'ringcomb-stack', 'tildecomb-stack', 'hungarumlautcomb-stack', 'hookabovecomb-stack', 'breveinvertedcomb.stack', 'dblgravecomb-stack', ]
selectedGlyphs += [ 'gravecomb.case', 'acutecomb.case', 'dieresiscomb.case', 'macroncomb.case', 'cedillacomb.case', 'circumflexcomb.case', 'caroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'ringcomb.case', 'ogonekcomb.case', 'tildecomb.case', 'hungarumlautcomb.case', 'hookabovecomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'gravecombstack.case', 'acutecombstack.case', 'dieresiscombstack.case', 'macroncombstack.case', 'circumflexcombstack.case', 'brevecombstack.case', 'dotaccentcombstack.case', 'tildecombstack.case', 'hookabovecombstack.case', ]
selectedGlyphs += [ 'gravecomb-stack.case', 'acutecomb-stack.case', 'dieresiscomb-stack.case', 'macroncomb-stack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case', 'brevecomb-stack.case', 'dotaccentcomb-stack.case', 'ringcomb-stack.case', 'tildecomb-stack.case', 'hungarumlautcomb-stack.case', 'hookcomb-stack.case', 'breveinvertedcomb-stack.case', 'dblgravecomb-stack.case', ]
selectedGlyphs += [ 'AE', 'Thorn', 'ae', 'eth', 'thorn', 'kgreenlandic', 'OE', 'oe', 'idotless', 'jdotless', 'Schwa', 'schwa', ]
selectedGlyphs += [ 'caroncomb.alt', 'diagonalbarO', 'diagonalbarl', 'diagonalbaro', 'engtail', 'horizontalbarH', 'horizontalbarlc', 'diagonalbarL', 'diagonalbarO.rvrn', 'diagonalbaro.rvrn', ]
selectedGlyphs += [ 'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi', 'Omega', 'Kaisymbol', 'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'xi', 'pi', 'rho', 'finalsigma', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'kaisymbol', 'numeralsign', 'lownumeralsign', 'tonoscomb', 'tonoscomb.case', ] # 'dieresistonoscomb', 'dieresistonoscomb.case',
selectedGlyphs += [ 'Dje', 'Ieukran', 'Lje', 'Nje', 'Tshe', 'Dzhe', 'Be', 'De', 'Zhe', 'Ze', 'Icyr', 'Ka', 'El', 'Ucyr', 'Tse', 'Che', 'Sha', 'Hard', 'Soft', 'Ecyr', 'Ya', 'Gheup', 'Kaverticalstrokecyr', 'Kabashkircyr', 'Cheverticalstroke-cy', 'Shha', 'De.bgr', 'Zhe.bgr', 'be', 've', 'ghe', 'de', 'zhe', 'ze', 'icyr', 'ka', 'el', 'em', 'en', 'pe', 'te', 'tse', 'che', 'sha', 'hard', 'soft', 'ecyr', 'ya', 'ieukran', 'lje', 'nje', 'dzhe', 'gheup', 'kaverticalstrokecyr', 'kabashkircyr', 'ustraight', 'cheverticalstroke-cy', 've.bgr', 'ghe.bgr', 'zhe.bgr', 'ze.bgr', 'el.bgr', 'sha.bgr', 'hard.bgr', 'soft.bgr', 'be.locl', 'breve.cyrcomb.case', 'breve.cyrcomb', 'Cy-descendercomb.case', 'cy-descendercomb', 'U-stroke', 'u-stroke', 'Obarcyr-stroke', 'Hacyr-stroke', 'obarcyr-stroke', 'hacyr-stroke', 'Yu-dash.case', 'yu-dash', ]

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
        'RobotoAvar2-XTRA741-opsz144-wdth151-wght100.ufo', 
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
makeShearTransformGlyphs(ufos, selectedGlyphs)

## XTUD SPARSE
#makeShearTransformGlyphs(['RobotoAvar2-XTUD741.ufo', ], ['A', 'I', 'K', 'L', 'M', 'N', 'V', 'W', 'AE', 'naira', 'won', 'naira.rvrn', 'won.rvrn', 'numero', 'J', ] )

## print designspace rules for inclusion
#printRules(glyphs)
