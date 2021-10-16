""" FileUI.py  Dan Hayes 16 Oct, 2021
Develop user interface for accessing files in fhx_processing.py.
"""


def func_display_menu():
    """ Displays an option menu """
    print("fhx_processing MENU")
    print()
    print("1  Input Path")
    print("2  Input Filename")
    print("3  Execute fhx_processing")
    print()
    print("Select option and press Enter")
    response = input("Press enter without an option to exit ")

def func_get_path():
    pass

def func_store_path():
    pass

def func_get_filename():
    pass

def func_store_filename():
    pass

def func_display_current():
    pass

def main():
    # Display option menu
    func_display_menu()

# Call main when run as script
if __name__ == '__main__':
    main()
