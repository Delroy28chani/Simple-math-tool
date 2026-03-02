print("---Simple Math Tool ---")
while True:
#1. Get raw inputs as a string first
  choice1 = input("Enter first number (or 'q' to quit)")
  if choice1 == "q":
      break
  num1 = float(choice1)
  num2 = float(input("Enter second number: "))

#2. Ask what they want do
operation = input("Type + to add or - to subtract: ")

# Exit the loop if the user types "q"
if operation == "q":
    print("Goodbye!")
    exit()

#3 Use Logic (IF/ELSE) to decide the result
if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 !=0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error cannot divide by zero!")
else:
    print("Invalid operation! Please type +, - , / or *.")
    print("_" * 25) # just a separator calculations 