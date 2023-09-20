import os

#save file name
file_path = '/mnt/c/Dioxine_XPiratez/user/piratez/f1.sav'

#pattern to identify units on the battlefield
search_string = 'directionTurret'

#enemies count (for verification purpose)
count = 0

#list of enemies that require KOS (robots, regeneration etc)
kos_enemies = ['STR_BANDIT_GHOUL','STR_ARMORED_CAR_TERRORIST', 'STR_ANIMATRON_MARAUDER', 'STR_NTURRET_14MM',
                'STR_TURRET_MINIGUN_TERRORIST', 'STR_WEREWOLF_WARRIOR', 'STR_ERIDIAN_SOLDIER', 'STR_ERIDIAN_BEASTMASTER',
                  'STR_ERIDIAN_LEADER', 'STR_XTANK_NAZI_CANNON_TERRORIST']

#load the file into array of strings
with open(file_path, "r") as fp:
	lines = fp.readlines()

#have to use enumerate because working with the above array numeration directly is bugged
with open(file_path, 'r') as fp:
    for l_no, line in enumerate(fp):
        if search_string in line:
            if 'faction: 1' in lines[l_no-4]:
                count = count+1
                #print(lines[l_no+2])
                #print('      health: 1')
                lines[l_no+2] =  '      health: 1\n'
                if any(x in lines[l_no-6] for x in kos_enemies):
                    lines[l_no+4] =  '      stunlevel: 10\n'

#write updated array to the save file                
with open(file_path, "w") as fp:
    fp.writelines(lines)
                                
print(count)