# PROJECT_10 project_10 is the driver function for the program.

# 	Name: Chris Chavez
# 	Date: 06 JULY 2021
# 	Class: CMPSC 132
# 	Description: Implement Monte Carlo Method to Integrate a function.
class Review_ValidateList:
	def __init__(self):
		self.sudoku_row = print(int(input("Please enter your Sudoku puzzle row for verification:  ")))

	def sudoku_row_input(sudoku_row):
			if ele in range (1, 10):
				sudoku_row.append(ele)
			else:
				print("Your input is not acceptable value.")

	def verify_sudoku_row_length(sudoku_row):
		# chekc if input is a list
		if not isinstance(sudoku_row, list): 
			print ("Input was not a list")

	def sudoku_row_length(sudoku_row):
		# List should contain 9 elements 
		if len(sudoku_row) < 9:
			print ("This Sudoku row does not contain enough digits")
		elif len(sudoku_row) > 9:
			print ("This Sudoku row contains to many digits")
		else: 
			return sudoku_row

	def value_repeated(): 

		# Iterate each row
		for ele in sudoku_row: 

			# Define array to append found numbers
			found = [] 

			# Iterate each number in the row
			for digit in row: 
				# Check if current value is already foudn 
				if digit not in found: 
					# Store found values 
					found.append(digit)
				else: 
					# Returns True if when it sees a repated number
					print("This Sudoku row is not valid, it has repeated values.")


Review_ValidateList()
