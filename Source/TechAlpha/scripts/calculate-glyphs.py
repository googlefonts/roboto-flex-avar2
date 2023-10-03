from importlib import reload
import variableValues.glyphCalculator
reload(variableValues.glyphCalculator)

import os
from variableValues.glyphCalculator import GlyphCalculator

baseFolder      = os.path.dirname(os.getcwd())
sourcesFolder   = os.path.join(baseFolder, 'sources')
designspacePath = os.path.join(sourcesFolder, 'RobotoFlex.designspace')

f = CurrentFont()

G = GlyphCalculator(f, designspacePath)

for k, v in G.default.items():
    print(k, v)

parameters = {
    # "slnt" :   10,
    # "GRAD" :  100,
    # "XOPQ" :  10,
    # "YOPQ" :  58,
    # "XTRA" :  734,
    # "XTUC" :  734,
    # "XTLC" :  480,
    # "XTFI" :  548,
    # "YTUC" :  1456,
    # "YTLC" :  1072,
    # "YTFI" :  1516,
    # "YTAS" :  1536,
    # "YTDE" :  -416,
}

g = CurrentGlyph()

glyphNames = f.selectedGlyphNames if g is None else g.name

for glyphName in glyphNames:
    G.calculate(glyphName, parameters)

