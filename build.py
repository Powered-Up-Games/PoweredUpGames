# create web site

import os
from yattag import Doc as html
from yattag import indent
from wand.image import Image as image
from wand.color import Color as color
import sqlite3

connection = sqlite3.connect(':memory:')
db = connection.cursor()
db.execute('CREATE TABLE studios (name TEXT, image TEXT, url TEXT)')
db.executemany('INSERT INTO studios VALUES (?, ?, ?)', [
	('Attractive Games', 'attractive', 'https://web.archive.org/web/20080820143353/http://attractive-games.com/'),
	('Avalanche Studios', 'avalanche', 'https://web.archive.org/web/20080820143353/http://www.avalanchestudios.se/'),
	('Coyote Developments', 'coyote', 'https://web.archive.org/web/20040406063019/http://coyotedev.co.uk/'),
	('Echo Peak', 'echo-peak', 'https://web.archive.org/web/20131230132524/http://echo-peak.com/'),
	('HotGen', 'hotgen', 'https://web.archive.org/web/20160129065655/http://hotgen.com/HGWordPress/'),
	('Just Add Water', 'just-add-water', 'https://web.archive.org/web/20110120022457/http://jawltd.com/'),
	('Lionhead Studios', 'lionhead', 'https://web.archive.org/web/20060209023317/http://www.lionhead.com/'),
	('London South Bank University', 'lsbu', 'https://www.lsbu.ac.uk/'),
	('Mojo Bones', 'mojo-bones', 'https://www.mojobones.co.uk/'),
	('National Film and Television School', 'nfts', 'https://nfts.co.uk/'),
	('Oxygen Interactive Studios', 'oxygen', 'https://web.archive.org/web/20081220151826/http://www.oxygen-studios.com/'),
	('Razorback Developments', 'razorback', 'https://web.archive.org/web/20070930032952/http://www.razorback.co.uk/'),
	('Relentless Software', 'relentless', 'https://web.archive.org/web/20120630120955/http://relentless.co.uk/home/'),
	('Warp Digital', 'warp', 'https://www.warpdigital.com/'),
	('Zoe Mode', 'zoe-mode', 'https://web.archive.org/web/20130604043958/http://zoemode.com/')
])
connection.commit()

sizes = [
	64,
	128,
	256,
	512,
	1024
]

studios = db.execute('SELECT * FROM studios')

document, tag, text = html(stag_end='>').tagtext()

document.asis('<!DOCTYPE html>')
with tag('html'):
	with tag('head'):
		document.stag('meta', name='viewport', content='width=device-width, initial-scale=1')
		with tag('title'):
			text('Powered Up Games')
		with tag('style'):
			document.asis('img {width: 10%;}')
	with tag('body'):
		with tag('div', id='logo'):
			with tag('picture'):
				for size in sizes:
					document.stag('source', srcset=f'images/logo-{size}.webp', media=f'(max-width: {size}px)')
				document.stag('img', src='images/logo-1024.webp', alt='Powered Up Games Logo')
		with tag('p'):
			text('Powered Up Games provides professional game development services. We have many years experience in porting, automation, optimization, training, and debugging.')
		with tag('h2'):
			text('studios')
		for name, id, url in studios:
			with tag('picture'):
				document.stag('img', src=f'images/studios/{id}-1024.webp', alt=f'{name} Logo')

with open('html/index.html', 'w') as file:
	file.write(indent(document.getvalue()))

def render_image_sizes(name):
	for width in sizes:
		if not os.path.exists(f'html/images/{name}-{width}.webp'):
			with image(filename=f'images/{name}.webp') as img:
				height = img.height * width // img.width
				img.resize(width, height, 'lanczos')
				img.background_color = color('white')
				img.alpha_channel = 'remove'
				img.save(filename=f'html/images/{name}-{width}.webp')

studios = db.execute('SELECT * FROM studios')
for name, id, url in studios:
	render_image_sizes(f'studios/{id}')

render_image_sizes('logo')
