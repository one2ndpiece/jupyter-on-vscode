import os
import argparse

def valid_path(arg_value):
    if not os.path.exists(arg_value):
        raise argparse.ArgumentTypeError(f"The path {arg_value} does not exist.")
    return os.path.abspath(arg_value)

def list_directory_recursive(path, ignore_paths=[], level=0):
    dirs = []
    ignored_dirs = []
    files = []
    for item in os.listdir(path):
        full_path = os.path.abspath(os.path.join(path, item))
        if full_path in ignore_paths:
            if os.path.isdir(full_path):
                ignored_dirs.append(item)
            continue
        if os.path.isdir(full_path):
            dirs.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    total_items = len(dirs) + len(files) + len(ignored_dirs)
    count = 0

    sub_indent = '│   ' * level

    for d in dirs:
        count += 1
        is_last_item = count == total_items
        branch = '└── ' if is_last_item else '├── '
        print(f'{sub_indent}{branch}{d}/')
        list_directory_recursive(os.path.join(path, d), ignore_paths, level + 1)
        
    for d in ignored_dirs:
        count += 1
        is_last_item = count == total_items
        branch = '└── ' if is_last_item else '├── '
        print(f'{sub_indent}{branch}{d}/')

    for f in files:
        count += 1
        is_last_item = count == total_items
        branch = '└── ' if is_last_item else '├── '
        print(f'{sub_indent}{branch}{f}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List directory contents.')
    parser.add_argument('path', nargs='?', default='.', type=valid_path, help='The path of the directory to list. Default is current directory.')
    parser.add_argument('--ignore', nargs='*', default=[], type=valid_path, help='List of directories or files to ignore.')

    args = parser.parse_args()
    list_directory_recursive(args.path, args.ignore)
