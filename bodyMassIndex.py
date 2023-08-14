# this program will calculate the users body mass index (BMI)


#introduction to the program
print("""**** Body Mass Index Calculator ****""")
bmi = input("Would you like to calculate your BMI? (yes/no) >")

#program will perform questions and calculations if the answer is yes
if bmi == "yes":
    weight = int(input("What is your weight in pounds? (round to the nearest integer) >"))
    height = float(input("What is your height in inches? >"))

    # calculations
    # will create the square for the height
    def square(num):
        return num * num

    # will calculate the BMI
    heightSq = square(height)
    calculate = 703 * weight / heightSq

    print("Your BMI is: ", calculate)

#program will exit if the answer is no
else:
    exit()


#Repeats the program if the user would like to re-calculate their BMI
while True:
    repeat = input("Would you like to calculate your BMI again? (yes/no) >")
    if repeat == "yes":
        weight = int(input("What is your weight in pounds? (round to the nearest integer) >"))
        height = float(input("What is your height in inches? >"))
        def square(num):
            return num * num
        heightSq = square(height)
        calculate = 703 * weight / heightSq
        print("Your BMI is: ", calculate)
    else:
        exit()











