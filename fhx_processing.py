""" fhx_processing.py  Dan Hayes  10 Oct, 2021
Developed based on a FHX file exported from DeltaV version 14.3.

Processes a DeltaV FHX file to compile data to CSV files.
"""

import csv
import os

def func_read_fhx(fhx_file_name):
    """ Reads a FHX file and returns a list. """

    fhx_list = []

    with open(fhx_file_name, encoding='utf-16 LE') as dv_in_file:
        for dv_in_line in dv_in_file:
            fhx_list.append(dv_in_line.rstrip('\n'))

    print("FHX file read complete")
    print()
    return fhx_list


def func_module_class(fhx_list, fhx_template_list):
    """ Searches for module class properties and writes to a CSV file. """
    #Call func_module_class before the other file output functions
    #func_module_class creates the 'output' folder if it does not exist.

    fhx_obj_list = []

    temp_list = []
    temp_list_a = []

    read_active = False

    print("Processing FHX file for Module Classes")

    #Write header line
    fhx_obj_list.append(fhx_template_list)

    for fhx_line in fhx_list:
        for fhx_template_item in fhx_template_list:
            #Check for header
            if fhx_line[0:18] == fhx_template_item + " NAME=":
                read_active = True
                temp_list = fhx_line.split('"')
                temp_list_a.append(temp_list[1])
                temp_list_a.append(temp_list[3])
                temp_list = []

            #Check for properties
            if read_active:
                fhx_tmp_item_size = len(fhx_template_item)
                prop_len = (fhx_tmp_item_size + 3)

                if fhx_line[2:prop_len] == fhx_template_item + "=":
                    temp_list = fhx_line.split('=')
                    temp_list_a.append(temp_list[1].strip('"'))
                    temp_list = []
                    break

                #Check for end of object and update list
                if len(fhx_line) > 0:
                    if fhx_line[0] == "}":
                        fhx_obj_list.append(temp_list_a)
                        temp_list_a = []
                        read_active = False


    #Write data to file
    filename = "output/_module_class.csv"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as fhx_obj_csv:
        writer = csv.writer(fhx_obj_csv)
        writer.writerows(fhx_obj_list)

    print('Module Classes written to file _module_class.csv')
    print()


def func_class_attrib(fhx_list, fhx_template_list):
    """ Searches for module class instance attributes and writes to a CSV file. """

    fhx_obj_list = []

    temp_list = []
    temp_list_a = []

    read_active = False

    module_name = ""
    attrib_name = ""

    print("Processing FHX file for Module Class Attributes")

    #Write header line
    fhx_obj_list.append(fhx_template_list)

    for fhx_line in fhx_list:
        #Check for header
        if fhx_line[0:18] == fhx_template_list[0] + " NAME=":
            read_active = True
            temp_list = fhx_line.split('"')
            module_name = temp_list[1]

        for fhx_template_item in fhx_template_list:
            #Check for attributes
            if read_active:
                fhx_tmp_item_size = len(fhx_template_item)
                prop_len = (fhx_tmp_item_size)

                if fhx_line[2:prop_len + 2] == fhx_template_item:
                    temp_list = fhx_line.split('=')
                    attrib_name = temp_list[1].strip('"')

                if fhx_line[4:prop_len + 4] == fhx_template_item:
                    temp_list = fhx_line.split('=')
                    temp_list_a.append(module_name)
                    temp_list_a.append(attrib_name)
                    temp_list_a.append (temp_list)
                    temp_list = []
                    fhx_obj_list.append(temp_list_a)
                    temp_list_a = []

            #Check for end of object and update list
            if len(fhx_line) > 0:
                if fhx_line[0] == "}":
                    read_active = False
                    first_attrib = True


    #Write data to file
    with open('output/_module_class_attrib.csv', 'w', newline='') as fhx_obj_csv:
        writer = csv.writer(fhx_obj_csv)
        writer.writerows(fhx_obj_list)

    print('Module Class Attributes written to file _module_class_inst_attrib.csv')
    print()


