README

Grade Evaluation and Salary Calculation Program
This program is designed to perform three main functions:

Evaluate a student's grade based on their score.
Calculate the net salary of an employee based on their gross salary, PAYE, NHIF, and NSSF deductions.
Check a driver's speed and determine if they receive demerit points or a license suspension.
Requirements
Python 3.x
How to Use
Grade Evaluation

The program prompts the user to input a grade (0-100).
Based on the input, it prints the corresponding grade or an error message if the input is invalid.
Salary Calculation

The program prompts the user to input the basic salary and benefits.
It calculates the gross salary, PAYE, NHIF, NSSF deductions, and the net salary.
Finally, it prints the detailed salary breakdown.
Speed Check

The program prompts the user to input a speed.
It checks if the speed is within the limit and calculates demerit points or suspends the license based on the input.
Code Explanation
Grade Evaluation
Prompts the user to enter a grade. Validates the input range (0-100). Categorizes and prints the grade based on the input value.

Salary Calculation
Functions to calculate PAYE, NHIF, and NSSF based on the gross salary. The calculate_net_salary function computes the gross salary and all deductions, then returns the net salary. The user inputs the basic salary and benefits, and the program outputs the detailed salary breakdown.

Speed Check
The check_speed function evaluates the speed input against the speed limit. Calculates demerit points or determines if the license should be suspended based on the speed. Handles invalid input gracefully by prompting the user to enter a valid integer.