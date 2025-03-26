
SRC_PATH = '../source/Parametric-avar2/'

DST_PATH = '../source/Parametric-avar2/'


XOFI = XTFI = YTFI = [ 'dollar', 'sterling', 'yen', 'numbersign', 'Euro', 'franc', 'lira', 'naira', 'peseta', 'won', 'dong', 'rupeeIndian', 'liraTurkish', 'manat', 'ruble', 'numero', 'commercialMinusSign', 'florin', 'coloncurrency', 'uni20AD', 'uni20B1', 'uni20B2', 'uni20B5', 'hryvnia', 'tenge', 'dollar.rvrn', 'cent.rvrn', 'coloncurrency.rvrn', 'naira.rvrn', 'won.rvrn', 'uni20B1.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.prop', 'one.prop', 'two.prop', 'three.prop', 'four.prop', 'five.prop', 'six.prop', 'seven.prop', 'eight.prop', 'nine.prop', 'percent', 'perthousand', 'fraction', 'zerosuperior', 'onesuperior', 'twosuperior', 'threesuperior', 'foursuperior', 'cent', ]

XOLC = XTLC = YTLC = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'germandbls', 'f_f', 'fi', 'fl', 'f_f_i', 'f_f_l', 'f_f_ij', 'f_ij', 'agrave', 'aacute', 'acircumflex', 'atilde', 'adieresis', 'aring', 'ae', 'ccedilla', 'egrave', 'eacute', 'ecircumflex', 'edieresis', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'eth', 'ntilde', 'ograve', 'oacute', 'ocircumflex', 'otilde', 'odieresis', 'oslash', 'ugrave', 'uacute', 'ucircumflex', 'udieresis', 'yacute', 'thorn', 'ydieresis', 'amacron', 'abreve', 'aogonek', 'cacute', 'ccircumflex', 'cdotaccent', 'ccaron', 'dcaron', 'dcroat', 'emacron', 'ebreve', 'edotaccent', 'eogonek', 'ecaron', 'gcircumflex', 'gbreve', 'gdotaccent', 'gcommaaccent', 'hcircumflex', 'hbar', 'itilde', 'imacron', 'ibreve', 'iogonek', 'ij', 'kcommaaccent', 'kgreenlandic', 'lacute', 'lcommaaccent', 'lcaron', 'ldot', 'lslash', 'nacute', 'ncommaaccent', 'ncaron', 'napostrophe', 'eng', 'omacron', 'obreve', 'ohungarumlaut', 'oe', 'racute', 'rcommaaccent', 'rcaron', 'sacute', 'scircumflex', 'scedilla', 'scaron', 'tcedilla', 'tcaron', 'tbar', 'utilde', 'umacron', 'ubreve', 'uring', 'uhungarumlaut', 'uogonek', 'wcircumflex', 'ycircumflex', 'zacute', 'zdotaccent', 'zcaron', 'ohorn', 'uhorn', 'dzcaron', 'idotless', 'jdotless', 'ijacute', 'idotaccent', 'jcircumflex', 'jacute.loclNLD', 'lj', 'nj', 'gcaron', 'oogonek', 'aringacute', 'aeacute', 'oslashacute', 'adblgrave', 'ainvertedbreve', 'edblgrave', 'einvertedbreve', 'idblgrave', 'iinvertedbreve', 'odblgrave', 'oinvertedbreve', 'rdblgrave', 'rinvertedbreve', 'udblgrave', 'uinvertedbreve', 'scommaaccent', 'tcommaaccent', 'odieresismacron', 'otildemacron', 'odotaccentmacron', 'ymacron', 'schwa', 'adotbelow', 'ahookabove', 'acircumflexacute', 'acircumflexgrave', 'acircumflexhookabove', 'acircumflextilde', 'acircumflexdotbelow', 'abreveacute', 'abrevegrave', 'abrevehookabove', 'abrevetilde', 'abrevedotbelow', 'edotbelow', 'ehookabove', 'etilde', 'ecircumflexacute', 'ecircumflexgrave', 'ecircumflexhookabove', 'ecircumflextilde', 'ecircumflexdotbelow', 'ihookabove', 'idotbelow', 'odotbelow', 'ohookabove', 'ocircumflexacute', 'ocircumflexgrave', 'ocircumflexhookabove', 'ocircumflextilde', 'ocircumflexdotbelow', 'ohornacute', 'ohorngrave', 'ohornhookabove', 'ohorntilde', 'ohorndotbelow', 'udotbelow', 'uhookabove', 'uhornacute', 'uhorngrave', 'uhornhookabove', 'uhorntilde', 'uhorndotbelow', 'ygrave', 'ydotbelow', 'yhookabove', 'ytilde', 'wgrave', 'wacute', 'wdieresis', 'grave', 'acute', 'dieresis', 'macron', 'cedilla', 'circumflex', 'caron', 'firsttonechinese', 'breve', 'dotaccent', 'ring', 'ogonek', 'tilde', 'hungarumlaut', 'hookabove', 'breveinverted', 'dblgrave', 'horn', 'dotbelow', 'dieresisbelow', 'commaaccent', 'brevebelow', 'macronbelow', 'commaaccentturned', 'gravecomb', 'acutecomb', 'circumflexcomb', 'tildecomb', 'macroncomb', 'brevecomb', 'dotaccentcomb', 'dieresiscomb', 'hookabovecomb', 'ringcomb', 'hungarumlautcomb', 'caroncomb', 'breveinvertedcomb', 'dblgravecomb', 'horncomb', 'dotbelowcomb', 'dieresisbelowcomb', 'commaaccentcomb', 'cedillacomb', 'ogonekcomb', 'brevebelowcomb', 'macronbelowcomb', 'commaaccentturnedcomb', 'gravecomb-stack', 'acutecomb-stack', 'dieresiscomb-stack', 'macroncomb-stack', 'circumflexcomb-stack', 'caroncomb-stack', 'brevecomb-stack', 'dotaccentcomb-stack', 'ringcomb-stack', 'tildecomb-stack', 'hungarumlautcomb-stack', 'hookabovecomb-stack', 'breveinvertedcomb.stack', 'dblgravecomb-stack', 'grave-stack', 'acute-stack', 'circumflex-stack', 'tilde-stack', 'macron-stack', 'breve-stack', 'dotaccent-stack', 'dieresis-stack', 'hookabove-stack', 'ring-stack', 'hungarumlaut-stack', 'caron-stack', 'breveinverted-stack', 'dblgrave-stack', 'diagonalbarl', 'diagonalbaro', 'engtail', 'horizontalbarlc', 'alpha', 'alphatonos', 'beta', 'gamma', 'delta', 'epsilon', 'epsilontonos', 'zeta', 'eta', 'etatonos', 'theta', 'iota', 'iotadieresistonos', 'iotatonos', 'iotadieresis', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'omicrontonos', 'pi', 'rho', 'finalsigma', 'sigma', 'tau', 'upsilon', 'upsilondieresistonos', 'upsilondieresis', 'upsilontonos', 'phi', 'chi', 'psi', 'omega', 'omegatonos', 'kaisymbol', 'anoteleia', 'tonos', 'tonoscomb', 'dieresistonoscomb', 'acyr', 'abrevecyr', 'adieresiscyr', 'be', 've', 'ghe', 'gje', 'de', 'ie', 'io', 'iebrevecyr', 'zhe', 'zhebrevecyr', 'zhedieresiscyr', 'ze', 'icyr', 'ishort', 'igravecyr', 'ka', 'kje', 'el', 'em', 'en', 'ocyr', 'odieresiscyr', 'pe', 'er', 'es', 'te', 'ucyr', 'ushort', 'umacroncyr', 'udieresiscyr', 'uhungarumlautcyr', 'ef', 'ha', 'tse', 'che', 'sha', 'shcha', 'hard', 'yeru', 'soft', 'ecyr', 'yu', 'ya', 'dje', 'ieukran', 'dze', 'iukran', 'yi', 'je', 'lje', 'nje', 'tshe', 'dzhe', 'gheup', 'ghestroke', 'zhedescender', 'zedescendercyr', 'kadescender', 'kaverticalstrokecyr', 'kabashkircyr', 'endescender', 'esdescendercyr', 'tedescender-cy', 'ustraight', 'ustraightstroke', 'hadescender', 'chedescender-cy', 'cheverticalstroke-cy', 'shha', 'palochka', 'schwacyr', 'obarcyr', 'hastroke-cy', 've.bgr', 'ghe.bgr', 'de.bgr', 'i.bgr', 'igrave.bgr', 'zhe.bgr', 'ze.bgr', 'ka.bgr', 'el.bgr', 'en.bgr', 'pe.bgr', 'te.bgr', 'tse.bgr', 'che.bgr', 'sha.bgr', 'shcha.bgr', 'hard.bgr', 'soft.bgr', 'yu.bgr', 'ishort.bgr', 'be.locl', 'ghe.locl', 'de.locl', 'pe.locl', 'te.locl', 'amacroncyr', 'iemacroncyr', 'omacroncyr', 'obrevecyr', 'emacroncyr', 'ebrevecyr', 'yamacron', 'yumacron', 'breve.cyr', 'yi-dieresis', 'cy-descender', 'breve.cyrcomb', 'yi-dieresiscomb', 'cy-descendercomb', 'u-stroke', 'obarcyr-stroke', 'hacyr-stroke', 'yu-dash', 'idot', ]

