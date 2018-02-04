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

import os, sys, uuid, csv, atexit
from distutils.spawn import find_executable

# meta resources
filemap=[]

# ImageMagick
image_magick_path=find_executable('convert')

# Target resources
# image resources directory
input_dir='%s/resources' % (os.getcwd())
# output file extension(don't forget dor(.))
output_ext='png'
# output thumbnail directory
output_thumb_dir='%s/output/thumb' % (os.getcwd())
# ouput csv directory
output_csv_path='%s/output/_map.csv' % (os.getcwd())
# If applied script into symbolic link, set `True`
isEnableSym=False
# Is customize script, modify avairable file format.
avairable_formats=['ai','eps','psd','png','jpg','jpeg','bmp','ico','ttf','pdf']

### Convert General Image
# thumbnail width
width=300
# thumbnail height
height=300
# thumbnail quality
quality=80
# thumbnail density
density=300

cmd_common_output=' "%s/%s"'
cmd_common='%s "%s" -resize %dx%d -quality %d %s'

# Convert Extension for Layer Image
cmd_layer='%s "%s[0]" -density %d -resize %dx%d -quality %d -colorspace CMYK %s'

# Convert Extension for Font
font_pointsize=100
font_label='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
これはひらがな
コレハカタカナ
此れは漢字'''
cmd_font='%s -font "%s" -pointsize %s label:"%s" -resize %dx%d -quality %d %s'


def writeCsv():
	with open(output_csv_path, 'w') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerows(filemap)

def convert(path, filename):
	cmd=''
	name, ext = os.path.splitext(filename)
	ext = ext.lstrip('.')
	if not ext in avairable_formats:
		print('💦  file extension `%s` is not support: %s' % (ext, path))
		return

	output_filename="%s_%s.%s" % (uuid.uuid4(), name, output_ext)
	output=cmd_common_output % (output_thumb_dir, output_filename)

	if ext in {'psd', 'ico', 'ai', 'eps'}:
		cmd = cmd_layer % (image_magick_path, path, density, width, height, quality, output)
	elif ext in {'pdf'}:
		cmd = cmd_layer % (image_magick_path, path, density, width, height, quality, output)
	elif ext in {'ttf'}:
		cmd = cmd_font % (image_magick_path, path, font_pointsize, font_label, width, height, quality, output)
	else:
		cmd = cmd_common % (image_magick_path, path, width, height, quality, output)
	try:
		# print(cmd)
		os.system(cmd)
		# Filename, File path, Extension, Thumbnail path, File size, width, height
		data=[name, ext, path, output_filename,os.path.getsize(path), 0, 0]
		filemap.append(data)
	except:	
		print('❌  Filed to convert: %s' % (path))


def rSearch(path):
	filenames = os.listdir(path)
	for filename in filenames:
		fullpath = os.path.join(path, filename)
		if os.path.islink(fullpath):
			if isEnableSym:
				rSearch(fullpath)
			else:
				print('🔗  Sym link is ignored: %s' % (fullpath))
		elif os.path.isdir(fullpath):
			rSearch(fullpath)
		elif os.path.isfile(fullpath):
			convert(fullpath, filename)
		else:
			print('💦  This file format not support: %s' % (fullpath))	


if __name__ == '__main__':
	if not image_magick_path:
		sys.stderr.write('''
	❌  ImageMagick not installed
	❌  Please install before. 
	❌  
	❌  https://www.imagemagick.org/script/download.php

''')
	else:
		if not os.path.exists(output_thumb_dir):
			os.makedirs(output_thumb_dir)
		if not os.path.exists(input_dir):
			sys.stderr.write('❌  No such directory: %s')
		print('Use convert<%s>' % (image_magick_path))
		atexit.register(writeCsv)
		rSearch(input_dir)