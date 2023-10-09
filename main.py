import os
from time import sleep

if os.name == 'posix':
	if os.path.isdir(os.getenv('HOME') + '/Downloads'): #linux
		path = os.getenv('HOME') #usuario??
	elif os.path.isdir(os.getenv('HOME') + '/storage/'): #android
		path = os.getenv('HOME') + '/storage/shared'


os.chdir(path); print(os.listdir())
for dir in os.listdir():
	if 'doc' in dir.lower():
		docs = (os.path.abspath(dir)) #doc = pathToDoc
	elif ('picture' or 'image') in dir.lower():
		pics = (os.path.abspath(dir))
	elif ('movies' or 'videos') in dir.lower():
                videos = (os.path.abspath(dir))
	elif 'proje' in dir.lower():
		projects = (os.path.abspath(dir))
	elif ('music' or 'audio') in dir.lower():
		musics = os.path.abspath(dir)
	elif 'download' in dir.lower():
                downloads = (os.path.abspath(dir))


print(downloads, docs, pics, videos, musics)


def replace_downloads():
	print('O sistema esta ativo...')
	while True:
		for file in os.listdir(downloads): 
			tipo = file[file.rfind('.'):]

			if tipo  in '.jpg.png.gif.':
				os.replace(f'{downloads}/{file}', f'{pics}/{file}')

			elif tipo in '.mp3.wav.m4a.opus':
				os.replace(f'{downloads}/{file}', f'{musics}/{file}')
			elif tipo in '.mp4.mkv':
				os.replace(f'/{downloads}/{file}', f'{videos}/{file}')
			elif tipo in '.html.js.css.py.jar':
				if file != 'main.py': 
					if os.path.exists('Projects'):
						os.replace(f'{downloads}/{file}', f'{projects}/{file}')
					else:
						os.replace(f'{downloads}/{file}', f'{docs}/{file}')
			elif tipo in '.docx.pdf.odf.odt.doc.csv':
				os.replace(f'{downloads}/{file}', f'{docs}/{file}')
		break
replace_downloads()
