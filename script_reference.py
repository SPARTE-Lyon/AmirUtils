import os
import numpy as np
import xml.etree.ElementTree as ET
import csv
import math

folderDir = f'./sources/{input()}/'
filesName = os.listdir(folderDir)
pics = []

tree = ET.parse(folderDir + filesName[0])
root = tree.getroot()
basePos = np.array([0.0,0.0,0.0])

for f in filesName:
	if(f.split('.')[1] == 'JPG'):
			pics.append(f)

def toFloat(s):
	return float(s)

def euler_from_quaternion(w, x, y, z):

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

        return math.degrees(roll_x), math.degrees(pitch_y), math.degrees(yaw_z)

with open('./sources/data_references_three.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for child in root.iter():
		if child.tag == 'couple':
			lrl_id = child[0].attrib['id']
			lrr_id = child[1].attrib['id']
			if lrl_id in pics and lrr_id in pics:
				pos_text_value = child[0][7][0][1].text
				rot_text_value = child[0][7][0][0].text

				pos_splitted = pos_text_value.split(' ')
				rot_splitted = rot_text_value.split(' ')

				rs = list(map(toFloat, rot_splitted))

				rotations = euler_from_quaternion(rs[0], rs[1], rs[2], rs[3])

				yaw = rotations[2]
				pitch = rotations[1]
				roll = rotations[0]

				addPos = np.array([float(pos_splitted[0]), float(pos_splitted[1]), float(pos_splitted[2])])
				basePos+=addPos
				print(basePos)
				print(yaw, pitch, roll)
				# writer.writerow([lrl_id, basePos[0], basePos[1], basePos[2]])
				writer.writerow([lrl_id, basePos[0], basePos[1], basePos[2], yaw, pitch, roll])
				writer.writerow([lrr_id, basePos[0], basePos[1], basePos[2], yaw, pitch, roll])
