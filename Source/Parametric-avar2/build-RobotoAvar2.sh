
source tools/robotoflexA2-env/bin/activate

## MAKE VF

## full glyphset
#fontmake -m source/Parametric-avar2/RobotoAvar2-avar1.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar1-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/RobotoAvar2-avar2.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar2-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/RobotoAvar2-avar2-fences.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar2-fences-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/RobotoAvar2-avar2-clean.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar2-clean-VF.ttf --no-production-names


deactivate