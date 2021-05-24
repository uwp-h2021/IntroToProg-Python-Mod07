# Exception Handling and Pickling
**Dev.** *HJong*  
**Date:** *5/24/2021*
## Introduction
This report documents a research results on exception handling and pickling.  It also describes a Python script I created that demonstrates my learning.  It contains three main sections (excluding this introduction):
1)	Exception Handling Research;
2)	Pickling Research;
3)	Exception and Pickling Script;
4)	GitHub webpage;
5)	Summary
## The Exception Handling
## The Pickling
## The Exception Handling and Pickling Script
### Script Planning
In this script, I am demonstrating exception handling and data pickling work.   The following is the steps I took and have implemented in the code:
1)	Create a text data file that contains multiple lines of string (outside of the script).  The data file name is “DataFile.txt”, and the content is shown in Figure 9.
2)	Ask the user to enter the text file name for pickling.  Handle the exception when the file name does not exist using try-except block.
3)	Read the data from the text file and add it into a list of strings.
4)	Write the list of strings into a binary file using pickle.dump() method
5)	Read the pickled data from the binary file back into a list of strings using pickle.load() method
6)	Print the list of strings to the user

![The "DataFile.txt" with its Content](https://github.com/uwp-h2021/IntroToProg-Python-Mod07/blob/main/docs/FIgure%209.png "The DataFile.txt with Its Content")
#### Figure 9 The "DataFile.txt" with Its Content
### Writing the Script in Pycharm
Following the steps in the planning, the script was completed with its various sections described in detail as follows.

```
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
```
### Executing the Script in Pycharm
The script in performing the exception handling and pickling actions in demonstrated in this section.  I tested the exception handling by entering a non-existing file name, then an existing file name without extension, both of which were handled by putting out the error message.  The script kept asking the user for an existing text file name until no exception was captured.  The data from the original text file “DataFile.txt” were read, written into a binary file, and read back into memory, and finally displayed to the user to verify the process was done correctly.  The binary file name “DataFile.dat” was the same name as the original text file except that its extension was “.dat”.  The run results are shown in Figure 15.

![Run Results in PyCharm](https://github.com/uwp-h2021/IntroToProg-Python-Mod07/blob/main/docs/Figure%2015.png "Run Results in PyCharm")
#### Figure 15  Run Results in PyCharm
### Checking the Binary Data File After PyCharm Run
After the run in PyCharm, I opened “DataFile.dat” to verify the binary data were created as intended, which is shown in Figure 16.

![Binary Data in "DataFile.dat" After Run in PyCharm](https://github.com/uwp-h2021/IntroToProg-Python-Mod07/blob/main/docs/Figure%2016.png "Binary Data in DataFile.dat After Run in PyCharm")
#### Figure 16  Binary Data in "DataFile.dat" After Run in PyCharm
### Executing the Script in Windows Command
Same steps as the PyCharm run were followed in the Windows command run, and the results are shown in the screenshot in Figure 17.  
![Run Results in Windows Command Prompt] (https://github.com/uwp-h2021/IntroToProg-Python-Mod07/blob/main/docs/Figure%2017.png "Run Results in Windows Command")
#### Figure 17  Run Results in Windows Command

### Checking the Binary Data File After Windows Command Run
After the run in Windows command, the “DataFile.dat” was opened again to verify the binary data were created as intended, which is shown in Figure 18.

## Summary
