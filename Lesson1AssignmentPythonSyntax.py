#1. Showcase Your Dance Moves!

#Task 1: Code correction
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2: Your Mood Today
mood = input("How are you feeling today: ")
mood.lower

if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I hope your day gets better!")

#Task 3: Spotting Indentation Errors
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!") 



#2. Python Comments & Multi-line Practice
    
#Task 1: Create a Poem using Comments
# Python, oh Python, so clear and so neat
# With every new challenge, you're hard to beat.
# Comments are nice to keep code clean.
# They keep you informed, no comments are mean.
    
#Task 2: Multi-line Poem
print('''Python, in the realm of code you shine,
With simplicity and grace, you're truly divine.
Writing this code fills me with glee.
Multi-line poems making coding feel free.
''')

#Task 3: Combining Single and Multi-line Comments

#This is from single line
# Comments are nice to keep code clean.

#This line is from multi-line
print('''Multi-line poems making coding feel free.''')


#3. Python Naming Convention Practice

#Task 1: Code Correction
PI = 3.14
userAge = 25
userLocation = "New York"
MAXLIMIT = 1000

#Python Data Types and type() Function
#Task 1: Code Correction
#String
variable_a = "Hello, World!"
#int
variable_b = 23
#float
variable_c = 3.14
#bool
variable_d = True
print(type(variable_a))
print(type(variable_b))
print(type(variable_c))
print(type(variable_d))


#4. Python Dynamic Typing Practice

#Task 1: Code Correction
dynamic_variable = "This is a string"
# (Your code to print the type of dynamic_variable here)
print(type(dynamic_variable))

dynamic_variable = 100
# (Your code to print the type of dynamic_variable here)
print(type(dynamic_variable))

dynamic_variable = 25.5
# (Your code to print the type of dynamic_variable here)
print(type(dynamic_variable))


#5. Arithmetic Operations in Daily Life

# Task 1: Grocery Store Math
# Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices.
banana_price = 3
apple_price = 2.5
grape_price = 4.5
total = banana_price + apple_price + grape_price
str(total)

print("Your total is: ", '$', total)

# Task 2: Bank Interest
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year.
initial_amount = 2100
interest = 0.05
amount_after_interest = initial_amount*interest + initial_amount
str(amount_after_interest)
str(initial_amount)
print("After depositing $", initial_amount, " you will have $", amount_after_interest, " at the end of the year.")

# Task 3: Area and Perimeter
# Given the length and width of a rectangle, compute both its area and perimeter using arithmetic operators.
length = 7
width = 5
area = length*width
perimeter = length*2 + width*2
str(perimeter)
str(area)
str(length)
str(width)
print("Length: ", length, "\nWidth: ", width, "\nPerimeter: ", perimeter, "\nArea: ", area)

#6. Understanding Assignments and Comparisons

# Task 1: Value Swapping
# Swap the values of two given numbers using assignment operators and then compare them to ensure they have been swapped.
a = 1
b = 2
a = 2
b = 1
compare = a == 2 and b == 1
print(f"Were values swapped: {compare}")


# Task 2: Perfect Square Checker
# Given a number, determine if it's a perfect square (like 1, 4, 9, 16, …). Hint: You might need the exponentiation operator for this.
sqrt_checker = input("Enter a number to see if it is a perfect square: ")
sqrt_checker = int(sqrt_checker)
i = 1

isSquareRoot = False
while i**2 <= sqrt_checker:
    if i**2 == sqrt_checker:
        isSquareRoot = True
        break
    else:
        i += 1

print(f"{isSquareRoot}")


#7. Exploring Logical Operations and Precedence

# Task 1: Simple Logic Puzzles
# Given a set of True or False values, use the AND, OR, and NOT operators to come up with a desired True or False outcome.
myTrue = True
myFalse = False

#returns/prints the opposite
myNotTrue = not myTrue
myNotFalse = not myFalse

#returns true because of or statement
print(f"{myFalse and myNotFalse or myTrue}")

#return false because both not true
print(f"{myFalse and myNotFalse}")

#return false because both false
print(f"{myFalse and myNotTrue}")

# Task 2: Validating Calculations
# Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.
no_parentheses = 1 + 2 * 3
with_paentheses = (1+2)*3

#should print false no_parentheses = 7 and with_parentheses = 9
print(f"{no_parentheses == with_paentheses}")


# Task 3: Mix and Match
# Combine arithmetic, logical, and comparison operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.
collection_of_operators = 1 + 2 == 2 + 3 < 2 - 4
print(collection_of_operators)