import os
caminho = os.system('cd && pwd')
print(caminho)
if os.curdir.lower() == 'downloads':
	print('esta na downloads')

elif os.name == 'posix':
	##como achar usuario??
	print(os.path.isdir('main.py'))

elif os.name == 'nt':
	print('Eh Ruindows') #eca
