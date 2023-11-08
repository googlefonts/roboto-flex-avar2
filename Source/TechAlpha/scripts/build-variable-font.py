# menuTitle: build Roboto Flex avar2 variable fonts

import os
from defcon import Font
from fontTools.designspaceLib import DesignSpaceDocument
from ufo2ft import compileVariableTTF

baseFolder      = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
sourcesFolder   = os.path.join(baseFolder, 'Source', 'TechAlpha', 'sources')
designspacePath = os.path.join(sourcesFolder, 'RobotoFlex1.designspace')
fontsFolder     = os.path.join(baseFolder, 'fonts', 'Tech Alpha TTFs')
varFontPath     = designspacePath.replace(sourcesFolder, fontsFolder).replace('.designspace', '.ttf')

assert os.path.exists(designspacePath)

print(f'generating variable font for {designspacePath}...')

D = DesignSpaceDocument()
D.read(designspacePath)
print(f'\tloading sources...')
for src in D.sources:
    src.font = Font(src.path)

print('\tbuilding variable font...')

# build variable font with ufo2ft
f = compileVariableTTF(D)
f.save(varFontPath)

print('...done.\n')

print(varFontPath, os.path.exists(varFontPath))
