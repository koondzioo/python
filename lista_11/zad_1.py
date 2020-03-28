import os


def list_folders(folder_path):
    """Function to show files in recursion"""
    path = os.path.abspath(folder_path)
    for file in os.listdir(path):
        print(file)
        path_to_inner_folder = f'{path}/{file}'
        if os.path.isdir(path_to_inner_folder):
            list_folders(path_to_inner_folder)


if __name__ == '__main__':
    list_folders('/home/konrad/Pulpit/Projekty')