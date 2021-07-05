# PROJECT_10 project_10 is the driver function for the program.

# 	Name: Chris Chavez
# 	Date: 06 JULY 2021
# 	Class: CMPSC 132
# 	Description: Implement Monte Carlo Method to Integrate a function.



sudoku_row = []
int(input("Please enter your Sudoku puzzle row for verification:  "))

for i in range(1, 10):
	ele = int(input())

	sudoku_row.append(ele)


def verify_board(sudoku_row):

	# chekc if input is a list
	if not isinstance(sudoku, list): 
		return False

	# List should contain 9 elements 
	if len(sudoku) != 9:
		return ("List does not contain enough digits")

	for row in sudoku:

	# Check if rows are strings or lists
		if not isinstance (row, (list, string)):
			return False

	# The length of both lists and sgtrings must equal 9
	# Use the join method to compare both strings and lists 
	text = ''.join(row)
	if len(text) != 9:
		return False

	# Finally, check if row is digits-only
	if not text.isdigit():
		return False 

# Else, return True
	return True

