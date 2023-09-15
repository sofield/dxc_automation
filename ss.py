import os

file_path = '/mnt/c/Dioxine_XPiratez/user/piratez/f1.sav'
search_string = 'directionTurret'
count = 0

with open(file_path, "r") as fp:
	lines = fp.readlines()

with open(file_path, 'r') as fp:
    for l_no, line in enumerate(fp):
        if search_string in line:
            if 'faction: 1' in lines[l_no-4]:
                count = count+1
                #print(lines[l_no+2])
                #print('      health: 1')
                lines[l_no+2] =  '      health: 1\n'
                
with open(file_path, "w") as fp:
    fp.writelines(lines)
                                
print(count)