XOUC = XTUC = YTUC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Germandbls', 'Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis', 'Aring', 'AE', 'Ccedilla', 'Egrave', 'Eacute', 'Ecircumflex', 'Edieresis', 'Igrave', 'Iacute', 'Icircumflex', 'Idieresis', 'Eth', 'Ntilde', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde', 'Odieresis', 'Oslash', 'Ugrave', 'Uacute', 'Ucircumflex', 'Udieresis', 'Yacute', 'Thorn', 'Amacron', 'Abreve', 'Aogonek', 'Cacute', 'Ccircumflex', 'Cdotaccent', 'Ccaron', 'Dcaron', 'Dcroat', 'Emacron', 'Ebreve', 'Edotaccent', 'Eogonek', 'Ecaron', 'Gcircumflex', 'Gbreve', 'Gdotaccent', 'Gcommaaccent', 'Hcircumflex', 'Hbar', 'Itilde', 'Imacron', 'Ibreve', 'Iogonek', 'Idotaccent', 'IJ', 'Jcircumflex', 'Kcommaaccent', 'Lacute', 'Lcommaaccent', 'Lcaron', 'Ldot', 'Lslash', 'Nacute', 'Ncommaaccent', 'Ncaron', 'Eng', 'Omacron', 'Obreve', 'Ohungarumlaut', 'OE', 'Racute', 'Rcommaaccent', 'Rcaron', 'Sacute', 'Scircumflex', 'Scedilla', 'Scaron', 'Tcedilla', 'Tcaron', 'Tbar', 'Utilde', 'Umacron', 'Ubreve', 'Uring', 'Uhungarumlaut', 'Uogonek', 'Wcircumflex', 'Ycircumflex', 'Ydieresis', 'Zacute', 'Zdotaccent', 'Zcaron', 'Ohorn', 'Uhorn', 'DZcaron', 'Dzcaron', 'IJacute', 'Jacute.loclNLD', 'LJ', 'Lj', 'NJ', 'Nj', 'Gcaron', 'Oogonek', 'Aringacute', 'AEacute', 'Oslashacute', 'Adblgrave', 'Ainvertedbreve', 'Edblgrave', 'Einvertedbreve', 'Idblgrave', 'Iinvertedbreve', 'Odblgrave', 'Oinvertedbreve', 'Rdblgrave', 'Rinvertedbreve', 'Udblgrave', 'Uinvertedbreve', 'Scommaaccent', 'Tcommaaccent', 'Odieresismacron', 'Otildemacron', 'Odotaccentmacron', 'Ymacron', 'Schwa', 'Adotbelow', 'Ahookabove', 'Acircumflexacute', 'Acircumflexgrave', 'Acircumflexhookabove', 'Acircumflextilde', 'Acircumflexdotbelow', 'Abreveacute', 'Abrevegrave', 'Abrevehookabove', 'Abrevetilde', 'Abrevedotbelow', 'Edotbelow', 'Ehookabove', 'Etilde', 'Ecircumflexacute', 'Ecircumflexgrave', 'Ecircumflexhookabove', 'Ecircumflextilde', 'Ecircumflexdotbelow', 'Ihookabove', 'Idotbelow', 'Odotbelow', 'Ohookabove', 'Ocircumflexacute', 'Ocircumflexgrave', 'Ocircumflexhookabove', 'Ocircumflextilde', 'Ocircumflexdotbelow', 'Ohornacute', 'Ohorngrave', 'Ohornhookabove', 'Ohorntilde', 'Ohorndotbelow', 'Udotbelow', 'Uhookabove', 'Uhornacute', 'Uhorngrave', 'Uhornhookabove', 'Uhorntilde', 'Uhorndotbelow', 'Ygrave', 'Ydotbelow', 'Yhookabove', 'Ytilde', 'Wgrave', 'Wacute', 'Wdieresis', 'diagonalbarO', 'engtail', 'horizontalbarH', 'grave.case', 'acute.case', 'dieresis.case', 'macron.case', 'cedilla.case', 'circumflex.case', 'caron.case', 'breve.case', 'dotaccent.case', 'ring.case', 'ogonek.case', 'tilde.case', 'hungarumlaut.case', 'hookabove.case', 'breveinverted.case', 'dblgrave.case', 'horn.case', 'dotbelow.case', 'dieresisbelow.case', 'commaaccent.case', 'brevebelow.case', 'macronbelow.case', 'gravecomb.case', 'acutecomb.case', 'dieresiscomb.case', 'macroncomb.case', 'cedillacomb.case', 'circumflexcomb.case', 'caroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'ringcomb.case', 'ogonekcomb.case', 'tildecomb.case', 'hungarumlautcomb.case', 'hookabovecomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'gravecombstack.case', 'acutecombstack.case', 'dieresiscombstack.case', 'macroncombstack.case', 'circumflexcombstack.case', 'brevecombstack.case', 'dotaccentcombstack.case', 'tildecombstack.case', 'hookabovecombstack.case', 'grave-stack.case', 'acute-stack.case', 'dieresis-stack.case', 'macron-stack.case', 'circumflex-stack.case', 'caron-stack.case', 'breve-stack.case', 'dotaccent-stack.case', 'ring-stack.case', 'tilde-stack.case', 'hungarumlaut-stack.case', 'hook-stack.case', 'breveinverted-stack.case', 'dblgrave-stack.case', 'gravecomb-stack.case', 'acutecomb-stack.case', 'dieresiscomb-stack.case', 'macroncomb-stack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case', 'brevecomb-stack.case', 'dotaccentcomb-stack.case', 'ringcomb-stack.case', 'tildecomb-stack.case', 'hungarumlautcomb-stack.case', 'hookcomb-stack.case', 'breveinvertedcomb-stack.case', 'dblgravecomb-stack.case', 'Alpha', 'Alphatonos', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Epsilontonos', 'Zeta', 'Eta', 'Etatonos', 'Theta', 'Iota', 'Iotatonos', 'Iotadieresis', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Omicrontonos', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Upsilontonos', 'Upsilondieresis', 'Phi', 'Chi', 'Psi', 'Omega', 'Omegatonos', 'Kaisymbol', 'ohm', 'tonos.case', 'dieresistonos.case', 'tonoscomb.case', 'dieresistonoscomb.case', 'Dje', 'Ieukran', 'Dze', 'Iukran', 'Yi', 'Je', 'Lje', 'Nje', 'Tshe', 'Dzhe', 'Acyr', 'Abrevecyr', 'Adieresiscyr', 'Be', 'Ve', 'Ghe', 'Gje', 'De', 'Ie', 'Io', 'Iebrevecyr', 'Zhe', 'Zhebrevecyr', 'Zhedieresiscyr', 'Ze', 'Icyr', 'Igravecyr', 'Ishort', 'Ka', 'Kje', 'El', 'Em', 'En', 'Ocyr', 'Odieresiscyr', 'Pe', 'Er', 'Es', 'Te', 'Ucyr', 'Ushort', 'Umacroncyr', 'Udieresiscyr', 'Uhungarumlautcyr', 'Ef', 'Ha', 'Tse', 'Che', 'Sha', 'Shcha', 'Hard', 'Yeru', 'Soft', 'Ecyr', 'Yu', 'Ya', 'Gheup', 'Ghestroke', 'Zhedescender', 'Zedescendercyr', 'Kadescender', 'Kaverticalstrokecyr', 'Kabashkircyr', 'Endescender', 'Esdescendercyr', 'Tedescender-cy', 'Ustraight', 'Ustraightstroke', 'Hadescender', 'Chedescender-cy', 'Cheverticalstroke-cy', 'Shha', 'Palochka', 'Schwacyr', 'Obarcyr', 'Hastroke-cy', 'De.bgr', 'Zhe.bgr', 'Ka.bgr', 'El.bgr', 'Amacroncyr', 'Iemacroncyr', 'Omacroncyr', 'Obrevecyr', 'Emacroncyr', 'Ebrevecyr', 'Yamacron', 'Yumacron', 'breve.cyr.case', 'Yi-dieresis.case', 'Cy-descender.case', 'breve.cyrcomb.case', 'Yi-dieresiscomb.case', 'Cy-descendercomb.case', 'U-stroke', 'Obarcyr-stroke', 'Hacyr-stroke', 'Yu-dash.case', ]

