import os, glob

baseFolder    = os.path.dirname(os.getcwd())
sourcesFolder = os.path.join(baseFolder, 'sources')
extremaFolder = os.path.join(sourcesFolder, 'extrema')

sources = glob.glob(f'{sourcesFolder}/*.ufo')

fea = '' # include(features/RobotoFlex.fea)

for sourcePath in sources:
    f = OpenFont(sourcePath, showInterface=False)
    if '../features' in f.features.text:
        print(sourcePath)
        print(f.features.text)
        f.features.text = f.features.text.replace('../', '')
        print(f.features.text)
    f.save()
    print()