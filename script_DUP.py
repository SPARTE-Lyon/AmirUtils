import os
import shutil

def isolate(s):
	try:
		return s[:-7]
	except:
		return 'null'


print('Folder name:')
folderDir = f'{input()}/'

filesName = os.listdir(folderDir)
pics = []

for f in filesName:
	if(f.split('.')[1].lower() == 'jpg'):
			pics.append(f)

pics = list(map(isolate, pics))
unique_key = set(pics)
folderUniqueDir = folderDir[:-1] + '_Uniques/'

for uk in unique_key:
	if(pics.count(uk)<2):
		try:
			os.mkdir(folderUniqueDir, 0o666)
		except:
			pass
		try:
			shutil.move(folderDir + uk + 'LRR.jpg', folderUniqueDir + uk + 'LRR.jpg')
			print(uk + f'LRR.jpg moved to {folderUniqueDir}')
		except:
			pass
		try:
			os.remove(folderDir + uk + 'LRL.jpg')
			print(uk + f'LRL.jpg moved to {folderUniqueDir}')
		except:
			pass

ok = input("Press enter to exit !")