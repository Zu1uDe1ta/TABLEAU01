#   Name: Chris Chavez
#   Date: 06 JULY 2021
#   Class: CMPSC 132
#   Description: Sudoku Row Verifier.




def verify_row():
  sudoku = []
  print("Enter 9 numbers from 1 to 9 to make a sudoku row,\n we will verify that your row is a proper sudoku row. \n")
  for i in range(0, 9):
   print("Enter 1 digit at a time and press enter.".format(i+1))
   elm = int(input())
   sudoku.append(elm) # adding the element
  print("The entered list is: \n",sudoku)

  # Row should contain 9 elements
  if len(sudoku) != 9: 
    print("Row does not have 9 numbers")

  found = []        
  # Iterate each number in the row
  for digit in sudoku:            
      # Check if current value is already found 
    if digit not in found:
                # Store found values
      found.append(digit)            
    else:                 
        # Returns True if when it sees a repeated number
      print("You have a repeat digit in your row!") 
  # If there were not repeated numbers, return False
  print("It is a valid row!")

