import os


def search_file(filename, path=os.getcwd()):
    if os.path.exists(path):
        content = os.listdir(path)
        for item in content:
            if os.path.isfile(os.path.join(path, item)):
                if item == filename:
                    print(f'file found...\nfile_name: {item.split(".")[0]}\npath: {os.path.join(path, item)}')
                    break
            if os.path.isdir(os.path.join(path, item)):
                search_file(filename, os.path.join(path, item))

    else:
        print(f'path does not exist')


# search_file('sample_in_folder.txt', '/home/pavel/Documents/GEEKBRAINS_COURSES')
# search_file('login.png', '/home/pavel/Documents')
search_file('task_1.py')
