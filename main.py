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
import ast
import configparser
import apimodels
from log import *
from distutils.spawn import find_executable
from time import time
from joblib import Parallel, delayed
from multiprocessing import Value

share_count = Value('i', 1)

# meta resources
filemap = []
filecount = 0
global timer
config = configparser.ConfigParser()
config.read('config/batch.ini')

# ImageMagick
image_magick_path = find_executable('convert')

# Target resources
# image resources directory
input_dir = config['batch']['input_dir']
# input_dir = '%s/debug/resources/' % (os.getcwd())
# output file extension(don't forget dor(.))
output_ext = config['batch']['output_ext']
# output thumbnail directory
output_thumb_dir = config['batch']['output_thumb_dir']
# If applied script into symbolic link, set `True`
isEnableSym = config['batch'].getboolean('isEnableSym')
# Is customize script, modify avairable file format.
avairable_formats = ast.literal_eval(config['batch']['avairable_formats'])

ignorefiles = [r'^\..*']

# Convert General Image
# thumbnail width
width = config['batch'].getint('width')
# thumbnail height
height = config['batch'].getint('height')
# thumbnail quality
quality = config['batch'].getint('quality')
# thumbnail density
density = config['batch'].getint('density')

cmd_common_output = ' "%s/%s"'
cmd_common = '%s "%s" -resize %dx%d -quality %d %s'

# Convert Extension for Layer Image
cmd_layer = '%s "%s[0]" -density %d -resize %dx%d -quality %d -colorspace CMYK %s'

# Convert Extension for Font
font_pointsize = config['batch'].getint('font_pointsize')
font_label = config['batch']['font_label']
cmd_font = '%s -font "%s" -pointsize %s label:"%s" -resize %dx%d -quality %d %s'

# Route Map Settings
routeMapDepth = config['batch'].getint('routeMapDepth')


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
            "path": path.replace(input_dir, ''),
            "thumbnail": output_filename,
            "size": os.path.getsize(path),
            "width": 0,
            "height": 0
        }
        apimodels.createIndex(data)
        logger.info('✅  (%d/%d) INSERTED: %s' %
                    (share_count.value, filecount, path))
        share_count.value += 1
    except:
        logger.warning('❌  Filed to convert: %s \n%s' %
                       (path, sys.exc_info()[1]))


def rSearch(path):
    filenames = os.listdir(path)
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
        apimodels.initRouteIndexes()
        rSearch(input_dir)
        filecount = len(filemap)
        logger.info('--- file count = %s' % (filecount))
        Parallel(n_jobs=-1)([
            delayed(convert)(
                filemap[idx]['filepath'],
                filemap[idx]['filename']
            ) for idx in range(len(filemap))
        ])
