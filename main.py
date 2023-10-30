import sys
import os


class RandomFile(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()


def creating_file_and_add_text(subcommand=None):
    full_name = input("Enter your full name: ")
    with RandomFile(f'{subcommand}.txt') as file:
        file.write(f'My name is {full_name}')
    return True

def main():

    is_file_created, is_file_delete = False, False

    try:
        subcommand = sys.argv[1]

        try:
            file_command = sys.argv[2]

            if file_command == 'create':
                is_file_created = creating_file_and_add_text(subcommand)

            elif file_command == 'delete':
                is_file_delete = True
                os.remove(f'{subcommand}.txt')
        
        except IndexError as e:
            is_file_created = creating_file_and_add_text(subcommand)

    except IndexError as e:
        is_file_created = False
        print("Please input any command after file name. ")

    if is_file_created:
        print("File created successfully. ")
    elif is_file_delete:
        print("File deleted successfully. ")


if __name__ == '__main__':
    main()
