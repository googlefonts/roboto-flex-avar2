size('A4')
fontSize(64)
x = width()/2
y = height()-90

for fontName in installedFonts():
    if not 'RobotoFlex' in fontName:
        continue
    print(fontName)
    font(fontName)
    text('Handgloves', (x, y), align='center')
    with savedState():
        fill(1, 0, 0)
        fontSize(13)
        font('Menlo-Bold')
        text(fontName, (x, y-32), align='center')
    y -= 112
