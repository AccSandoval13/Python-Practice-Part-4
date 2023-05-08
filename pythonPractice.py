# *! To check: python3 pythonPractice.py 

# Activity (Python Function Practice Part 4)

# 1. Write a function called max_num() to find the maximum of three numbers 
def max_num(num1, num2, num3): # Three parameters 

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
a = 13
b = 777
c = 18

max_value = max_num(a, b, c) # max_num function gets called and stored in max_value variable 
print("The maximum of", a, b, c, "is:", max_value) # Each argument is automatically converted to a string and concatenated together 



# 2. Write a Python function called mult_list() to multiply all the numbers in a list
def mult_list(list): 
    total = 1 # 1 x anything = anything 
    for num in list: # Iterate through the list, with a Python for loop  
        total *= num # Multiply each number in list by the total
    return total 

list = [13,16,2,7,9] 
print("The product of the numbers in this list", list, "is:", mult_list(list)) # mult_list function gets called and stored in total variable



# 3. Write a Python function called rev_string() to reverse a string 
def rev_string(string):
    return string[::-1] # String slicing and a step size of -1 to reverse the string or move backwards through the string

string = "Enter The Void"
print("The reverse of", string, "is:", rev_string(string)) # rev_string function gets called and stored in string variable



# 4. Write a Python function called num_within() to check whether a number is in a given range 
def num_within(num, low, high): # We want to check if num is in the range of low or high
    if num in range(low, high): # 
        return True # Return True
    else:
        return False
    
num = 3
low = 13
high = 777

print("Is", num, "in the range of", low, "and", high, "?", num_within(num, low, high)) # num_within function gets called and stored in num variable



# 5. Write a function called pascal() that prints out the first n rows of Pascal's triangle 
def pascal(n): # n is the number of rows 
    row = [1] # First row 
    y = [0] # Second row & its a 0 because we want to add the first row and second row together 
    for x in range(max(n,0)): # Iterate through the range of n
        print(row) # Print the first row
        row=[l+r for l,r in zip(row+y, y+row)] # A for loop to iterate through the list and zip() to iterate through the list and add the elements together
    return n>=1 # Return n>=1 bceause we want to print out the first n rows of Pascal's triangle 

n = 14
pascal(n) # Pascal's triangle an arithmetic and geometric figure first imagined by Blaise Pascal 

