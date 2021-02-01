# PROGRAM: Internet Service Subscription Pricing (CS-1110 Project 2)
# AUTHOR: Cameron Brenberger
# DESCRIPTION:
#       This program allows you to pick one of three internet service subscriptions
#           and asks for the amount of hours you desire each month.
#       The program will then tell you the amount per month for the subscription and then
#           compare the other subscriptions to see how much you would save with another option.
# DATA:
#       Package A: For $10.00 per month 10 hours of access are provided.
#           Additional hours or any fraction thereof are $2.50 per hour.
#       Package B: For $20.50 per month 20 hours of access are provided.
#           Additional hours or any fraction thereof are $2.00 per hour.
#       Package C: For $35.00 per month unlimited access is provided.

while True:
    plan_input = input("Enter your plan letter (A, B, or C): ")  # Asks input of plan A, B, or C

    plan_input_s = plan_input.strip()  # If there is any leading whitespaces, this will get ride of them
    char0 = plan_input_s[0]  # Grabs first letter of the input of plan_input
    cap_char = char0.upper()  # Coverts first letter of plan_input (if A(a), B(b), or C(c)) to always be uppercase
# ----------------------------------------------------------------------------------
    if cap_char == "A":
        while True:
            hours = input("Enter your number of hours: ")
            hours = float(hours)  # Converts str to float
            r_hours = round(hours)  # Rounds number

            pack_A = ((r_hours - 10) * 2.50) + 10
            pack_B = ((r_hours - 20) * 2) + 20.50
            pack_C = 35

            if r_hours <= 0:
                print("You entered an invalid number of hours.")
                continue
            else:
                print("Your usage charge is for", r_hours, "hours.")
                print("Your charges for Package A are $", "{:.2f}".format(pack_A), sep='')
                break

        if pack_A > pack_B and pack_A > pack_C:
            save_C = pack_A - pack_C
            save_B = pack_A - pack_B
            print("With package B you would have saved $", "{:.2f}".format(save_B), sep='')
            print("With package C you would have saved $", "{:.2f}".format(save_C), sep='')
        elif pack_A > pack_B:
            save_B = pack_A - pack_B
            print("With package B you would have saved $", "{:.2f}".format(save_B), sep='')
        elif pack_A > pack_C:
            save_C = pack_A - pack_C
            print("With package C you would have saved $", "{:.2f}".format(save_C), sep='')
        else:
            break

    elif cap_char == "B":
        while True:
            hours = input("Enter your number of hours: ")
            hours = float(hours)  # Converts str to float
            r_hours = round(hours)  # Rounds number

            pack_A = ((r_hours - 10) * 2.50) + 10
            pack_B = ((r_hours - 20) * 2) + 20.50
            pack_C = 35

            if r_hours <= 0:
                print("You entered an invalid number of hours.")
                continue
            else:
                print("Your usage charge is for", r_hours, "hours.")
                print("Your charges for Package B are $", "{:.2f}".format(pack_B), sep='')
                break

        if pack_B > pack_A and pack_B > pack_C:
            save_A = pack_B - pack_A
            save_C = pack_B - pack_C
            print("With package A you would have saved $", "{:.2f}".format(save_A), sep='')
            print("With package C you would have saved $", "{:.2f}".format(save_C), sep='')
        elif pack_B > pack_A:
            save_A = pack_B - pack_A
            print("With package A you would have saved $", "{:.2f}".format(save_A), sep='')
        elif pack_B > pack_C:
            save_C = pack_B - pack_C
            print("With package C you would have saved $", "{:.2f}".format(save_C), sep='')
        else:
            break

    elif cap_char == "C":
        while True:
            hours = input("Enter your number of hours: ")
            hours = float(hours)  # Converts str to float
            r_hours = round(hours)  # Rounds number

            pack_A = ((r_hours - 10) * 2.50) + 10
            pack_B = ((r_hours - 20) * 2) + 20.50
            pack_C = 35

            if r_hours <= 0:
                print("You entered an invalid number of hours.")
                continue
            else:
                print("Your usage charge is for", r_hours, "hours.")
                print("Your charges for Package C are $", "{:.2f}".format(pack_C), sep='')
                break

        if pack_C > pack_A and pack_C > pack_B:
            save_A = pack_C - pack_A
            save_B = pack_C - pack_B
            print("With package A you would have saved $", "{:.2f}".format(save_A), sep='')
            print("With package B you would have saved $", "{:.2f}".format(save_B), sep='')
        elif pack_C > pack_A:
            save_A = pack_B - pack_A
            print("With package A you would have saved $", "{:.2f}".format(save_A), sep='')
        elif pack_C > pack_B:
            save_B = pack_C - pack_B
            print("With package B you would have saved $", "{:.2f}".format(save_B), sep='')
        else:
            break

    else:
        print("You entered an invalid plan code", plan_input, end=".")
        print("\t")
        continue
# ---------------------------------------------------------------------------------------
    print("\t")
    an_package = input("Do you want to enter another package?")

    char1 = an_package[0]  # Grabs first letter of input an_package
    cap_an_package = char1.upper()  # Converts first letter of input an_package to uppercase
    if cap_an_package == "Y":  # If input first letter equals Y,
        print("\t")            # prints a new line,
        continue               # starts program over.
    else:
        exit()  # Closes/Ends program
