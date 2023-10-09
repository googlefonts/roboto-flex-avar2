import os
from defcon import Font
from fontTools.designspaceLib import DesignSpaceDocument
from fontmake.font_project import FontProject

baseFolder      = os.path.dirname(os.getcwd())
sourcesFolder   = os.path.join(baseFolder, 'sources')
designspacePath = os.path.join(sourcesFolder, 'RobotoFlex.designspace')
fontsFolder     = os.path.join(baseFolder, 'fonts')
varFontPath     = os.path.join(fontsFolder, 'RobotoFlex-avar2.ttf')

assert os.path.exists(designspacePath)

D = DesignSpaceDocument()
D.read(designspacePath)
for src in D.sources:
    print(f'\tloading {src.path}...')
    src.font = Font(src.path)
print('...done.\n')

print('generating variable font... ', end='')
P = FontProject()
P.build_variable_fonts(D, output_path=varFontPath, verbose=True)
print('done!\n')

print(varFontPath, os.path.exists(varFontPath))
