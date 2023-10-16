import os
from defcon import Font
from fontTools.designspaceLib import DesignSpaceDocument
from fontmake.font_project import FontProject
from ufo2ft import compileVariableTTF

baseFolder      = os.path.dirname(os.getcwd())
sourcesFolder   = os.path.join(baseFolder, 'sources')
designspacePath = os.path.join(sourcesFolder, 'RobotoFlex3.designspace')
fontsFolder     = os.path.join(baseFolder, 'fonts')
varFontPath     = designspacePath.replace(sourcesFolder, fontsFolder).replace('.designspace', '.ttf')

assert os.path.exists(designspacePath)

print(f'generating variable font for {designspacePath}...')

D = DesignSpaceDocument()
D.read(designspacePath)
print(f'\tloading sources...')
for src in D.sources:
    src.font = Font(src.path)

print('\tbuilding variable font...')

### build variable font with fontmake
# P = FontProject()
# P.build_variable_fonts(D, output_path=varFontPath, verbose=True)

### build variable font with ufo2ft
f = compileVariableTTF(D)
f.save(varFontPath)

print('...done.\n')

print(varFontPath, os.path.exists(varFontPath))
