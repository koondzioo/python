def read_file(file_name):
    """Function to read students from file"""
    with open(file_name, "r") as f:
        students = f.read().splitlines()
    return students


def main():
    """Main function to find students of both classes"""
    cpp = read_file('studenci_cpp.txt')
    python = read_file('studenci_python.txt')
    return [student for student in cpp if student in python]


if __name__ == '__main__':
    print(main())
