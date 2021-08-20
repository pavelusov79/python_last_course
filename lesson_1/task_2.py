import os


def show_files(path):
    if os.path.exists(path):
        content = os.listdir(path)
        for item in content:
            if os.path.isfile(os.path.join(path, item)):
                print(f'file_name: {item}\npath: {os.path.join(path, item)}')
                print('-'*80)
            else:
                print(f'directory: {item}')
                show_files(os.path.join(path, item))
    else:
        print('path does not exist')


show_files('/home/pavel/Documents/GEEKBRAINS_COURSES/linux/')




