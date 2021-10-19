""" FileUI.py  Dan Hayes 16 Oct, 2021
Develop user interface for accessing files in fhx_processing.py.
"""

import os

def func_display_menu():
    """ Displays an option menu """
    print("fhx_processing MENU")
    print()
    print("1  Input Path")
    print("2  Input Filename")
    print("3  Execute fhx_processing")
    print()
    print("Select option and press Enter")
    response = int(input("Press enter without an option to exit "))
    print("response = ", response)

    if response == 1:
        func_get_path()
    elif response == 2:
        func_get_filename()
    else:
        pass

def func_get_path():
    #Prompt for path
    #Consider example path for different operating systems
    path_in = input("Enter the path to the .fhx file (C:\\Folder\\) ")
    print(path_in)

    #Verify path

    #Implement error handling

    #Store path
    func_store_path()

def func_store_path():
    filename = "var_store/path_var.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as path_var_stor:
        path_var_stor.write("C:\Test\Path\\")
    print("Path Stored")

def func_get_filename():
    filename_in = input("Enter the .fhx file filename: ")
    print(filename_in)
    func_store_filename()

def func_store_filename():
    filename = "var_store/filename_var.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as filename_var_stor:
        filename_var_stor.write("Filename")
    print("Filename Stored")

def func_display_current():
    print("Display Current File Properties")

def main():
    # Display option menu
    func_display_menu()

# Call main when run as script
if __name__ == '__main__':
    main()
