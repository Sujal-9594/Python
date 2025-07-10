ASSIGNMENT 3 : Task 1 and 2 
Task1 Program: Factorial Using Recursion

This Python program calculates the factorial of a number using a function and a technique called recursion.

🔹 What is a Factorial?
- The factorial of a number is the result of multiplying that number by every whole number below it down to 1.
- Example: 
  5! = 5 × 4 × 3 × 2 × 1 = 120

🔹 How the Program Works:

1. The program defines a function named `factorial(n)`.
   - If the number is less than 2 (i.e., 0 or 1), it returns 1. This is the **base case**.
   - If the number is 2 or more, it returns `n * factorial(n - 1)`. 
     This is the **recursive case**, where the function keeps calling itself with smaller values of `n`.

2. The user is asked to enter a number using `input()`.

3. The entered number is converted to an integer and stored in the variable `num`.

4. The program then calls the `factorial()` function with this number.

5. Finally, it prints the result in this format:
   `Factorial of 5 is :120`

🔹 Example:
If the user enters 4, the function works like this:
- factorial(4) = 4 * factorial(3)
- factorial(3) = 3 * factorial(2)
- factorial(2) = 2 * factorial(1)
- factorial(1) = 1 (base case)

Now it calculates:
4 × 3 × 2 × 1 = 24

So the output will be:
Factorial of 4 is :24 



Task2 : Using Math Functions in Python

This program takes a number from the user and performs three mathematical operations using Python’s built-in math module:

1. Square Root
2. Natural Logarithm
3. Sine Value (in radians)

---

🔹 Step-by-Step Functionality:

1.  User Input:
   - The program asks the user to enter a number.
   - The input is taken as a decimal number (float).

2.  Math Module:
   - The program uses `from math import *` to access math functions like `sqrt()`, `log()`, and `sin()`.

3.  Square Root:
   - It calculates the square root using `sqrt(num)`.
   - Example: If num = 16 → sqrt(16) = 4.0

4.  Natural Logarithm:
   - It calculates the natural logarithm (log base **e**) using `log(num)`.
   - Example: If num = 10 → log(10) ≈ 2.302

5.  Sine Value:
   - It calculates the sine of the number (in **radians**) using `sin(num)`.
   - Example: If num = π/2 → sin(π/2) = 1

6.  Output:
   - The program prints all three results in a clean, readable format.









