import os
import shutil

print('Folder name:')
folderDir = f'./sources/{input()}/'
picsName = os.listdir(folderDir)
LRL = folderDir[:-1] + '_LRL/'
LRR = folderDir[:-1] + '_LRR/'

try:
	os.mkdir(LRL, 0o666)
except:
	pass
try:
	os.mkdir(LRR, 0o666)
except:
	pass


for pic in picsName:
	typeName = pic.split('.')[0][-3:]
	if(typeName == 'LRL'):
		shutil.move(folderDir + pic, LRL + pic)
	else:
		shutil.move(folderDir + pic, LRR + pic)

ok = input("Press enter to exit !")