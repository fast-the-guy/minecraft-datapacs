"""
a python script to make datapack setup/creation easier
"""

import filemanager as fm

# get info from user/hardcoded
print("Welcome to the datapack setup script!")
pack_name = input("Enter the name of your datapack: ")
pack_description = input("Enter a description for your datapack: ")
pack_author = "Fast_the_guy"    # hardcoded because I am lazy/only i use this script
pack_namespace = input("Enter the namespace for your datapack: ")
pack_namespace = pack_namespace.replace(" ", "_") #replace space with _ in namespace


# create the datapack folder structure
def create_root_structure():
    
    
    #1 create the root folder
    fm.mkdir(pack_name)                             #create root folder
    fm.cdir(pack_name)                              #change dir to root folder
    fm.mkdir("data")                                #create data folder for namespaces
    fm.mkdir("data/"+pack_namespace+"/functions")   #create user namespace
    fm.mkdir("data/"+pack_namespace+"/recipe")      #create user recepies
    fm.mkdir("data/"+pack_namespace+"/loot_table")  #create user loot table
    fm.mkdir("data/"+pack_namespace+"/dialog")      #create user dialog folder
    fm.mkdir("data/minecraft/tags/functions")       #create minecraft namespace
    

    #create help.txt
    with open("help.txt", "w") as f:
        f.write("insert pack.png to have icon for datapack")


    #2 create the pack.mcmeta file
    with open("pack.mcmeta", "w") as f:
        f.write('{\n')
        f.write('  "pack": {\n')
        f.write('    "description": "'+pack_description+'",\n')
        f.write('    "pack_format": 80\n')
        f.write('  }\n')
        f.write('}\n')
    
    #3 make tick and load.mcfunction
    #make load.json
    print("working dir is:"+str(fm.lsdir()))
    with open("data/minecraft/tags/functions/load.json", "w") as f:
        f.write("{")
        f.write('    "values": [')
        f.write('"'+pack_namespace+':load"')
        f.write("    ]")
        f.write("}")

    #make tick.json
    with open("data/minecraft/tags/functions/tick.json", "w") as f:
        f.write("{")
        f.write('    "values": [')
        f.write('"'+pack_namespace+':tick"')
        f.write("    ]")
        f.write("}")
    

    #make load.mcfunction
    with open("data/"+pack_namespace+"/functions/load.mcfunction", "w") as f:
        f.write("#this mcfunction will be run when datapack is loaded")
    
    #make tick.mcfunction
    with open("data/"+pack_namespace+"/functions/tick.mcfunction", "w") as f:
        f.write("#this mcfunction will be evry tick")

              


### TESTING DELEATE FOR REAL USE
create_root_structure()
