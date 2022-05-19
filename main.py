# Juan José Montaño, 8B, May 9th  2022


#Imports
from time import sleep
from os import system

op = "y" # Defining the variable op, that will be used later on

def monthly_salary(pay, unit): # declaration of the function
  system("clear")

  ## [Getting the name and how many hours has the employee worked trough input]
  name = input("What's the employee's name? ") 
  hpw = input("How many hours does the employee work per week? ")

  try:
  ## [Setting hpw variable (hours per week) as a float]
    hpw = float(hpw)
  except ValueError:
    print("That's not a number!")
    return "Errors occurred"

  ## [As a month has 4 weeks, multiplying the hours per week by 4, and then by the amount paid for each one (hours_per_month*pay)]
  monthly_salary = str((hpw*4)*pay)

  
  print("")

  ## [The final output]
  return "The employee "+name+" must recieve "+monthly_salary+" "+unit+" per month."
  ############################################################## end of the function


## [Getting the payment unit and the amount paid for each hour of work]
unit = input("In wich unit should the salary of the employees measured? ")
pay = input("How much should each employee recieve per hour? ")
try:
  pay = float(pay)
except ValueError:
  print("That's not a number!")
  exit("Errors occured")

## [Until op variable's value isn't "y" string]
while op[0 : 1].lower() == "y": # lower in case you forget the caps lock
  # do
  print(monthly_salary(pay, unit)) ## returns the final output
  ## Here, op's value will be changed. The progam only checks if op is an empty string; If not, it will call again monthly_salary function and ask for changing op's value until it is an empty string
  print("Enter to continue")
  i=input()
  system("clear")
  print(" Do you want to calculate another employee's salary? (yes/no) [y/anything else]: ")
  op = input("-> ")