import os 
import shutil

def input_function(input_type,filter_list):
    if input("filter by " + input_type + " ? Y or N: ") == "Y":
        filter_list += [input(input_type+": ")]
        while True :
            if input("add another "+ input_type +" ? Y or N: ") == "N":
                break
            else:
                filter_list += [input(input_type + ": ")]

filter_strings = []
input_function("keyword", filter_strings)

filter_file_type = []
input_function("file type",filter_file_type)
    
destination_file = input("destination folder: ")
desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
new_directory_path = os.path.join(desktop_dir, destination_file)
desktop_files = os.listdir(desktop_dir)


def does_file_exist(possible_file,list_of_files):
    for files in list_of_files:
        if files.lower() == possible_file.lower():
            return True
    return False

if does_file_exist(destination_file,desktop_files) == False:
    os.mkdir(new_directory_path)


filtered_files = []
if len(filter_strings) > 0:
    for files in desktop_files:
        for string in filter_strings:
            if string.lower() in files.lower():
                filtered_files.append(files)
else:
    filtered_files = desktop_files

filtered_files2 = []
if len(filter_file_type) > 0:
    for files in filtered_files:
        for file_type in filter_file_type:
            if files.endswith(file_type):
                filtered_files2.append(files)


for files in filtered_files2:
    shutil.move(os.path.join(desktop_dir, files), new_directory_path)

    




