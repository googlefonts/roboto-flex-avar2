RobotoA2
===========

Alpha version of RobotoFlex made with avar2 data. (work in progress)


Table of contents
-----------------

- [File Size Comparison](#file-size-comparison)
- [Current folder structure](#current-folder-structure)
- [fonts](#Fonts-Folder)
  - [LGC Alpha](#lgc-alpha)
- [source](#Source-folder)
  - [Parametric avar2](#parametric-avar2)
  - [Measurements file](#measurements.json)
  - [Blends file](#blends.json)
  - [Fences file](#fences.json)
- [The designspace and variable font builder](#the-designspace-and-variable-font-builder)

File Size Comparison
------------------------

File | glyphs | file-size | bytes per glyph
--|--|--|--|
RobotoA2-avar2-VF.ttf | 1,042 | ![GitHub file size in bytes](https://img.shields.io/github/size/googlefonts/roboto-flex-avar2/fonts%2FLGCAlpha%2FRobotoA2-avar2-VF.ttf) | 476  
RobotoFlex[...].ttf | 948 | ![GitHub file size in bytes](https://img.shields.io/github/size/googlefonts/roboto-flex/fonts%2FRobotoFlex%5BGRAD%2CXOPQ%2CXTRA%2CYOPQ%2CYTAS%2CYTDE%2CYTFI%2CYTLC%2CYTUC%2Copsz%2Cslnt%2Cwdth%2Cwght%5D.ttf) | 1,885.33

1,885.3291139241/476.072 = 3.96x smaller

476.072/1,885.3291139241 = 25.25140022%

Current folder structure
------------------------

```
RobotoA2
├── docs/
├── fonts/
├── OFL.txt
├── source/
├── README.md
├── requirements.txt
├── tools/
```

<dl>
  <dt>Fonts</dt>
  <dd>This folder contains variable font binaries for testing, in subfolders for different stages of the project.</dd>
  <dt>Source</dt>
  <dd>This folder contains various source files used to design and build the variable fonts. Source files include UFO font sources, designspace files, Python scripts, as well as additional text files with data for glyph sets, glyph constructions, measurements, parametric blends, and fences.</dd>
  <dt>docs</dt>
  <dd>This folder is meant to contain font proof tests.
  </dd>
</dl>


Fonts Folder
----------------

The Fonts folder currently contains two subfolders which correspond to different development stages of the project.

```
Fonts
├── AsciiAlpha/
├── LGCAlpha/
├── TechAlpha/
```
<dl>
  <dt>AsciiAlpha</dt>
  <dd>Our second (successful) attempt at building an avar2 font, ascii only.</dd>
  <dt>LGCAlpha</dt>
  <dd>THIS contains the latest WIP fonts.</em></dd>
  <dt>TechAlpha</dt>
  <dd>Our first (failed) attempt at building an avar2 font. ⚠️ <em>These files are no longer useful and can probably be archived in a branch.</em></dd>
</dl>

### ASCII Alpha 

```
AsciiAlpha
├── RobotoA2-avar1-VF.ttf
├── RobotoA2-avar2-VF.ttf
└── RobotoA2-avar2-fences-VF.ttf
```
<dl>
  <dt>RobotoA2-Roman_avar1.ttf</dt>
  <dd>Variable font in avar1 format. Blended axes are created by instantiating their extrema from parametric axes, and inserting them into the designspace as sources.</dd>
  <dt>RobotoA2-Roman_avar2.ttf</dt>
  <dd>Variable font in avar2 format. Blended axes are created by defining mappings from parametric axes to extrema input values.</dd>
  <dt>RobotoA2-Roman_avar2_fences.ttf</dt>
  <dd>Attempt to build an avar2 font with “fences” to restrict the limits of parametric values at blended extrema locations. ⚠️ <em>The added fences work at the default location, but not at the blended extrema.</em>*</dd>
</dl>

\* see [Implementing fences](https://github.com/googlefonts/amstelvar-avar2/issues/4)

### LGC Alpha 

```
LGCAlpha
├── RobotoA2-avar2-VF.ttf
└── RobotoA2-avar2-fences-VF.ttf
```
<dl>
  <dt>RobotoA2-avar2.ttf</dt>
  <dd>Variable font in avar2 format. Blended axes are created by defining mappings from parametric axes to extrema input values, **with fencing mappings**</dd>
  <dt>RobotoA2-avar2-no-fences.ttf</dt>
  <dd>Variable font in avar2 format. Blended axes are created by defining mappings from parametric axes to extrema input values, **without fencing mappings**</dd>
</dl>


Source folder
------------------

Just like the Fonts folder, the Sources folder contains subfolders which correspond to different stages of the project:

```
Source
├── TechAlpha/
└── Parametric-avar2/
```

<dl>
  <dt>TechAlpha</dt>
  <dd>Sources in the TechAlpha folder were derived from the original RobotoFlexavar1 parametric sources. A measurements file in JSON format is included, as well as the original extrema sources in a subfolder. <em>With the exception of the `extrema` sources and the measurements file (which are used in the initial blends calculation, see below), all other files are no longer useful and can probably be archived in a branch.</em></dd>
  <dt>Parametric-avar2</dt>
  <dd>Sources in the Parametric-avar2 folder were recreated from a revised default. These are the current WIP files.</dd>
  <dt>tools</dt>
  <dd>This folder collects various small scripts which were used during development of TechAlpha and/or Parametric-avar2 sources. Most of them are no longer needed. The most relevant ones are listed below.</dd>
</dl>


### Parametric-avar2

Folder containing source files, designspace, and features.

```
Roman
├── *.ufo
├── measurements.json
├── blends.json
├── fences.json
├── features
│   └── *.fea
├── instances
│   ├── RobotoA2-opsz8.ufo
│   ├── RobotoA2-opsz144.ufo
│   ├── RobotoA2-wdth25.ufo
│   ├── RobotoA2-wdth151.ufo
│   ├── RobotoA2-wght200.ufo
│   └── RobotoA2-wght800.ufo
├── RobotoA2-avar2.designspace
└── RobotoA2-avar2-no-fences.designspace
```

<dl>
	<dt>*.ufo</dt>
	<dd>Font sources in UFO format, with files named according to their variation parameters.</dd>
	<dt>measurements.json</dt>
	<dd>Standalone JSON file containing definitions for various font- and glyph-level measurements. Created using the <a href='#'>Measurements tool</a> from the <a href='#'>VariableValues</a> extension. See <a href='http://gferreira.github.io/fb-variable-values/reference/measurements-format/'>Measurements format</a> for documentation of the data format.</dd>
	<dt>blends.json</dt>
	<dd>Standalone JSON file containing definitions of blended axes and blended sources from parametric axes. This data is used to build the avar2 designspace.</dd>
	<dt>fences.json</dt>
	<dd>Standalone JSON file containing definitions of min/max fence values for parametric values at blended sources. This data is used to add mappings for fences to the avar2 designspace (experimental).</dd>
	<dt>features</dt>
	<dd>Subfolder with files containing OpenType code which can be linked to the source fonts. <em>Currently not used when building the variable fonts.</em></dd>
	<dt>instances</dt>
	<dd>Subfolder containing instances generated from the parametric sources, which are used to add blended axes to the avar1 designspace. Also useful for comparison with the original RobotoFlex var1 sources for blended extrema.</dd>
	<dt>RobotoA2-avar2.designspace</dt>
	<dd>Designspace for building avar2 variable font. Includes avar2 mappings which define blended sources from parametric values.</dd>
	<dt>RobotoA2-avar2-no-fences.designspace</dt>
	<dd>Designspace for building avar2 variable font. Does not includes avar2 fencing mappings, so we can see the parametric axes’ full range</dd>
	<dt>Scratch folder</dt>
	<dd>Parametric axis from RobotoFlex public version.</dd>
</dl>

\* All variable fonts are built into the `Fonts/LGCAlpha` folder.

## Tools folder

A selection of production scripts which are worth mentioning:

<dl>
  <dt>glyphConstruction folder</dt>
  <dd>Contains all the glyphconstruction recipes by script</dd>
  <dt>copyGlyphsToSources.py</dt>
  <dd>Copy base glyphs from the default to the parametric sources.</dd>
  <dt>fixGlyphs.py</dt>
  <dd>Used make miscellaneous fixes needed glyphs on all the defined sources.</dd>
  <dt>getRecipe.py</dt>
  <dd>Used to get the current glyph construction recipes, without anchors.</dd>
</dl>

<dl>
  <dt><a href='http://github.com/googlefonts/roboto-flex-avar2/blob/main/Source/tools/mark-components.py'>mark-components.py</a></dt>
  <dd>Mark glyphs in the current font containing components with different colors depending on their components' nesting level.</dd>
</dl>

The designspace and variable font builder
-----------------------------------------

The different Variable Fonts are built by a single `build-RobotoAvar2.sh` shell script.

First make virtualenv.

```
virtualenv tools/robotoflexA2-env
```

Then install dependencies.

```
source tools/robotoflexA2-env/bin/activate
pip install -r requirements.txt
deactivate
```

Finally build Variable Fonts.

```
sh source/Parametric-avar2/build-RobotoAvar2.sh
```