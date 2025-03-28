
source tools/roboto-delta-env/bin/activate

## MAKE VF

## full glyphset
fontmake -m source/Parametric-avar2/Roboto-Delta.designspace -o variable --output-path fonts/LGCAlpha/Roboto-Delta-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/Roboto-Delta-no-fences.designspace -o variable --output-path fonts/LGCAlpha/Roboto-Delta-no-fences-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/Roboto-Delta-no-slant.designspace -o variable --output-path fonts/LGCAlpha/Roboto-Delta-no-slant-VF.ttf --no-production-names

## MAKE INSTANCES
#fontmake -m source/Parametric-avar2/RobotoAvar2-avar2.designspace -i -o ufo --output-dir source/Parametric-avar2/instances/

deactivate
