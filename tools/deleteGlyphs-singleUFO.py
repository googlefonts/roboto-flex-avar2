dst_font = CurrentFont()

##ASCII
selectedGlyphs = ['exclam.ital', 'quotedbl.ital', 'numbersign.ital', 'dollar.ital', 'percent.ital', 'ampersand.ital', 'quotesingle.ital', 'parenleft.ital', 'parenright.ital', 'asterisk.ital', 'plus.ital', 'comma.ital', 'hyphen.ital', 'period.ital', 'slash.ital', 'zero.ital', 'one.ital', 'two.ital', 'three.ital', 'four.ital', 'five.ital', 'six.ital', 'seven.ital', 'eight.ital', 'nine.ital', 'colon.ital', 'semicolon.ital', 'less.ital', 'equal.ital', 'greater.ital', 'question.ital', 'at.ital', 'A.ital', 'B.ital', 'C.ital', 'D.ital', 'E.ital', 'F.ital', 'G.ital', 'H.ital', 'I.ital', 'J.ital', 'K.ital', 'L.ital', 'M.ital', 'N.ital', 'O.ital', 'P.ital', 'Q.ital', 'R.ital', 'S.ital', 'T.ital', 'U.ital', 'V.ital', 'W.ital', 'X.ital', 'Y.ital', 'Z.ital', 'bracketleft.ital', 'backslash.ital', 'bracketright.ital', 'asciicircum.ital', 'underscore.ital', 'grave.ital', 'a.ital', 'b.ital', 'c.ital', 'd.ital', 'e.ital', 'f.ital', 'g.ital', 'h.ital', 'i.ital', 'j.ital', 'k.ital', 'l.ital', 'm.ital', 'n.ital', 'o.ital', 'p.ital', 'q.ital', 'r.ital', 's.ital', 't.ital', 'u.ital', 'v.ital', 'w.ital', 'x.ital', 'y.ital', 'z.ital', 'braceleft.ital', 'bar.ital', 'braceright.ital', 'asciitilde.ital', 'zerosuperior.ital', 'fraction.ital', 'gravecomb.ital', 'idotless.ital', 'jdotless.ital',  ]


for glyphName in selectedGlyphs:
    
    if glyphName in dst_font:
        del dst_font[glyphName]
    else:
        print("font does not contain a glyph named '%s'" % glyphName)
        
    #dst_font.save()
    print('Deleted glyphs at ' )