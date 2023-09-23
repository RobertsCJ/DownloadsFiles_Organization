import os
#os.path.expanduser() ver a pasta home usuario
#os.system(pwd) atual diretorio 
def replace_downloads():
	print('O sistema de pastas esta ativo...')
	while True:
		for file in os.listdir('downloads'): 
			tipo = file[file.index('.'):]
			if tipo  in '.jpg.png':
				os.replace(f'/data/data/com.termux/files/home/storage/termux/file-move/downloads/{file}', f'/data/data/com.termux/files/home/storage/termux/file-move/pictures/{file}')
			elif tipo in '.mp3.wav':
				os.replace(f'/data/data/com.termux/files/home/storage/termux/file-move/downloads/{file}', f'/data/data/com.termux/files/home/storage/termux/file-move/musics/{file}')
			elif tipo in '.mp4.mkv.m4a':
				os.replace(f'/data/data/com.termux/files/home/storage/termux/file-move/downloads/{file}', f'/data/data/com.termux/files/home/storage/termux/file-move/videos/{file}')
			elif tipo in '.html.js.css.py.jar':
				os.replace(f'/data/data/com.termux/files/home/storage/termux/file-move/downloads/{file}', f'/data/data/com.termux/files/home/storage/termux/file-move/projects/{file}')
			elif tipo in '.docx.pdf.odf.odt.doc.csv':
				os.replace(f'/data/data/com.termux/files/home/storage/termux/file-move/downloads/{file}', f'/data/data/com.termux/files/home/storage/termux/file-move/docs/{file}')
			#os.replace(f'/data/data/com.termux/files/home/storage/termux/file-move/downloads/{file}', f'/data/data/com.termux/files/home/storage/termux/file-move/pictures/{file}')
		break ##por enquanto
replace_downloads()
