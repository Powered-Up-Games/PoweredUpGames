# create web site

from yattag import Doc as html
from yattag import indent
from wand.image import Image as image
from wand.color import Color as color

sizes = [64, 128, 256, 512, 1024]

document, tag, text = html(stag_end='>').tagtext()

document.asis('<!DOCTYPE html>')
with tag('html'):
	with tag('head'):
		document.stag('meta', name='viewport', content='width=device-width, initial-scale=1')
		with tag('title'):
			text('Powered Up Games')
		with tag('style'):
			document.asis('img {width: 25%;}')
	with tag('body'):
		with tag('div', id='logo'):
			with tag('picture'):
				for size in sizes:
					document.stag('source', srcset=f'images/logo-{size}.webp', media=f'(max-width: {size}px)')
				document.stag('img', src='images/logo-1024.webp', alt='Powered Up Games Logo')
			with tag('p'):
				text('Powered Up Games')
		with tag('p'):
			text('Powered Up Games provides professional game development services.')
		with tag('h2'):
			text('Platforms')
		with tag('picture'):
			document.stag('img', src='images/platforms/switch.jpg', alt='Nintendo Switch')

with open('html/index.html', 'w') as file:
	file.write(indent(document.getvalue()))


for size in sizes:
	with image(filename='images/logo.webp') as img:
		img.resize(size, size)
		img.background_color = color('white')
		img.alpha_channel = 'remove'
		img.save(filename=f'html/images/logo-{size}.webp')