def func_module_instance(fhx_list, fhx_template_list):
    """ Searches for module class instance properties and writes to a CSV file. """

    fhx_obj_list = []

    temp_list = []
    temp_list_a = []

    read_active = False

    print("Processing FHX file for Module Class Instances")

    #Write header line
    fhx_obj_list.append(fhx_template_list)

    for fhx_line in fhx_list:
        for fhx_template_item in fhx_template_list:
            #Check for header
            if fhx_line[0:20] == fhx_template_item + " TAG=":
                read_active = True
                temp_list = fhx_line.split('"')
                temp_list_a.append(temp_list[1])
                temp_list_a.append(temp_list[3])
                temp_list_a.append(temp_list[5])
                temp_list_a.append(temp_list[7])
                temp_list = []

            #Check for properties
            if read_active:
                fhx_tmp_item_size = len(fhx_template_item)
                prop_len = (fhx_tmp_item_size + 3)

                if fhx_line[2:prop_len] == fhx_template_item + "=":
                    temp_list = fhx_line.split('=')
                    temp_list_a.append(temp_list[1].strip('"'))
                    temp_list = []
                    break

                #Check for end of object and update list
                if len(fhx_line) > 0:
                    if fhx_line[0] == "}":
                        fhx_obj_list.append(temp_list_a)
                        temp_list_a = []
                        read_active = False


    #Write data to file
    with open('output/_module_class_inst.csv', 'w', newline='') as fhx_obj_csv:
        writer = csv.writer(fhx_obj_csv)
        writer.writerows(fhx_obj_list)

    print('Module Class Instances written to file _module_class_inst.csv')
    print()


def func_instance_attrib(fhx_list, fhx_template_list):
    """ Searches for module class instance attributes and writes to a CSV file. """

    fhx_obj_list = []

    temp_list = []
    temp_list_a = []

    read_active = False

    module_name = ""
    attrib_name = ""

    print("Processing FHX file for Module Class Instance Attributes")

    #Write header line
    fhx_obj_list.append(fhx_template_list)

    for fhx_line in fhx_list:
        #Check for header
        if fhx_line[0:20] == fhx_template_list[0] + " TAG=":
            read_active = True
            temp_list = fhx_line.split('"')
            module_name = temp_list[1]

        for fhx_template_item in fhx_template_list:
            #Check for attributes
            if read_active:
                fhx_tmp_item_size = len(fhx_template_item)
                prop_len = (fhx_tmp_item_size)

                if fhx_line[2:prop_len + 2] == fhx_template_item:
                    temp_list = fhx_line.split('=')
                    attrib_name = temp_list[1].strip('"')

                if fhx_line[4:prop_len + 4] == fhx_template_item:
                    temp_list = fhx_line.split('=')
                    temp_list_a.append(module_name)
                    temp_list_a.append(attrib_name)
                    temp_list_a.append (temp_list)
                    temp_list = []
                    fhx_obj_list.append(temp_list_a)
                    temp_list_a = []

            #Check for end of object and update list
            if len(fhx_line) > 0:
                if fhx_line[0] == "}":
                    read_active = False
                    first_attrib = True


    #Write data to file
    with open('output/_module_class_inst_attrib.csv', 'w', newline='') as fhx_obj_csv:
        writer = csv.writer(fhx_obj_csv)
        writer.writerows(fhx_obj_list)

    print('Module Class Instance Attributes written to file _module_class_inst_attrib.csv')
    print()


def func_module(fhx_list, fhx_template_list):
    """ Searches for classless module properties and writes to a CSV file. """

    fhx_obj_list = []

    temp_list = []
    temp_list_a = []

    read_active = False

    print("Processing FHX file for Classless Modules")

    #Write header line
    fhx_obj_list.append(fhx_template_list)

    for fhx_line in fhx_list:
        for fhx_template_item in fhx_template_list:
            #Check for header
            if fhx_line[0:11] == fhx_template_item + " TAG=":
                read_active = True
                temp_list = fhx_line.split('"')
                temp_list_a.append(temp_list[1])
                temp_list_a.append(temp_list[3])
                temp_list_a.append(temp_list[5])
                temp_list = []

            #Check for properties
            if read_active:
                fhx_tmp_item_size = len(fhx_template_item)
                prop_len = (fhx_tmp_item_size + 3)

                if fhx_line[2:prop_len] == fhx_template_item + "=":
                    temp_list = fhx_line.split('=')
                    temp_list_a.append(temp_list[1].strip('"'))
                    temp_list = []
                    break

                #Check for end of object and update list
                if len(fhx_line) > 0:
                    if fhx_line[0] == "}":
                        fhx_obj_list.append(temp_list_a)
                        temp_list_a = []
                        read_active = False


    #Write data to file
    with open('output/_classless_module.csv', 'w', newline='') as fhx_obj_csv:
        writer = csv.writer(fhx_obj_csv)
        writer.writerows(fhx_obj_list)

    print('Classless Modules written to file _classless_module.csv')
    print()

