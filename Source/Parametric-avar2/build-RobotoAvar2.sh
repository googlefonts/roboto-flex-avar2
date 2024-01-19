
source tools/robotoflexA2-env/bin/activate

## MAKE VF

#fontmake -m Parametric-avar2/RobotoAvar2-avar1.designspace -o variable --output-path fonts/AsciiAlpha/RobotoA2-avar1-VF.ttf --no-production-names
fontmake -m Parametric-avar2/RobotoAvar2-avar2.designspace -o variable --output-path fonts/AsciiAlpha/RobotoA2-avar2-VF.ttf --no-production-names
fontmake -m Parametric-avar2/RobotoAvar2-avar2-fences.designspace -o variable --output-path fonts/AsciiAlpha/RobotoA2-avar2-fences-VF.ttf --no-production-names

## SUBSET ascii

python Parametric-avar2/subset.py


## MAKE INSTANCES

#fontmake -m Parametric-avar2/RobotoAvar2-avar1.designspace -i -o ufo --output-dir Parametric-avar2/instances/


#Partial VFs

#fonttools varLib.instancer fonts/RobotoAvar2[]-VF.ttf opsz=144 wdth=25:151 wght=1:1000

deactivate