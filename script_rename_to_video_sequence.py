import os
import ffmpeg

print('Folder name:')
folderDir = f'{input()}\\'

picsName = os.listdir(folderDir)
LRL = 0
LRR = 0
LRL_dict = {}
LRR_dict = {}

for i in range(len(picsName)):
  pic = picsName[i]
  if(pic[-3:].lower() != 'jpg'):
    continue
  else:
    print(pic)
    nameSplit = pic.split('_')
    typeName = nameSplit[1][:-4][-3:]
    if(typeName == 'LRL'):
      LRL += 1
      new_name = nameSplit[0] + '_LRL_' + f'{LRL:05}' + '.jpg'
      LRL_dict[new_name] = pic
      try:
        os.rename(folderDir + pic, folderDir + new_name)
      except:
        pass
    if(typeName == 'LRR'):
      LRR += 1
      new_name = nameSplit[0] + '_LRR_' + f'{LRR:05}' + '.jpg'
      LRL_dict[new_name] = pic
      try:
        os.rename(folderDir + pic, new_name)
      except:
        pass

# filenames = os.listdir(folderDir)
# prefix = filenames[0].split('_')[0]

# print('Frame rate :')
# framerate = f'{input()}'


# rightComp = ffmpeg.input(f'{folderDir+prefix}_%05_20240117-11h52m05s_06024LRL.JPG', framerate=framerate)
# rightComp = ffmpeg.filter(rightComp, 'drawtext', text='%{n}', x=10, y=10, fontfile='C:/Windows/Fonts/Arial.ttf', fontsize=150, fontcolor='white')
# leftImages = ffmpeg.input(f'{folderDir+prefix}_%05dLRL.JPG', framerate=framerate)
# leftText = ffmpeg.drawtext(leftImages, text='LRL', x=10, y=10, fontfile='C:/Windows/Fonts/Arial.ttf', fontsize=300, fontcolor='white')

# finalComp = ffmpeg.filter([leftText, rightComp], 'vstack')
# outputVideo = ffmpeg.output(finalComp, f'{folderDir + prefix}_video.mp4', crf=20, s='1300x1920')
# ffmpeg.run(outputVideo)

ok = input("Press enter to exit !")