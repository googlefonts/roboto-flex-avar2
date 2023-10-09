Roboto Flex avar2
=================


Contents
--------

```
├── fonts/
│   └── *.ttf
├── scripts/
│   └── *.py
└── sources/
    ├── *.ufo
    ├── RobotoFlex.designspace
    ├── RobotoFlex.roboFontSets
    └── measurements.json
```


Parametric axes
---------------

- [x] `slnt` slant
- [x] `GRAD` Grade
- [x] `SPAC` Spacing
- [x] `XOPQ` General x opaque
- [ ] `XOUC` X stem uppercase
- [ ] `XOLC` x stem lowercase
- [ ] `XOFI` X stem figures
- [x] `XTRA` General x transparent
- [ ] `XTUC` x transparent uppercase
- [ ] `XTLC` x transparent lowercase
- [ ] `XTFI` x transparent figures
- [ ] `XTAB` Figure width
- [ ] `XTSP` General x sidebearing
- [ ] `XUCS` x sidebearing uppercase H
- [ ] `XUCR` x sidebearing uppercase O
- [ ] `XLCS` x sidebearing lowercase n
- [ ] `XLCR` x sidebearing lowercase o
- [ ] `XFIR` x sidebearing figure 0
- [x] `YOPQ` General y opaque
- [ ] `YOUC` Y opaque uppercase
- [ ] `YOLC` y opaque lowercase
- [ ] `YOFI` y opaque figures
- [ ] `YTRA` y transparent
- [x] `YTUC` y transparent uppercase
- [x] `YTLC` y transparent lowercase
- [x] `YTFI` y transparent figures
- [x] `YTAS` y transparent ascender 
- [x] `YTDE` y transparent descender
- [ ] `YTOS` General y overshoot
- [ ] `YTUO` y uppercase overshoot
- [ ] `YTLO` y lowercase overshoot
- [ ] `YTFO` y figures overshoot
- [ ] `YTDO` y descender overshoot
- [ ] `YTAO` y ascender overshoot
- [ ] `XOAC` Accents main weight
- [ ] `YOAC` Accents secondary weight
- [ ] `YTUA` Uppercase accent base
- [ ] `YTLA` Lowercase accent base
- [ ] `YUAT` Uppercase accent height
- [ ] `YLAT` Lowercase accent height
- [ ] `XTSP` 
- [ ] `UDLN` underline top
- [ ] `YTTL` trap length
- [ ] `XTTW` trap width


Blended axes
------------

- [x] `wght` Weight
- [x] `wdth` Width
- [x] `opsz` Optical Size


Documents
---------

- [avar2 > Simplified controls for parametric fonts without redundant data](http://github.com/harfbuzz/boring-expansion-spec/blob/main/avar2.md#3-simplified-controls-for-parametric-fonts-without-redundant-data)
- [avar2 in designspace > Parametric use case](https://github.com/harfbuzz/boring-expansion-spec/blob/main/avar2-in-designspace.md#parametric-use-case)


Implementation example
----------------------

- [behdad/generate-avar2](http://github.com/behdad/generate-avar2)


Tools
-----

- [VariableValues](http://github.com/gferreira/fb-variable-values)
