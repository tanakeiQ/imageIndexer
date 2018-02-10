#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ### ImageIndexer
#
# This script required below libraries.
#
# - ImageMagick
# - ghostscript(For AI, EPS, PDF)
#
# Created by tanakeiQ<tanakei@suitehearts.co>

import os
import sys
import uuid
import atexit
import json
import hashlib
import re
import apimodels
from log import *
from distutils.spawn import find_executable
from time import time
from joblib import Parallel, delayed

# meta resources
filemap = []
global timer

# ImageMagick
image_magick_path = find_executable('convert')

# Target resources
# image resources directory
input_dir = '%s/debug/resources/' % (os.getcwd())
# output file extension(don't forget dor(.))
output_ext = 'png'
# output thumbnail directory
output_thumb_dir = '%s/debug/output/thumb' % (os.getcwd())
# If applied script into symbolic link, set `True`
isEnableSym = False
# Is customize script, modify avairable file format.
avairable_formats = ['ai', 'eps', 'psd', 'png',
                     'jpg', 'jpeg', 'bmp', 'ico', 'ttf', 'pdf']

ignorefiles = [r'^\..*']

# Convert General Image
# thumbnail width
width = 300
# thumbnail height
height = 300
# thumbnail quality
quality = 80
# thumbnail density
density = 300

cmd_common_output = ' "%s/%s"'
cmd_common = '%s "%s" -resize %dx%d -quality %d %s'

# Convert Extension for Layer Image
cmd_layer = '%s "%s[0]" -density %d -resize %dx%d -quality %d -colorspace CMYK %s'

# Convert Extension for Font
font_pointsize = 100
font_label = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
これはひらがな
コレハカタカナ
此れは漢字'''
cmd_font = '%s -font "%s" -pointsize %s label:"%s" -resize %dx%d -quality %d %s'

# Route Map Settings
routeMapDepth = 10


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def close():
    logger.info('🌟  ---- END ----')
    logger.info(time() - timer)
    apimodels.close()


def convert(path, filename):
    cmd = ''
    name, ext = os.path.splitext(filename)
    ext = ext.lstrip('.')

    output_filename = "%s_%s.%s" % (uuid.uuid4(), name, output_ext)
    output = cmd_common_output % (output_thumb_dir, output_filename)

    if ext in {'psd', 'ico', 'ai', 'eps'}:
        cmd = cmd_layer % (image_magick_path, path, density,
                           width, height, quality, output)
    elif ext in {'pdf'}:
        cmd = cmd_layer % (image_magick_path, path, density,
                           width, height, quality, output)
    elif ext in {'ttf'}:
        cmd = cmd_font % (image_magick_path, path, font_pointsize,
                          font_label, width, height, quality, output)
    else:
        cmd = cmd_common % (image_magick_path, path,
                            width, height, quality, output)
    try:
        # logger.info(cmd)
        os.system(cmd)
        # Filename, File path, Extension, Thumbnail path, File size, width,
        # height
        data = {
            "uid": md5(path),
            "name": name,
            "ext": ext,
            "path": path,
            "thumbnail": output_filename,
            "size": os.path.getsize(path),
            "width": 0,
            "height": 0
        }
        apimodels.createIndex(data)
        logger.info('✅  INSERTED: %s' % (path))
    except:
        logger.warning('❌  Filed to convert: %s \n%s' %
                       (path, sys.exc_info()[1]))


def rSearch(path):
    filenames = os.listdir(path)
    print(filenames)
    for filename in filenames:
        ignored = False
        for pattern in ignorefiles:
            if re.match(pattern, filename):
                logger.info('🛳  Ignored file: %s' % (filename))
                ignored = True
                break
        if ignored:
            continue
        fullpath = os.path.join(path, filename)
        if os.path.islink(fullpath):
            if isEnableSym:
                rSearch(fullpath)
            else:
                logger.info('🔗  Sym link is ignored: %s' % (fullpath))
        elif os.path.isdir(fullpath):
            logger.info('🌳  mapping Directory: %s' % (fullpath))
            apimodels.createRoute(input_dir, fullpath)
            rSearch(fullpath)
        elif os.path.isfile(fullpath):
            name, ext = os.path.splitext(filename)
            ext = ext.lstrip('.')
            if not ext in avairable_formats:
                logger.info('💦  file extension `%s` is not support: %s' %
                            (ext, fullpath))
                break
            filemap.append({
                "filepath": fullpath,
                "filename": filename
            })
        else:
            logger.info('💦  This file format not support: %s' % (fullpath))
    return True


if __name__ == '__main__':
    if not image_magick_path:
        logger.warning('''
	❌  ImageMagick not installed
	❌  Please install before. 
	❌  
	❌  https://www.imagemagick.org/script/download.php

''')
    else:
        if not os.path.exists(output_thumb_dir):
            os.makedirs(output_thumb_dir)
        if not os.path.exists(input_dir):
            logger.warning('❌  No such directory: %s')
        logger.info('Use convert<%s>' % (image_magick_path))
        logger.info('🌤  ---- START ----')
        # Adjsut input_directory path
        input_dir += '/'
        timer = time()
        atexit.register(close)
        apimodels.initIndex()
        apimodels.initRoutes(routeMapDepth)
        rSearch(input_dir)
        logger.info('--- file count = %s' % (len(filemap)))
        Parallel(n_jobs=-1)([delayed(convert)(filemap[idx]['filepath'],
                                              filemap[idx]['filename']) for idx in range(len(filemap))])
