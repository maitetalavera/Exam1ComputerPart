###############################################################################
# DONE: 1. (3 pts)
#
#   In this module, we are going to create a program that will help the user
#   calculate how much they earned in week at work.
#
#   First, lets create a function that asks the user how many hours they
#   worked on a particular day.
#
#   Write a function called get_hours() that takes one parameter:
#       - day_of_week   <-- str
#
#   and prompts the user like so:
#
#       "How many hours did you work on <DAY_OF_WEEK>? "
#
#   The user should then enter a number.
#
#   The function should return that number as a float.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def get_hours(day_of_week):
    return float(input(f"How many hours did you work on {day_of_week}?"))

###############################################################################
# DONE: 2. (3 pts)
#
#   Now, write a function called calculate_hours() that takes 5 keyword
#   arguments:
#       - mon   <-- float
#       - tues  <-- float
#       - wed   <-- float
#       - thurs <-- float
#       - fri   <-- float
#
#   The function should total up all the hours and return the result.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def calculate_hours(mon, tues, wed, thurs, fri):
    return float(mon + tues + wed + thurs + fri)

###############################################################################
# DONE: 3. (3 pts)
#
#   Next, write a function called calculate_pay() that takes two parameters:
#       - total_hours   <-- float
#       - pay_rate      <-- float
#
#   The parameter total_hours is the total number of hours the user worked in a
#   week and the pay_rate parameters is the amount that the user is payed per
#   hour.
#
#   This function should calculate the total pay that the user will earn for
#   the week. You calculate this by multiplying the total number of hours by
#   the pay rate.
#
#   The function should then return that result.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def calculate(total_hours, pay_rate):
    result=float(total_hours * pay_rate)
    return result

###############################################################################
# TODO: 4. (9 pts)
#
#   Now, let's put it all together.
#
#   Write a function called main() that does these things in order (make sure
#   you use the functions you defined above and use f-strings in your
#   solution):
#
#       1. Prints "Let's calculate your pay!"
#       2. Asks the user to input how many hours they worked on Monday and
#          saves it to a variable.
#       3. Repeat step 2 for the rest of the days of the work week.
#       4. Calculates the total number of hours worked and saves it to a
#          variable. Make sure you use keyword arguments.
#       5. Asks the user to input how much they get paid per hour with this
#          prompt below (you do NOT need a separate function for this):
#
#           "How much are you currently paid per hour? "
#
#       6. Calculates how much the user should get paid for the week.
#       7. Prints a report of the user's hours and pay lik so:
#
#           Monday: 2 hour(s)
#           Tuesday: 4 hour(s)
#           Wednesday: 3 hour(s)
#           Thursday: 1 hour(s)
#           Friday: 0 hour(s)
#           Total Hours: 10 hour(s)
#           Pay Rate: $12.00 per hour
#           Total Pay: $120.00
#
#          Notice how the dollar amounts have two decimal places even when they
#          are zeros. You do NOT have to do this since we have not covered
#          this, but if you want to take a shot at it, take a look at the extra
#          credit below.
#
#   EXTRA CREDIT +2 pts: Try to see if you can get the dollar amounts above to
#   always have two decimals places. This is something we have not covered so
#   it will be extra credit. It might take some googling but take a stab at it
#   if you wish. Do NOT attempt this extra credit until you have everything
#   else from all the module completed and working!
#   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def main(): 
    print("Let's calculate your pay!")
    mon1=get_hours("Monday:")
    tues1=get_hours("Tuesday:")
    wed1=get_hours("Wednesday:")
    thurs1=get_hours("Thursday:")
    fri1=get_hours("Friday:")
    total_hours=calculate_hours(mon=mon1, tues=tues1, wed=wed1, thurs=thurs1, fri=fri1)
    pay_rate=float(input("How much are you currently getting paid per hour? "))
    total_pay= format(total_hours * pay_rate, "0.2f")

    print(f'Monday:{mon1} hour(s)')
    print(f'Tuesday:{tues1} hour(s)')
    print(f'Wednesday:{wed1} hour(s)')
    print(f'Thursday:{thurs1} hour(s)')
    print(f'Friday:{fri1} hour(s)')
    print(f'Total Hours:{total_hours} hour(s)')
    print(f'Pay Rate:${format(pay_rate,"0.2f")} per hour')
    print(f'Total Pay:${total_pay}')
    


main()




