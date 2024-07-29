import os
import shutil

def isolate(s):
	try:
		return s[:-7]
	except:
		return 'null'


print('Folder name:')
folderDir = f'./sources/{input()}/'

filesName = os.listdir(folderDir)
pics = []

for f in filesName:
	if(f.split('.')[1] == 'JPG'):
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
			shutil.move(folderDir + uk + 'LRR.JPG', folderUniqueDir + uk + 'LRR.JPG')
			print(uk + f'LRR.JPG moved to {folderUniqueDir}')
		except:
			pass
		try:
			os.remove(folderDir + uk + 'LRL.JPG')
			print(uk + f'LRL.JPG moved to {folderUniqueDir}')
		except:
			pass

ok = input("Press enter to exit !")