def func_mod_attrib(fhx_list, fhx_template_list):
    """ Searches for classless module attributes and writes to a CSV file. """

    fhx_obj_list = []

    temp_list = []
    temp_list_a = []

    read_active = False

    module_name = ""
    attrib_name = ""

    print("Processing FHX file for Class Module Attributes")

    #Write header line
    fhx_obj_list.append(fhx_template_list)

    for fhx_line in fhx_list:
        #Check for header
        if fhx_line[0:11] == fhx_template_list[0] + " TAG=":
            read_active = True
            temp_list = fhx_line.split('"')
            module_name = temp_list[1]

        for fhx_template_item in fhx_template_list:
            #Check for attributes
            if read_active:
                fhx_tmp_item_size = len(fhx_template_item)
                prop_len = (fhx_tmp_item_size)

                if fhx_line[2:prop_len + 2] == fhx_template_item:
                    temp_list = fhx_line.split('=')
                    attrib_name = temp_list[1].strip('"')

                if fhx_line[4:prop_len + 4] == fhx_template_item:
                    temp_list = fhx_line.split('=')
                    temp_list_a.append(module_name)
                    temp_list_a.append(attrib_name)
                    temp_list_a.append (temp_list)
                    temp_list = []
                    fhx_obj_list.append(temp_list_a)
                    temp_list_a = []

            #Check for end of object and update list
            if len(fhx_line) > 0:
                if fhx_line[0] == "}":
                    read_active = False
                    first_attrib = True


    #Write data to file
    with open('output/_classless_module_attrib.csv', 'w', newline='') as fhx_obj_csv:
        writer = csv.writer(fhx_obj_csv)
        writer.writerows(fhx_obj_list)

    print('Classless Module Attributes written to file _classless_module_attrib.csv')
    print()

def main():
    fhx_list = []

    FHX_FILE_NAME = 'DeltaV_In.fhx'

    # Module Class fields
    MC_FIELDS = ['MODULE_CLASS',
                'CATEGORY',
                'DESCRIPTION',
                'PERIOD',
                'PRIMARY_CONTROL_DISPLAY',
                'INTRUMENT_AREA_DISPLAY',
                'DETAIL_DISPLAY',
                'TYPE',
                'SUB_TYPE',
                'NVM',
                'ELECTRONIC_SIGNATURE_POLICY']

    # Module Class Attributes fields
    MC_ATTRIBUTES = ['MODULE_CLASS',
                     'ATTRIBUTE_INSTANCE',
                     'VALUE']


    # Module Instance fields
    MI_FIELDS = ['MODULE_INSTANCE',
                'PLANT_AREA',
                'MODULE_CLASS',
                'CATEGORY',
                'DESCRIPTION',
                'WORK_IN_PROGRESS',
                'PERIOD',
                'PRIMARY_CONTROL_DISPLAY',
                'INSTRUMENT_AREA_DISPLAY',
                'DETAIL_DISPLAY',
                'TYPE',
                'SUB_TYPE',
                'NVM',
                'PRINT_BANNER_TITLE1',
                'PRINT_BANNER_TITLE2',
                'PERSIST',
                'USES_CLASS_SIGNATURE_POLICY']

    # Module Instance Attributes fields
    MI_ATTRIBUTES = ['MODULE_INSTANCE',
                     'ATTRIBUTE_INSTANCE',
                     'VALUE']

    # Module (classless) fields
    MOD_FIELDS = ['MODULE',
                  'PLANT_AREA',
                  'CATEGORY',
                  'DESCRIPTION',
                  'PERIOD',
                  'CONTROLLER',
                  'PRIMARY_CONTROL_DISPLAY',
                  'INSTRUMENT_AREA_DISPLAY',
                  'DETAIL_DISPLAY',
                  'TYPE',
                  'SUB_TYPE',
                  'ASSIGN_BLOCKS_TO_H1_CARD']

    # Classless Module Attributes fields
    MOD_ATTRIBUTES = ['MODULE',
                     'ATTRIBUTE_INSTANCE',
                     'VALUE']

    #Read FHX file
    fhx_list = func_read_fhx(FHX_FILE_NAME)

    # Search for object properties and write to CSV file
    func_module_class(fhx_list, MC_FIELDS)
    func_class_attrib(fhx_list, MC_ATTRIBUTES)
    func_module_instance(fhx_list, MI_FIELDS)
    func_instance_attrib(fhx_list, MI_ATTRIBUTES)
    func_module(fhx_list, MOD_FIELDS)
    func_mod_attrib(fhx_list, MOD_ATTRIBUTES)


# Call main when run as script
if __name__ == '__main__':
    main()
