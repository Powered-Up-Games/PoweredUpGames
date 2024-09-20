# create web site

import os
from yattag import Doc as html
from yattag import indent
from wand.image import Image as image
from wand.color import Color as color
import sqlite3

connection = sqlite3.connect(':memory:')
db = connection.cursor()
db.execute('CREATE TABLE studios (id TEXT, name TEXT, url TEXT)')
db.executemany('INSERT INTO studios VALUES (?, ?, ?)', [
	('attractive', 'Attractive Games', 'https://web.archive.org/web/20080820143353/http://attractive-games.com/'),
	('avalanche', 'Avalanche Studios', 'https://web.archive.org/web/20080820143353/http://www.avalanchestudios.se/'),
	('coyote', 'Coyote Developments', 'https://web.archive.org/web/20040406063019/http://coyotedev.co.uk/'),
	('echo-peak', 'Echo Peak', 'https://web.archive.org/web/20131230132524/http://echo-peak.com/'),
	('hotgen', 'HotGen', 'https://web.archive.org/web/20160129065655/http://hotgen.com/HGWordPress/'),
	('just-add-water', 'Just Add Water', 'https://justaddwaterdevelopment.com/'),
	('lionhead', 'Lionhead Studios', 'https://web.archive.org/web/20060209023317/http://www.lionhead.com/'),
	('lsbu', 'London South Bank University', 'https://www.lsbu.ac.uk/'),
	('mojo-bones', 'Mojo Bones', 'https://www.mojobones.co.uk/'),
	('nfts', 'National Film and Television School', 'https://nfts.co.uk/'),
	('oxygen', 'Oxygen Interactive Studios', 'https://web.archive.org/web/20081220151826/http://www.oxygen-studios.com/'),
	('razorback', 'Razorback Developments', 'https://web.archive.org/web/20070930032952/http://www.razorback.co.uk/'),
	('relentless', 'Relentless Software', 'https://web.archive.org/web/20120630120955/http://relentless.co.uk/home/'),
	('warp', 'Warp Digital', 'https://www.warpdigital.com/'),
	('zoe-mode', 'Zoe Mode', 'https://web.archive.org/web/20130604043958/http://zoemode.com/')
])
db.execute('CREATE TABLE games (id TEXT, name TEXT, studio TEXT, url TEXT)')
db.executemany('INSERT INTO games VALUES (?, ?, ?, ?)', [
	('agent-hugo-hula-holiday', 'Agent Hugo: Hula Holiday', 'attractive', 'https://www.mobygames.com/game/81315/agent-hugo-hula-holiday/'),
	('alan-hansens-sports-challenge', 'Alan Hansen\'s Sports Challenge', 'oxygen', 'https://www.mobygames.com/game/141866/alan-hansens-sports-challenge/'),
	('alien-trilogy', 'Alien Trilogy', 'probe', 'https://www.mobygames.com/game/1267/alien-trilogy/'),
	('armorines-project-swarm', 'Armorines: Project S. W. A. R. M.', 'probe', 'https://www.mobygames.com/game/5600/armorines-project-swarm/'),
	('army-men-rts', 'Army Men RTS', 'coyote', 'https://www.mobygames.com/game/6420/army-men-rts/'),
	('autonauts', 'Autonauts', 'warp', 'https://denki.co.uk/games/autonauts/'),
	('bionicle', 'Bionicle', 'coyote', 'https://www.mobygames.com/game/11487/bionicle/'),
	('brain-voyage', 'Brain Voyage', 'razorback', 'https://www.mobygames.com/game/35194/brain-voyage/'),
	('cheggers-party-quiz', 'Cheggers Party Quiz', 'oxygen', 'https://www.mobygames.com/game/44727/cheggers-party-quiz/'),
	('disney-sing-it-family-hits', 'Disney Sing It: Family Hits', 'zoe-mode', 'https://www.mobygames.com/game/86159/disney-sing-it-family-hits/'),
	('disney-sing-it-party-hits', 'Disney Sing It: Party Hits', 'zoe-mode', 'https://www.mobygames.com/game/207245/disney-sing-it-party-hits/'),
	('doctor-who', 'Doctor Who: The Edge of Time', 'warp', 'https://www.maze-theory.com/our-games/doctor-who-the-edge-of-time'),
	('european-super-league', 'European Super League', 'coyote', 'https://www.mobygames.com/game/4381/european-super-league/'),
	('forsaken', 'Forsaken', 'probe', 'https://www.mobygames.com/game/117/forsaken/'),
	('gravity-crash', 'Gravity Crash', 'just-add-water', 'https://www.mobygames.com/game/psp/gravity-crash/'),
	('haunt', 'Haunt', 'zoe-mode', 'https://www.mobygames.com/game/125591/haunt/'),
	('homestead', 'Homestead Arcana', 'warp', 'https://www.xbox.com/en-us/games/store/homestead-arcana/9n7thwlzzbwr'),
	('i-ninja', 'I-Ninja', 'coyote', 'https://www.mobygames.com/game/11808/i-ninja/'),
	('just-cause', 'Just Cause', 'avalanche', 'https://www.mobygames.com/game/24152/just-cause/'),
	('nat-geo-tv', 'Kinect Nat Geo TV', 'relentless', 'https://www.youtube.com/watch?v=8lSoupuFkLg'),
	('kylie-sing-and-dance', 'Kylie Sing and Dance', 'echo-peak', 'https://www.youtube.com/watch?v=bH8qZkN9VHY'),
	('lawn-mowing-simulator', 'Lawn Mowing Simulator', 'warp', 'https://www.youtube.com/watch?v=BeR_0NsxuIc'),
	('operation-vietnam', 'Operation Vietnam', 'coyote', 'https://www.youtube.com/watch?v=ggpTWWxC3Xo'),
	('peaky-blinders', 'Peaky Blinders: Mastermind', 'warp', 'https://www.youtube.com/watch?v=qEvvS2uZZ6I'),


])
db.execute('CREATE TABLE releases (id TEXT, platform TEXT)')
db.executemany('INSERT INTO releases VALUES (?, ?)', [
	('agent-hugo-hula-holiday', 'wii'),
	('agent-hugo-hula-holiday', 'pc'),
	('agent-hugo-hula-holiday', 'ps2'),
	('alan-hansens-sports-challenge', 'wii'),
	('alan-hansens-sports-challenge', 'pc'),
	('alan-hansens-sports-challenge', 'ps2'),
	('alien-trilogy', 'pc'),
	('armorines-project-swarm', 'n64'),
	('army-men-rts', 'gamecube'),
	('autonauts', 'switch'),
	('autonauts', 'xbox-gamecore'),
	('autonauts', 'ps4'),
	('autonauts', 'ps5'),
	('bionicle', 'gamecube'),
	('brain-voyage', 'ds'),
	('disney-sing-it-family-hits', 'wii'),
	('disney-sing-it-family-hits', 'ps3'),
	('disney-sing-it-party-hits', 'wii'),
	('disney-sing-it-party-hits', 'ps3'),
	('doctor-who', 'quest'),
	('european-super-league', 'dc'),
	('european-super-league', 'psx'),
	('european-super-league', 'pc'),
	('forsaken', 'psx'),
	('forsaken', 'pc'),
	('forsaken', 'n64'),
	('gravity-crash', 'ps3'),
	('haunt', 'kinect-360'),
	('homestead', 'xbox-series'),
	('i-ninja', 'gamecube'),
	('just-cause', 'ps2'),
	('nat-geo-tv', 'kinect-360'),
	('kylie-sing-and-dance', 'wii'),
	('lawn-mowing-simulator', 'switch'),
	('operation-vietnam', 'ds'),
	('peaky-blinders', 'pc'),
])
db.execute('CREATE TABLE contracts (game TEXT, client TEXT)')
db.executemany('INSERT INTO contracts VALUES (?, ?)', [
	('agent-hugo-hula-holiday', 'attractive'),
	('alan-hansens-sports-challenge', 'oxygen'),
	('brain-voyage', 'razorback'),
	('cheggers-party-quiz', 'oxygen'),
	('disney-sing-it-family-hits', 'zoe-mode'),
	('disney-sing-it-party-hits', 'zoe-mode'),
	('doctor-who', 'warp'),
	('gravity-crash', 'just-add-water'),
	('haunt', 'zoe-mode'),
	('homestead', 'warp'),
	('just-cause', 'avalanche'),
	('nat-geo-tv', 'relentless'),
	('kylie-sing-and-dance', 'echo-peak'),
	('lawn-mowing-simulator', 'warp'),
	('operation-vietnam', 'coyote'),
	('peaky-blinders', 'warp'),
])
db.execute('CREATE TABLE employments (game TEXT, employer TEXT)')
db.executemany('INSERT INTO employments VALUES (?, ?)', [
	('alien-trilogy', 'probe'),
	('armorines-project-swarm', 'probe'),
	('army-men-rts', 'coyote'),
	('autonauts', 'warp'),
	('bionicle', 'coyote'),
	('european-super-league', 'coyote'),
	('i-ninja', 'coyote'),
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

#images = 'https://raw.githubusercontent.com/Powered-Up-Games/PoweredUpGames/main/images'
images = 'images'

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
					document.stag('source', srcset=f'{images}/logo-{size}.webp', media=f'(max-width: {size}px)')
				document.stag('img', src=f'{images}/logo-1024.webp', alt='Powered Up Games Logo')
		with tag('p'):
			text('Powered Up Games provides professional game development services. We have many years experience in porting, automation, optimization, training, and debugging.')
		with tag('h2'):
			text('studios')
		for name, id, url in studios:
			with tag('picture'):
				for size in sizes:
					document.stag('source', srcset=f'{images}/studios/{id}-{size}.webp', media=f'(max-width: {size}px)')
				document.stag('img', src=f'{images}/studios/{id}-1024.webp', alt=f'{name} Logo')

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
