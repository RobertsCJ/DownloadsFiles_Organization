import os

os.chdir(os.getenv('HOME') + '/storage/shared')
os.chdir('Documentos')
print(os.listdir())


'''
####lista os arquivos da pasta home e suas childs
os.chdir(os.getenv('HOME'))
for dir in os.listdir():
	print(dir)
	if os.path.isdir(os.path.abspath(dir)):
		for file in os.listdir(os.path.abspath(dir)):
			print('\t' + file)
'''