YTAS = [ 'b', 'd', 'f', 'h', 'k', 'l', 'germandbls', 'eth', 'thorn', 'dcroat', 'hcircumflex', 'hbar', 'lacute', 'beta', 'delta', 'zeta', 'theta', 'lambda', 'xi', 'phi', 'psi', 'be', 'dje', 'tshe', 'gheup', 've.bgr', 'zhe.bgr', 'be.locl', ]

YTDE = [ 'g', 'j', 'p', 'q', 'y', 'jdotless', 'thorn', 'engtail', 'beta', 'gamma', 'zeta', 'eta', 'mu', 'xi', 'rho', 'finalsigma', 'phi', 'chi', 'psi', 'kaisymbol', 'Dzhe', 'De', 'Tse', 'de', 'tse', 'dzhe', 'ustraight', 'De.bgr', 'ze.bgr','cy-descendercomb', ]

YTOS = ['C', 'G', 'J', 'O', 'Q', 'S', 'U', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'Germandbls', 'germandbls', 'question', 'at', 'ae', 'eth', 'OE', 'oe', 'thorn', 'dollar', 'sterling', 'Euro', 'lira', 'numero', 'florin', 'coloncurrency', 'uni20B2', 'uni20B5', 'hryvnia', 'dollar.rvrn', 'coloncurrency.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'two', 'three', 'five', 'six', 'eight', 'nine', 'zero.prop', 'two.prop', 'three.prop', 'five.prop', 'six.prop', 'eight.prop', 'nine.prop', 'ordfemenine', 'ordmasculine', 'ampersand', 'questiondown', 'question', 'zerosuperior', 'onesuperior', 'twosuperior', 'threesuperior', 'foursuperior', 'Schwa', 'schwa', 'Theta', 'Omega', 'alpha', 'beta', 'delta', 'epsilon', 'eta', 'theta', 'iota', 'lambda', 'mu', 'pi', 'rho', 'finalsigma', 'sigma', 'tau', 'upsilon', 'phi', 'psi', 'omega', 'Ieukran', 'Lje', 'Ze', 'El', 'Ucyr', 'Ecyr', 'be', 'ze', 'el', 'ecyr', 'ieukran', 'lje', 've.bgr', 'ghe.bgr', 'ze.bgr', 'sha.bgr', 'hard.bgr', 'soft.bgr', 'be.locl', ]

XTTW = YTTL = [ 'A', 'M', 'N', 'V', 'W', 'Y', 'v', 'w', 'y' ]

STLI = STLO = [ 'a', 'b', 'c', 'd', 'e', 'g', 'h', 'm', 'n', 'o', 'p', 'q', 's', 'u', 'ae', 'eth', 'thorn', 'oe', 'schwa', 'alpha', 'beta', 'delta', 'epsilon', 'eta', 'theta', 'rho', 'finalsigma', 'sigma', 'upsilon', 'phi', 'psi', 'omega', 'be', 'ze', 'che', 'ecyr', 'ya', 'ieukran', 'lje', 'nje', 'cheverticalstroke-cy', 've.bgr', 'ghe.bgr', 'ze.bgr', 'sha.bgr', 'hard.bgr', 'soft.bgr', 'be.locl', ]

STUI = STUO = [ 'B', 'C', 'D', 'G', 'J', 'O', 'P', 'R', 'Q', 'S', 'U', 'dollar', 'sterling', 'Euro', 'lira', 'peseta', 'dong', 'rupeeIndian', 'liraTurkish', 'manat', 'ruble', 'numero', 'coloncurrency', 'uni20B1', 'uni20B2', 'uni20B5', 'hryvnia', 'dollar.rvrn', 'cent.rvrn', 'coloncurrency.rvrn', 'uni20B1.rvrn', 'uni20B2.rvrn', 'uni20B5.rvrn', 'hryvnia.rvrn', 'zero', 'two', 'three', 'five', 'six', 'eight', 'nine', 'zero.prop', 'two.prop', 'three.prop', 'five.prop', 'six.prop', 'eight.prop', 'nine.prop', 'cent', 'currency', 'ordfeminine', 'ordmasculine', 'ampersand', 'questiondown', 'question', 'zerosuperior', 'twosuperior', 'threesuperior', 'Thorn', 'OE', 'Schwa', 'Theta', 'Phi', 'Psi', 'Omega', 'Dje', 'Ieukran', 'Lje', 'Nje', 'Tshe', 'Be', 'Ze', 'Che', 'Hard', 'Soft', 'Ecyr', 'Ya', 'Cheverticalstroke-cy', 'Shha', ]

XTUD = [ 'A', 'I', 'K', 'M', 'N', 'V', 'W', 'j', 'Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis', 'Aring', 'AE', 'Ntilde', 'Amacron', 'Abreve', 'Aogonek', 'Kcommaaccent', 'Nacute', 'Ncommaaccent', 'Ncaron', 'Eng', 'Wcircumflex', 'Nj', 'Aringacute', 'AEacute', 'Adblgrave', 'Ainvertedbreve', 'Adotbelow', 'Ahookabove', 'Acircumflexacute', 'Acircumflexgrave', 'Acircumflexhookabove', 'Acircumflextilde', 'Acircumflexdotbelow', 'Abreveacute', 'Abrevegrave', 'Abrevehookabove', 'Abrevetilde', 'Abrevedotbelow', 'Wgrave', 'Wacute', 'Wdieresis', 'jdotless', 'diagonalbarO', 'idot', 'engtail', 'hookabovecomb-stack', 'caroncomb.alt', 'diagonalbarl', 'Alpha', 'Alphatonos', 'Kappa', 'Mu', 'Nu', 'tonoscomb.case', 'Acyr', 'Abrevecyr', 'Adieresiscyr', 'Kje', 'Em', 'Ka.bgr', 'breve.cyrcomb.case', 'naira', 'won', 'naira.rvrn', 'won.rvrn', 'numero', 'A.ital', 'I.ital', 'K.ital', 'M.ital', 'N.ital', 'V.ital', 'W.ital', 'gravecomb.case', 'acutecomb.case', 'dieresiscomb.case', 'macroncomb.case', 'cedillacomb.case', 'circumflexcomb.case', 'caroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'ringcomb.case', 'ogonekcomb.case', 'tildecomb.case', 'hungarumlautcomb.case', 'hookabovecomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'gravecombstack.case', 'acutecombstack.case', 'dieresiscombstack.case', 'macroncombstack.case', 'circumflexcombstack.case', 'brevecombstack.case', 'dotaccentcombstack.case', 'tildecombstack.case', 'hookabovecombstack.case', 'grave-stack.case', 'acute-stack.case', 'dieresis-stack.case', 'macron-stack.case', 'circumflex-stack.case', 'caron-stack.case', 'breve-stack.case', 'dotaccent-stack.case', 'ring-stack.case', 'tilde-stack.case', 'hungarumlaut-stack.case', 'hook-stack.case', 'breveinverted-stack.case', 'dblgrave-stack.case', 'gravecomb-stack.case', 'acutecomb-stack.case', 'dieresiscomb-stack.case', 'macroncomb-stack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case', 'brevecomb-stack.case', 'dotaccentcomb-stack.case', 'ringcomb-stack.case', 'tildecomb-stack.case', 'hungarumlautcomb-stack.case', 'hookcomb-stack.case', 'breveinvertedcomb-stack.case', 'dblgravecomb-stack.case', 'grave.case', 'acute.case', 'dieresis.case', 'macron.case', 'cedilla.case', 'circumflex.case', 'caron.case', 'breve.case', 'dotaccent.case', 'ring.case', 'ogonek.case', 'tilde.case', 'hungarumlaut.case', 'hookabove.case', 'breveinverted.case', 'dblgrave.case', 'horn.case', 'dotbelow.case', 'dieresisbelow.case', 'commaaccent.case', 'brevebelow.case', 'macronbelow.case', ]

XTUR = [ 'C', 'G', 'I', 'O', 'Q', 'S', 'Ccedilla', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde', 'Odieresis', 'Oslash', 'Cacute', 'Ccircumflex', 'Cdotaccent', 'Ccaron', 'Gcircumflex', 'Gbreve', 'Gdotaccent', 'Gcommaaccent', 'Omacron', 'Obreve', 'Ohungarumlaut', 'OE', 'Sacute', 'Scircumflex', 'Scedilla', 'Scaron', 'Ohorn', 'Gcaron', 'Oogonek', 'Oslashacute', 'Odblgrave', 'Oinvertedbreve', 'Scommaaccent', 'Odieresismacron', 'Otildemacron', 'Odotaccentmacron', 'Odotbelow', 'Ohookabove', 'Ocircumflexacute', 'Ocircumflexgrave', 'Ocircumflexhookabove', 'Ocircumflextilde', 'Ocircumflexdotbelow', 'Ohornacute', 'Ohorngrave', 'Ohornhookabove', 'Ohorntilde', 'Ohorndotbelow', 'diagonalbarO', 'Omicron', 'Omicrontonos', 'tonoscomb.case', 'Dze', 'Ocyr', 'Odieresiscyr', 'Es', 'Yu', 'Esdescendercyr', 'Obarcyr', 'Obarcyr-stroke', 'Yu-dash.case', 'gravecomb.case', 'acutecomb.case', 'dieresiscomb.case', 'macroncomb.case', 'cedillacomb.case', 'circumflexcomb.case', 'caroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'ringcomb.case', 'ogonekcomb.case', 'tildecomb.case', 'hungarumlautcomb.case', 'hookabovecomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'gravecombstack.case', 'acutecombstack.case', 'dieresiscombstack.case', 'macroncombstack.case', 'circumflexcombstack.case', 'brevecombstack.case', 'dotaccentcombstack.case', 'tildecombstack.case', 'hookabovecombstack.case', 'grave-stack.case', 'acute-stack.case', 'dieresis-stack.case', 'macron-stack.case', 'circumflex-stack.case', 'caron-stack.case', 'breve-stack.case', 'dotaccent-stack.case', 'ring-stack.case', 'tilde-stack.case', 'hungarumlaut-stack.case', 'hook-stack.case', 'breveinverted-stack.case', 'dblgrave-stack.case', 'gravecomb-stack.case', 'acutecomb-stack.case', 'dieresiscomb-stack.case', 'macroncomb-stack.case', 'circumflexcomb-stack.case', 'caroncomb-stack.case', 'brevecomb-stack.case', 'dotaccentcomb-stack.case', 'ringcomb-stack.case', 'tildecomb-stack.case', 'hungarumlautcomb-stack.case', 'hookcomb-stack.case', 'breveinvertedcomb-stack.case', 'dblgravecomb-stack.case', 'grave.case', 'acute.case', 'dieresis.case', 'macron.case', 'cedilla.case', 'circumflex.case', 'caron.case', 'breve.case', 'dotaccent.case', 'ring.case', 'ogonek.case', 'tilde.case', 'hungarumlaut.case', 'hookabove.case', 'breveinverted.case', 'dblgrave.case', 'horn.case', 'dotbelow.case', 'dieresisbelow.case', 'commaaccent.case', 'brevebelow.case', 'macronbelow.case', 'C.ital', 'G.ital', 'I.ital', 'O.ital', 'Q.ital', 'S.ital', ]

def makeGlyphs(src_font, dst_font, glyphs, in_set):

    src_fontName = SRC_PATH + src_font
    src_font = OpenFont(src_fontName, showInterface=False)
    
    dst_fontName = DST_PATH + dst_font
    dst_font = OpenFont(dst_fontName, showInterface=False)
    
    if in_set:
    
        for glyph in glyphs:
            
            dst_font[glyph] = src_font[glyph]
    
    else:
        
        for glyph in src_font:
            
            if glyph.name not in glyphs:
                
                dst_font[glyph.name] = src_font[glyph.name]
                
            
    dst_font.save()
    print('Propagated glyphs at ' + dst_fontName)


# # # XOPQs
# makeGlyphs('RobotoAvar2-XOPQ2.ufo', 'RobotoAvar2-XOFI2.ufo', XOFI, True)
# makeGlyphs('RobotoAvar2-XOPQ310.ufo', 'RobotoAvar2-XOFI300.ufo', XOFI, True)
# makeGlyphs('RobotoAvar2-XOPQ2.ufo', 'RobotoAvar2-XOLC2.ufo', XOLC, True)
# makeGlyphs('RobotoAvar2-XOPQ310.ufo', 'RobotoAvar2-XOLC294.ufo', XOLC, True)
# makeGlyphs('RobotoAvar2-XOPQ2.ufo', 'RobotoAvar2-XOUC2.ufo', XOUC, True)
# makeGlyphs('RobotoAvar2-XOPQ310.ufo', 'RobotoAvar2-XOUC310.ufo', XOUC, True)

# # # XTRAs
# makeGlyphs('RobotoAvar2-XTRA244.ufo', 'RobotoAvar2-XTFI244.ufo', XTFI, True)
# makeGlyphs('RobotoAvar2-XTRA741.ufo', 'RobotoAvar2-XTFI741.ufo', XTFI, True)
# makeGlyphs('RobotoAvar2-XTRA244.ufo', 'RobotoAvar2-XTLC244.ufo', XTLC, True)
# makeGlyphs('RobotoAvar2-XTRA741.ufo', 'RobotoAvar2-XTLC741.ufo', XTLC, True)
# makeGlyphs('RobotoAvar2-XTRA244.ufo', 'RobotoAvar2-XTUC244.ufo', XTUC, True)
# makeGlyphs('RobotoAvar2-XTRA741.ufo', 'RobotoAvar2-XTUC741.ufo', XTUC, True)

# # # YTAS
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTAS665.ufo', YTAS, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTAS875.ufo', YTAS, False)

# # # YTDE
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTDE-100.ufo', YTDE, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTDE-310.ufo', YTDE, False)

