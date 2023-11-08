# menuTitle: mark glyphs with components

'''
red    : nested components
blue   : multiple components
yellow : one component only

'''

f = CurrentFont()

def getNestingLevels(g, levels=0):
    if g.components:
        levels += 1
        for c in g.components:
            baseGlyph = f[c.baseGlyph]
            levels = getNestingLevels(baseGlyph, levels)
    return levels

for g in f:
    g.markColor = None
    if not(g.components):
        continue
    if len(g.components) == 1:
        g.markColor = 1, 1, 0, 0.5
    else:
        levels = getNestingLevels(g)
        if levels > 1:
            g.markColor = 1, 0, 0, 0.5
        else:
            g.markColor = 0, 0, 1, 0.5

f.changed()