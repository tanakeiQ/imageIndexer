![Python](https://img.shields.io/badge/Python-3.x-blue.svg "Python 3.x")
![MIT](https://img.shields.io/badge/License-MIT-green.svg "MIT License")

`imageIndexer` is index Huge Image reources and view by HTML.

We will be able to organize huge resources and live a stress-free life😼 😼


## Avairable formats
- Photoshop(.pdf)
- Illustrator(.ai, .eps)
- Jpeg(.jpg, .jpeg)
- Png(.png)
- Icon(.ico)
- PDF(.pdf)
- Bitmap(.bmp)
- True Type Font(.ttf)

## Usage

### 1. Install `ImageMagick`
https://www.imagemagick.org/script/download.php

#### ex. OSX
```bash
$ brew install imageMagick
# Check whether it is installed
$ convert -h
```

### 2. Install `gs(ghostScript)` for used PostScript resources(.psd, .pdf, .ai, .eps)
#### ex. OSX
```bash
$ brew install gs
# or brew install ghostscript
```

### 3. Set configuration
```python
# image resources directory
input_dir='%s/resources' % (os.getcwd())
# output file extension(don't forget dor(.))
output_ext='.png'
# output thumbnail directory
output_thumb_dir='%s/output' % (os.getcwd())
# If applied script into symbolic link, set `True`
isEnableSym=False
# Is customize script, modify avairable file format.
avairable_formats=['.ai','.eps','.psd','.png','.jpg','.jpeg','.bmp','.ico','.ttf','.pdf']

### Convert General Image
# thumbnail width
width=300
# thumbnail height
height=300
# thumbnail quality
quality=80
# thumbnail density
density=300

```
refs to ImageMagic docs. 
https://www.imagemagick.org/script/convert.php

### execute
```bash
$ python main.py
```

## View data on Bottle
```bash
$ pipenv run python server.py
```

# Issues
https://github.com/tanakeiQ/imageIndexer/issues

# Comment
I am bad both English and Python😢.

But I'll try my best!

# Lisence
MIT License

# Author
tanakeiQ([@tanakeiQ](https://twitter.com/tanakeiq))
