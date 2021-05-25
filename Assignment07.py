# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Exception Handling Demonstration
# ChangeLog (Who,When,What):
# HJong, 5/22/2021, Started script
# HJong, 5/22/2021, Created functions in Processor class
# HJong, 5/22/2021, Created functions in IO class
# HJong, 5/23/2021, Added while loop to receive user input of file name
# HJong, 5/23/2021, Added try-except block to capture non-existent filename in user input
# HJong, 5/23/2021, Added function calls for pickling and unpickling data
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = ''  # The name of the text file
strBinFileName = '' # The name of the binary file
objFile = None  # An object that represents a file
list_of_string = []  # A list of strings that contains data in strFileName


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of strings

        :param file_name: (string) with name of file
        :return: (list) of strings
        """
        list_of_rows = []
        file = open(file_name, 'r')
        for line in file:
            list_of_rows.append(line)
        file.close()
        return list_of_rows

    @staticmethod
    def pickle_it(file_name, list_of_rows):
        """ Add data into existing list of dictionary

        :param file_name: (string) of file name to pickle data to
        :param list_of_rows: (list) of dictionary rows to add new data to
        :return: nothing
        """
        objFile = open(file_name, 'wb')
        for row in list_of_rows:
            pickle.dump(row, objFile)
        objFile.close()

    @staticmethod
    def unpickle_it(file_name):
        """ Remove data from existing list of dictionary

        :param file_name: (string) of file name to unpickle
        :return: nothing
        """
        list_of_rows = []
        objFile = open(file_name, 'rb')
        for row in list_of_string:
            list_of_rows.append(pickle.load(objFile))
        return list_of_rows

# Presentation --------------------------------------------------------------#
class IO:
    """ User input and output """

    @staticmethod
    def get_user_filename():
        """ Receive user's input of text file name

        param: None
        Return: (string) of file name
        """
        file_name = str(input('Enter the file name with extension: '))
        return file_name

    @staticmethod
    def display_data(list_of_rows):
        """ Display data from the un-pickled file

        :param list_of_rows: (list) of strings
        :return: nothing
        """
        print('The data in the file is: ')
        for row in list_of_string:
            print(row.strip())
        return


# Main Body of Script  ------------------------------------------------------ #

# Testing Exception Handling
while True:
    strFileName = IO.get_user_filename()    # Ask for name of data file for processing
    # Perform exception handling
    try:
        list_of_string = Processor.read_data_from_file(strFileName)
    except FileNotFoundError as error:     # handle non-existent file error
        print('Text file must exist before running this script!')
        print('Built-In Python error info: ')
        print(error, error.__doc__, type(error), sep='\n')
    else:   # If no exception, print out success of finding file
        print('File was found!\n')
        break

# Testing Pickling and Unpickling
strBinFileName = strFileName.replace('.txt', '.dat')    # make a name for the binary data file
Processor.pickle_it(strBinFileName, list_of_string)    # Pickle the data
list_of_string = Processor.unpickle_it(strBinFileName)     # Unpickle the data
IO.display_data(list_of_string)     # Display the un-pickled data to the user
