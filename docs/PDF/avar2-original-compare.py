import os, json

proofsFolder  = os.path.dirname(os.getcwd())
baseFolder    = os.path.dirname(proofsFolder)
fontsFolder   = os.path.join(baseFolder, 'fonts')
font1_name    = 'RobotoFlex'
font1   = os.path.join(proofsFolder, 'HTML', 'RobotoFlex[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght].ttf')
font1_label   = font1_name

font2_name    = 'RobotoAvar2'
font2   = os.path.join(fontsFolder, 'LGCAlpha', 'RobotoA2-avar2-VF.ttf')
font2_label   = font2_name

ASCII  = '''\
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789 .,:;!? @#$%&*
{|}[\](/)_<=>+~- '"^`
'''

p  = 18
fs = 28

savePDF = False

proofName = f'avar2-original-compare.pdf'
pdfPath = os.path.join(os.getcwd(), proofName)

for opsz in [8, 14, 144]:
    for wdth in [50, 100, 150]:
        for wght in range(100, 1001, 100):
            variations = {
                'opsz' : opsz,
                'wght' : wght,
                'wdth' : wdth,
            }
            newPage('A4Landscape')

            W = width()-p*2
            H = (height()-p*3) / 2

            T1 = FormattedString()
            T1.font(font1)
            T1.fontSize(fs)
            T1.lineHeight(fs*1.3)
            T1.fontVariations(**variations)
            T1.append(ASCII, align='center')

            # HACK TO MAKE AVAR2 FONT WORK
            font(font2)
            _variations = fontVariations()
            for k, v in variations.items():
                _variations[k] = v

            T2 = FormattedString()
            T2.font(font2)
            T2.fontSize(fs)
            T2.lineHeight(fs*1.3)
            T2.fontVariations(**_variations)
            T2.append(ASCII, align='center')

            textBox(T2, (p, p, W, H*2))
            textBox(T1, (p, p, W, H))

            with savedState():
                txt1 = f'{font1_name}'
                txt2 = f'{font2_name}'
                font('Menlo')
                fontSize(9)
                fill(1, 0, 0)
                with savedState():
                    translate(p, height()*0.5)
                    rotate(90)
                    text(txt1, (-H*0.5, 0), align='left')
                    text(txt2, (H*0.5, 0), align='left')

                text(f'opsz{opsz} wght{wght} wdth{wdth}', (W/2, p), align='center')

if savePDF:
    saveImage(pdfPath)

