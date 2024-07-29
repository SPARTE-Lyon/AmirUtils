import os

print('Folder name:')
folderDir = f'./sources/{input()}/'

picsName = os.listdir(folderDir)
LRL = 0
LRR = 0

for i in range(len(picsName)):
	pic = picsName[i]
	if(pic[-3:] != 'JPG'):
		continue
	else:
		print(pic)
		nameSplit = pic.split('_')
		typeName = nameSplit[1][:-4][-3:]
		if(typeName == 'LRL'):
			LRL += 1
			try:
				os.rename(folderDir + pic, folderDir + nameSplit[0] + '_LRL_' + f'{LRL:05}' + '.JPG')
			except:
				pass
		else:
			LRR += 1
			try:
				os.rename(folderDir + pic, folderDir + nameSplit[0] + '_LRR_' + f'{LRR:05}' + '.JPG')
			except:
				pass

ok = input("Press enter to exit !")