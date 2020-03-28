import argparse


def arg_parser():
    """Function to catch command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', help="File name: ", type=str, required=True)
    parser.add_argument('--text',
                        help="Add this text to the end of file", type=str, required=True)
    return parser.parse_args()


def save_to_file(file_name, text):
    """Function save text to file"""
    with open(file_name, "a") as f:
        f.write('{}\n'.format(text))


if __name__ == '__main__':
    arguments = arg_parser()
    save_to_file(arguments.filename, arguments.text)
