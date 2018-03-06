#-------------------------------------------------------------------------------
# Name:        count_evens.py
# Purpose:  This program is designed to use recursion to count the number of
#           even numbers are read from a file. This sequence is stored in a
#           linked list.
#
# Created:     08/10/2014
# Updated:     03/06/2018 Converted to Python 3 and made other small improvements
#-------------------------------------------------------------------------------

from LList import LList

# recursive function to count the number of even numbers in this linked list.
def count_evens(currentNode):
    if(currentNode == None):
        return 0
    else:
        if( currentNode.item % 2 == 0 ):
            return 1 + count_evens( currentNode.link )
        else:
            return count_evens( currentNode.link )

def read_numbers_return_list(verbose):
    '''preconditions: none
    postconditions: the numbers in the file with the name asked by the user will
        be placed into a linked list and returned.'''
    filename = input("What is the name of the file? ")

    file = open(filename, "r")

    # get the list of strings from the file. This list will need to be converted to
    # a list of numbers in a
    stringList = file.read().split()
    file.close()

    # time to create an integer version of the numbers list
    numberList = []
    for item in stringList:
        if verbose:
            print(item)
        numberList.append(int(item))

    # Now create a linked list version of this number sequence
    created_list = LList(numberList)
    return created_list

def main():

    numbersList = read_numbers_return_list(True)
    print("There are " + str(count_evens( numbersList.head)) + " even numbers in the list." )

if __name__ == '__main__':
    main()
