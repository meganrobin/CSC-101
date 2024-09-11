import math
def addition(first, second):
    return first + second
def subtraction(first, second):
    return first - second
def multiplication(first, second):
    return first * second
def division(first, second):
    return first / second
def floor_division(first, second):
    return first // second
def modulus(first, second):
    return first % second
def power(first, second):
    return first ** second
def log(first, second):
    return math.log(first, second)

def test_operations():
    #Test 1: addition function#
    assert addition(8,42) == 50, "Test 1 failed"
    #Test 2: subtraction function#
    assert subtraction(300,30) == 270, "Test 2 failed"
    #Test 3: multiplication function#
    assert multiplication(71,909) == 64539, "Test 3 failed"
    #Test 4: division function#
    assert division(30,6) == 5, "Test 4 failed"
    #Test 5: floor division function#
    assert floor_division(8,3) == 2, "Test 5 failed"
    #Test 6: modulus function#
    assert modulus(9,2) == 1, "Test 6 failed"
    #Test 7: power function#
    assert power(4,5) == 1024, "Test 7 failed"
    #Test 8: log function#
    assert log(100,10) == 2, "Test 8 failed"
    #Test 9: more log function#
    assert log(1,math.e) == 0, "Test 9 failed"

test_operations() #Runs the tests#
print("Enter the first number:")
first_number = int(input()) #turns the user's first input into an int and sets it equal to the var first_number#
print("Enter the second number:")
second_number = int(input()) #turns the user's second input into an int and sets it equal to the var second#
print("Choose an operation (addition, subtraction, multiplication, division, floor division, modulus, power, or log):")
operation = input() #sets the var operation equal to the user's choice of operation#
if operation == "addition": #if user chooses addition, calls the addition function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " + " + str(second_number) + " = " + str(addition(first_number, second_number)))
elif operation == "subtraction": #if user chooses subtraction, calls the subtraction function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " - " + str(second_number) + " = " + str(subtraction(first_number, second_number)))
elif operation == "multiplication": #if user chooses multiplication, calls the multiplication function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " x " + str(second_number) + " = " + str(multiplication(first_number, second_number)))
elif operation == "division": #if user chooses division, calls the division function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " / " + str(second_number) + " = " + str(division(first_number, second_number)))
elif operation == "floor division": #if user chooses floor division, calls the floor division function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " // " + str(second_number) + " = " + str(floor_division(first_number, second_number)))
elif operation == "modulus": #if user chooses modulus, calls the modulus function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " % " + str(second_number) + " = " + str(modulus(first_number, second_number)))
elif operation == "power": #if user chooses power, calls the power function and prints the result along with a visualization of the calculation#
    print(str(first_number) + " ** " + str(second_number) + " = " + str(power(first_number, second_number)))
elif operation == "log": #if user chooses log, calls the log function and prints the result along with a visualization of the calculation#
    print("log of " + str(first_number) + " with base " + str(second_number) + " = " + str(log(first_number, second_number)))