"""
This script is designed to create Paradox's proprietary GFX Portrait txt files for Stellaris portrait mods.
The script is modular and will create the text file with any number of portraits so long as they are in the format race_name_NUMBER.dds
Each section builds one critical portion of the txt file.

V 1.2
Tristan Lundgreen
"""

#Library imports
import platform
import os

#Set image directory, file output directory, custo race name, and default race image here
image_directory = 'your/directory/here'
output_directory = 'your/directory/here'
race_name = 'race_name'
race_image = '1'

class text_generator:

    def __init__(self):
        self.image_directory = image_directory
        self.output_directory = output_directory
        self.race_name = race_name
        self.race_image = race_image

    def string_iterator(self, limit, start_string, iterate_string, *args):
        counter = 1
        loopproduct=''
        for filename in os.listdir(image_directory):
            if counter > limit:
                break
            else:
                counter_string = str(counter)
                loopproduct += iterate_string.format(*args, *([counter_string]*iterate_string.count('{}')))
                counter += 1
        processed_string = start_string + loopproduct
        return processed_string

    def get_file_count(self):
        #Checking for appropriate number of files to work with
        OS = platform.system()
        if OS == 'Darwin':
            count = 0
            #Iterate image_directory
            for path in os.listdir(image_directory):
                # check if current path is a file
                if os.path.isfile(os.path.join(image_directory, path)):
                    count = count + 1
            count = count - 1
            limit = count
            print('File count:', count)
        else:
            count = 0
            #Iterate image_directory
            for path in os.listdir(image_directory):
                # check if current path is a file
                if os.path.isfile(os.path.join(image_directory, path)):
                    count = count + 1
            limit = count
        return  limit

    def portraits_section(self, limit):
        start_string = 'portraits = { \n#Default'
        iterate_string = '\n	'+race_name+'_{}= {{texturefile = "gfx/models/portraits/'+race_name+'/'+race_name+'_{}.dds"}}'
        portrait_string = self.string_iterator(limit, start_string, iterate_string)
        #print(portrait_string)
        return portrait_string

    def portrait_groups_section(self, limit):
        start_string = '\n}\n\nportrait_groups = {\n	'+race_name+'= {\n		default = '+race_name+'_'+race_image+'\n		game_setup = {\n			add ={\n 				portraits = {'
        iterate_string = '\n					'+race_name+'_{}'
        portrait_groups_string = self.string_iterator(limit, start_string, iterate_string)
        #print(portrait_groups_string)
        return portrait_groups_string

    def leaders_section(self, limit):
        start_string = '\n				}\n			}\n		}\n		leader = {\n			add = {\n						portraits = {'
        iterate_string = '\n 							'+race_name+'_{}'
        leaders_string = self.string_iterator(limit, start_string, iterate_string)
        #print(leaders_string)
        return leaders_string

    def rulers_section(self, limit):
        start_string = '\n				}\n			}\n		}\n		ruler = {\n			add = {\n						portraits = {'
        iterate_string = '\n 							'+race_name+'_{}'
        rulers_string = self.string_iterator(limit, start_string, iterate_string)
        #print(rulers_string)
        return  rulers_string

    def set_species_portrait_section(self):
        string = '\n				}\n			}\n		}\n		species = {\n			set = {\n						portraits = {\n					'+race_name+'_'+race_image+'\n				}\n			}\n		}\n'
        species_portrait_string = string
        #print(species_portrait_string)
        return species_portrait_string

def main():
    #Generate required components
    text_generator_obj = text_generator()
    count_limit = text_generator_obj.get_file_count()
    portraits_string = text_generator_obj.portraits_section(count_limit)
    portrait_groups_string = text_generator_obj.portrait_groups_section(count_limit)
    leaders_string = text_generator_obj.leaders_section(count_limit)
    rulers_string = text_generator_obj.rulers_section(count_limit)
    species_portrait_string = text_generator_obj.set_species_portrait_section()

    #Assemble components and export
    file = open(output_directory+'/'+race_name+'_'+race_name+'.txt', 'w')
    file.write(portraits_string + portrait_groups_string + leaders_string + rulers_string + species_portrait_string)
    print('Necessary text file has been placed in '+output_directory+'/'+race_name+'_'+race_name+'.txt')

if __name__ == '__main__':
    main()