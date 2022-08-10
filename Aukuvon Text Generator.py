# -*- coding: utf-8 -*-
"""
This script is designed to create GFX Portrait txt files for stellaris portrait mods.
The script is modular and will create the text file with any number of portraits so long as they are in the format RaceName_NUMBER.dds
Each section builds one critical portion of the txt file.

V 1.1
Tristan Lundgreen
"""
#Library imports
import platform
import os

#Set image directory, file output directory, custo race name, and default race image here
imagedirectory = '/Users/user/Documents/4) Projects/5) Gaming/Mods/Stellaris/Aukuvon/gfx/models/portraits/Aukuvon'
outputdirectory = '/Users/user/Documents/4) Projects/5) Gaming/Mods/Stellaris'
racename = 'Aukvon'
raceimage= '77'


#Checking for appropriate number of files to work with
OS = platform.system()
if OS=='Darwin':
    count = 0
    # Iterate imagedirectory
    for path in os.listdir(imagedirectory):
        # check if current path is a file
        if os.path.isfile(os.path.join(imagedirectory, path)):
            count = count + 1
    count=count-1
    limit=count
    print('File count:', count)
else:
    count = 0
    # Iterate imagedirectory
    for path in os.listdir(imagedirectory):
        # check if current path is a file
        if os.path.isfile(os.path.join(imagedirectory, path)):
            count = count + 1
    limit=count
#%%
string='portraits = { \n#Default'
counter=1
loopproduct=''
for filename in os.listdir(imagedirectory):
    if counter>limit:
        break
    else:
        loopstring =''
        counterstring=str(counter)
        loopproduct=loopproduct+'\n	'+racename+'_'+counterstring+ '= {texturefile = "gfx/models/portraits/'+racename+'/'+racename+'_'+counterstring+'.dds"}'
        counter=counter +1
string=string+loopproduct
#%%%%
string1='\n}\n\nportrait_groups = {\n	'+racename+'= {\n		default = '+racename+'_'+raceimage+'\n		game_setup = {\n			add ={\n 				portraits = {'
string=string+string1
counter=1
loopproduct=''
for filename in os.listdir(imagedirectory):
    if counter>limit:
        break
    else:
        loopstring =''
        counterstring=str(counter)
        loopproduct=loopproduct+'\n					'+racename+'_'+counterstring
        counter=counter +1
string=string+loopproduct
print(string)
#%%
string2='\n				}\n			}\n		}\n		leader = {\n			add = {\n						portraits = {'
string=string+string2
counter=1
loopproduct=''
for filename in os.listdir(imagedirectory):
    if counter>limit:
        break
    else:
        loopstring =''
        counterstring=str(counter)
        loopproduct=loopproduct+'\n 							'+racename+'_'+counterstring
        counter=counter +1
string=string+loopproduct
#%%
string3='\n				}\n			}\n		}\n		ruler = {\n			add = {\n						portraits = {'
string=string+string3
counter=1
loopproduct=''
for filename in os.listdir(imagedirectory):
    if counter>limit:
        break
    else:
        loopstring =''
        counterstring=str(counter)
        loopproduct=loopproduct+'\n 							'+racename+'_'+counterstring
        counter=counter +1
string=string+loopproduct
#%%
string4='\n				}\n			}\n		}\n		species = {\n			set = {\n						portraits = {\n					'+racename+'_'+raceimage+'\n				}\n			}\n		}\n'
string=string+string4
print(string)
#%%
f = open(outputdirectory+'/'+racename+'_'+racename+'.txt', 'w')
f.write(string)
print('Necessary text file has been placed in '+outputdirectory+'/'+racename+'_'+racename+'.txt')