import os, datetime

baseFolder = os.path.dirname(os.path.dirname(os.getcwd()))
fontsFolder = os.path.join(baseFolder, 'fonts', 'LGCAlpha')

fontPath = os.path.join(fontsFolder, f'RobotoA2-avar2-VF.ttf')

assert os.path.exists(fontPath)

ASCII  = list('''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?@#$%&*{|}[\](/)_<=>+~-'"^`''')

fs = 36
p = 30, 10, 10, 10

stepsX = 12
stepsY = 8

wghts = range(100, 1001, 100)
wdths = [50, 100, 150]
opszs = [8, 14, 144]

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

savePDF = True

proofName = f'sources-weights.pdf'
pdfPath   = os.path.join(os.getcwd(), proofName)

for opsz in opszs:
    for wdth in wdths:

        newPage('A4Landscape')

        with savedState():
            x1 = p[3]
            x2 = width() / 2
            x3 = width() - p[1]
            y = height() - p[0]*0.57
            font('Menlo')
            fontSize(9)
            fill(1, 0, 0)
            text(f'RobotoAvar2', (x1, y), align='left')
            text(f'opsz{opsz} wdth{wdth}', (x2, y), align='center')
            text(f'{now}', (x3, y), align='right')

        strokeWidth(0.5)
        stroke(1, 0, 0)
        fill(None)
        fontSize(fs)
        font(fontPath)

        _variations = fontVariations()
        _variations['opsz'] = opsz
        _variations['wdth'] = wdth

        stepX = (width()-p[1]-p[3])  / stepsX
        stepY = (height()-p[0]-p[2]) / stepsY

        y = height() - p[0] - stepY

        n = 0
        for i in range(stepsY):
            x = p[3]
            for j in range(stepsX):
                if n < len(ASCII):
                    with savedState():
                        pos = x + stepX / 2, y + stepX * 0.33
                        stroke(None)
                        fill(0, 0.1)
                        for wght in wghts:
                            _variations['wght'] = wght
                            fontVariations(**_variations)
                            text(ASCII[n], pos, align='center')

                    rect(x, y, stepX, stepY)

                    n += 1
                    x += stepX

            y -= stepY

if savePDF:
    saveImage(pdfPath)

