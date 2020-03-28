import argparse
import sys

#TODO wczytac jedna metoda i przerobic dane

def read_file_all_lines(file_name):
    """Function to read all lines in file"""
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


def read_file_without_comments(file_name):
    """Function to read file without comments"""
    with open(file_name, "r") as f:
        data = [line.splitlines() for line in f if not line.startswith('#')]
    return data


def read_file_with_index(file_name):
    """Function to read file with index"""
    with open(file_name, "r") as f:
        data = ['{} --> {}'.format(idx, line.splitlines()) for idx, line in enumerate(f, 1)]
    return data


def arg_parser():
    """Function to catch command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', help="File name: ", type=str, required=True)
    parser.add_argument('--mode',
                        help="Mode how to read file, 0 - (default choice) read whole file, 1 - omit lines with # at the beginning, 2 - line numbering",
                        choices=[0, 1, 2], default=0, type=int, required=False)
    return parser.parse_args()


if __name__ == '__main__':
    arguments = arg_parser()
    if arguments.mode == 0:
        print(read_file_all_lines(arg_parser().filename))
    elif arguments.mode == 1:
        print(read_file_without_comments(arg_parser().filename))
    elif arguments.mode == 2:
        print(read_file_with_index(arg_parser().filename))
