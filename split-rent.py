"""
This program calculates how to split rent fairly based on a given person's income.
It incorporates some basic error handling and calculations for up to 4 people.
"""
def main():
    print("This program calculates rent fairly based on income 💸.")
    print()
    num_of_other_people = inputNumber("How many other people do you split rent with 🔢? ")
    print()
    if int(num_of_other_people) == 1:
        calculation_1()
    elif int(num_of_other_people) == 2:
        calculation_2()
    elif int(num_of_other_people) == 3:
        calculation_3()
    else:
        print("I'm sorry - I'm a bit of an introvert so I work best splitting rent with up to 3 people 😅.")
        try_again = str(input("Would you like to try again? (y/n) "))
        if try_again == "y":
            main()
        else:
            print()
            print("See you later! 👋")

def calculation_1():
        name_a = input("What's your name? ")
        income_a = inputNumber("Please enter your monthly income, " + name_a + ": ")
        print()
        name_b = input("What's your roommate's name? ")
        income_b = inputNumber("Please enter " + name_b + "'s monthly income: ")
        print()
        monthly_rent = inputNumber("Please enter your monthly total rent: ")
        # calculating % of total
        total_income = int(income_a) + int(income_b)
        percentage_a = int(income_a) / total_income
        percentage_b = int(income_b) / total_income
        a_amount = percentage_a * int(monthly_rent)
        b_amount = percentage_b * int(monthly_rent)
        percent_of_income = a_amount / income_a
        # print the final amounts
        print()
        print("------")
        print("1️⃣: " + name_a + " should pay " + str(int(a_amount)) + " per month.")
        print("2️⃣: " + name_b + " should pay " + str(int(b_amount)) + " per month.")
        print()
        print("This represents " + "{:.1f}".format(percent_of_income * 100) + "% of each person's income.")
        print()
        print("Thanks for using my rent splitter 🎉!")
        print()
        try_again = str(input("Would you like to try again? (y/n) "))
        if try_again == "y":
            main()
        else:
            print()
            print("See you later! 👋")

def calculation_2():
        name_a = input("What's your name? ")
        income_a = inputNumber("Please enter your monthly income, " + name_a + ": ")
        print()
        name_b = input("What's your first roommate's name? ")
        income_b = inputNumber("Please enter " + name_b + "'s monthly income: ")
        print()
        name_c = input("What's your second roommate's name? ")
        income_c = inputNumber("Please enter " + name_c + "'s monthly income: ")
        print()
        monthly_rent = inputNumber("Please enter your monthly total rent: ")
        # calculating % of total
        total_income = int(income_a) + int(income_b) + int(income_c)
        percentage_a = int(income_a) / total_income
        percentage_b = int(income_b) / total_income
        percentage_c = int(income_c) / total_income
        a_amount = percentage_a * int(monthly_rent)
        b_amount = percentage_b * int(monthly_rent)
        c_amount = percentage_c * int(monthly_rent)
        percent_of_income = a_amount / income_a
        # print the final amounts
        print()
        print("------")
        print("1️⃣: " + name_a + " should pay " + str(int(a_amount)) + " per month.")
        print("2️⃣: " + name_b + " should pay " + str(int(b_amount)) + " per month.")
        print("3️⃣: " + name_c + " should pay " + str(int(c_amount)) + " per month.")
        print()
        print("This represents " + "{:.1f}".format(percent_of_income * 100) + "% of each person's income.")
        print()
        print("Thanks for using my rent splitter 🎉!")
        print()
        try_again = str(input("Would you like to try again? (y/n) "))
        if try_again == "y":
            main()
        else:
            print()
            print("See you later! 👋")

def calculation_3():
        name_a = input("What's your name? ")
        income_a = inputNumber("Please enter your monthly income, " + name_a + ": ")
        print()
        name_b = input("What's your first roommate's name? ")
        income_b = inputNumber("Please enter " + name_b + "'s monthly income: ")
        print()
        name_c = input("What's your second roommate's name? ")
        income_c = inputNumber("Please enter " + name_c + "'s monthly income: ")
        print()
        name_d = input("What's your third roommate's name? ")
        income_d = inputNumber("Please enter " + name_d + "'s monthly income: ")
        print()
        monthly_rent = inputNumber("Please enter your monthly total rent: ")
        # calculating % of total
        total_income = int(income_a) + int(income_b) + int(income_c) + int(income_d)
        percentage_a = int(income_a) / total_income
        percentage_b = int(income_b) / total_income
        percentage_c = int(income_c) / total_income
        percentage_d = int(income_d) / total_income
        a_amount = percentage_a * int(monthly_rent)
        b_amount = percentage_b * int(monthly_rent)
        c_amount = percentage_c * int(monthly_rent)
        d_amount = percentage_d * int(monthly_rent)
        percent_of_income = a_amount / income_a
        # print the final amounts
        print()
        print("------")
        print("1️⃣: " + name_a + " should pay " + str(int(a_amount)) + " per month.")
        print("2️⃣: " + name_b + " should pay " + str(int(b_amount)) + " per month.")
        print("3️⃣: " + name_c + " should pay " + str(int(c_amount)) + " per month.")
        print("4️⃣: " + name_d + " should pay " + str(int(d_amount)) + " per month.")
        print()
        print("This represents " + "{:.1f}".format(percent_of_income * 100) + "% of each person's income.")
        print()
        print("Thanks for using my rent splitter 🎉!")
        print()
        try_again = str(input("Would you like to try again? (y/n) "))
        if try_again == "y":
            main()
        else:
            print()
            print("See you later! 👋")

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print(">>> Oops! Please enter a whole (or rounded) number instead.")
       print()
       continue
    else:
       return userInput 
       break

def inputSting(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print(">>> Oops! Please enter a whole (or rounded) number instead.")
       print()
       continue
    else:
       return userInput 
       break 

if __name__ == '__main__':
    main()