# # # YTFI
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTFI270.ufo', YTFI, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTFI793.ufo', YTFI, False)

# # # YTLC
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTLC426.ufo', YTLC, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTLC584.ufo', YTLC, False)

# # # YTUC
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTUC528.ufo', YTUC, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTUC778.ufo', YTUC, False)

# # # YTOS
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTOS0.ufo', YTOS, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTOS50.ufo', YTOS, False)

# # # XTTW
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-XTTW0.ufo', XTTW, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-XTTW30.ufo', XTTW, False)

# # # YTTL
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTTL0.ufo', YTTL, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-YTTL50.ufo', YTTL, False)

# # # STLI
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STLI2.ufo', STLI, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STLI412.ufo', STLI, False)

# # # STLO
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STLO2.ufo', STLO, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STLO426.ufo', STLO, False)

# # # STUI
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STUI2.ufo', STUI, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STUI736.ufo', STUI, False)

# # # STUO
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STUO2.ufo', STUO, False)
# makeGlyphs('RobotoAvar2-wght400.ufo', 'RobotoAvar2-STUO722.ufo', STUO, False)

# # # XTUD
# makeGlyphs('RobotoAvar2-XTRA741.ufo', 'RobotoAvar2-XTUD741.ufo', XTUD, True)

# # # XTUR
# makeGlyphs('RobotoAvar2-XTRA741.ufo', 'RobotoAvar2-XTUR741.ufo', XTUR, True)


