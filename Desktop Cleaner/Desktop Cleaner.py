import os 
import shutil

KNOWN_EXTENSIONS = [
    '.txt', '.csv', '.xls', '.xlsx', '.json', '.xml',
    '.html', '.htm', '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.bmp',
    '.mp3', '.wav', '.flac', '.mp4', '.avi', '.mov',
    '.py', '.js', '.css', '.md', '.markdown',
    '.ini', '.cfg', '.conf', '.zip', '.tar', '.gz'
]

def input_yes_or_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Not a valid option")

def input_function(input_type,filter_list):
    format_specification = " (in the for '.file extension')"
    add_filter = input_yes_or_no("Filter by " + input_type + "? Y or N: ")
    if add_filter:
        while True:
            if input_type == "keyword":
                filter_list.append(input(input_type +": "))
                if not input_yes_or_no("Add another keyword? Y or N: "):
                    break
            else:
                possible_file_type = input(input_type + " " + format_specification + ": ").lower()
                if possible_file_type in KNOWN_EXTENSIONS:
                    filter_list.append(possible_file_type)
                else:
                    print("Not valid or supported file type")
                if not input_yes_or_no("Add another file type? Y or N: "):
                    break

def move_files(filtered_files, destination_folder):
    desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
    new_directory_path = os.path.join(desktop_dir, destination_folder)

    if not os.path.exists(new_directory_path):
        os.mkdir(new_directory_path)

    for file_name in filtered_files:
        shutil.move(os.path.join(desktop_dir, file_name), new_directory_path)


def main():

    filter_strings = []
    input_function("keyword", filter_strings)

    filter_file_type = []
    input_function("file type",filter_file_type)
    
    destination_folder = input("destination folder: ")
    desktop_files = os.listdir(os.path.expanduser('~') + '/Desktop')

    filtered_files = []
    for file_name in desktop_files:
        if any(string.lower() in file_name.lower() for string in filter_strings):
            filtered_files.append(file_name)

    final_filtered_files = []
    if filter_file_type:
        for file_type in filter_file_type:
            for file in filtered_files:
                if file.lower().endswith(file_type):
                    final_filtered_files.append(file)
    else:
        final_filtered_files = filtered_files

    if final_filtered_files:
        move_files(filtered_files, destination_folder)
    else:
        print("No files matched the filter criteria.")

if __name__ == "__main__":
    main()
    




