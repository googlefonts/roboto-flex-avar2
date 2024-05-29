
import os, glob, datetime
from fontParts.world import OpenFont
from variableValues.validation import *

def checkGlyph(g1, g2):
    return {
        'width'          : validateWidth(g1, g2),
        'points'         : validateContours(g1, g2),
        'pointPositions' : equalContours(g1, g2),
        'components'     : validateComponents(g1, g2),
        'anchors'        : validateAnchors(g1, g2),
        'unicodes'       : validateUnicodes(g1, g2),
    }

# subFamilyName = ['Roman', 'Italic'][0]
baseFolder    = os.path.dirname(os.path.dirname(os.getcwd()))
sourcesFolder = os.path.join(baseFolder, 'Source', 'Parametric-avar2')
defaultPath   = os.path.join(sourcesFolder, f'RobotoAvar2-wght400.ufo')

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

assert os.path.exists(defaultPath)

ufoPaths = glob.glob(f'{sourcesFolder}/*.ufo')
ufoPaths.remove(defaultPath)

defaultFont = OpenFont(defaultPath, showInterface=False)

glyphNames = defaultFont.glyphOrder

ufoPaths.insert(0, defaultPath)

for ufoPath in ufoPaths:

    currentFont = OpenFont(ufoPath, showInterface=False)

    newPage('A4Landscape')

    m = 25, 10, 10, 10
    stepsX, stepsY = 41, 26
    # print(stepsX*stepsY)

    colorContours   = 0,
    colorComponents = 0.65,

    stepX = (width()-m[1]-m[3])/stepsX
    stepY = (height()-m[0]-m[2])/stepsY

    font('Menlo-Bold')

    fontSize(9)
    text(f'RobotoAvar2', (m[3], height()-m[0]*0.66), align='left')
    text(f'{currentFont.info.styleName}', (width()/2, height()-m[0]*0.66), align='center')
    text(now, (width()-m[1], height()-m[0]*0.66), align='right')

    stroke(0.85)
    strokeWidth(0.5)
    fill(None)
    fontSize(6)

    s = 0.005

    n = 0
    for i in range(stepsY):
        for j in range(stepsX):
            x = m[3] + j * stepX
            y = height() - m[0] - (i+1) * stepY

            if n > len(glyphNames)-1:
                break

            rect(x, y, stepX, stepY)

            glyphName = glyphNames[n]
            defaultGlyph = defaultFont[glyphName]
            if glyphName not in currentFont:
                continue

            currentGlyph = currentFont[glyphName]

            results = checkGlyph(defaultGlyph, currentGlyph)

            if currentGlyph.bounds:
                L, B, R, T = currentGlyph.bounds
                W = R-L
                _x = x + (stepX - W * s) / 2
                _y = y + stepY * 0.3
                with savedState():
                    stroke(None)
                    if currentGlyph.components and not currentGlyph.contours:
                        c = colorComponents
                    else:
                        c = colorContours
                    fill(*c)
                    translate(_x, _y)
                    scale(s)
                    drawGlyph(currentGlyph)
            else:
                print(f'no bounds for {glyphName}')

            with savedState():
                stroke(None)
                translate(x, y)
                font('Menlo-Bold')
                fontSize(3.5)
                for check in results.keys():
                    if check == 'pointPositions':
                        continue
                    if results[check]:
                        fill(0, 1, 0)
                        if check == 'points' and results['pointPositions']:
                            fill(0, 0, 1)
                    else:
                        fill(1, 0, 0)
                    label = check[0].upper()
                    text(label, (1, 1))
                    w, h = textSize(label)
                    translate(w+0.5, 0)
                
            n += 1

pdfPath = os.path.join(os.getcwd(), f'sources-glyphset.pdf')
saveImage(pdfPath)
# newDrawing()

