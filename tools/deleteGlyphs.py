
SRC_PATH = '../source/Parametric-avar2/'

DST_PATH = '../source/Parametric-avar2/'

selectedGlyphs = ['exclam.ital', 'quotedbl.ital', 'numbersign.ital', 'dollar.ital', 'percent.ital', 'ampersand.ital', 'quotesingle.ital', 'parenleft.ital', 'parenright.ital', 'asterisk.ital', 'plus.ital', 'comma.ital', 'hyphen.ital', 'period.ital', 'slash.ital', 'zero.ital', 'one.ital', 'two.ital', 'three.ital', 'four.ital', 'five.ital', 'six.ital', 'seven.ital', 'eight.ital', 'nine.ital', 'colon.ital', 'semicolon.ital', 'less.ital', 'equal.ital', 'greater.ital', 'question.ital', 'at.ital', 'A.ital', 'B.ital', 'C.ital', 'D.ital', 'E.ital', 'F.ital', 'G.ital', 'H.ital', 'I.ital', 'J.ital', 'K.ital', 'L.ital', 'M.ital', 'N.ital', 'O.ital', 'P.ital', 'Q.ital', 'R.ital', 'S.ital', 'T.ital', 'U.ital', 'V.ital', 'W.ital', 'X.ital', 'Y.ital', 'Z.ital', 'bracketleft.ital', 'backslash.ital', 'bracketright.ital', 'asciicircum.ital', 'underscore.ital', 'grave.ital', 'a.ital', 'b.ital', 'c.ital', 'd.ital', 'e.ital', 'f.ital', 'g.ital', 'h.ital', 'i.ital', 'j.ital', 'k.ital', 'l.ital', 'm.ital', 'n.ital', 'o.ital', 'p.ital', 'q.ital', 'r.ital', 's.ital', 't.ital', 'u.ital', 'v.ital', 'w.ital', 'x.ital', 'y.ital', 'z.ital', 'braceleft.ital', 'bar.ital', 'braceright.ital', 'asciitilde.ital', 'zerosuperior.ital', 'fraction.ital', 'gravecomb.ital', 'idotless.ital', 'jdotless.ital',  ]

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
            
            del dst_font[glyph]
        
        dst_font.save()
        print('Deleted glyphs at ' + dst_fontName)

def printRules(glyphs):
    
    for glyph in glyphs:
        
        print( '<sub name="' + glyph + '" with="' + glyph + '.ital"/>' )

# make glyphs wit shear transformations to ufoslist 
makeShearTransformGlyphs(ufos, selectedGlyphs)

# ## XTUD SPARSE
# makeShearTransformGlyphs(['RobotoAvar2-XTUD741.ufo', ], ['A', 'I', 'K', 'L', 'M', 'N', 'V', 'W', 'AE', 'naira', 'won', 'naira.rvrn', 'won.rvrn', 'numero', 'J', ] )


