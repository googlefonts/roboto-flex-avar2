font = CurrentFont()

glyphs = ""

for g in font.glyphOrder:
    
    if font[g].selected:
        glyphs = glyphs + font[g].name + "', '"

print(glyphs)