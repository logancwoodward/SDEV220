"""Logan Woodward
SDEV220
4/1/24
M02 Lab Case Study"""
#initiate loop to collect student names
while True:
    last_name = input("Enter student's last name (enter 'ZZZ' to quit): ") #get last name
    if last_name == 'ZZZ':
        break #stop asking for names if 'ZZZ' is entered for a last name
    first_name = input("Enter student's first name: ") #get first name
    gpa = float(input("Enter student's GPA: ")) #get gpa
    if gpa >= 3.5: #Dean's list
        print("Congratulations! You've made the Dean's List.")
    if gpa >= 3.25: #Honor Roll
        print("Congratulations! You've made the Honor Roll.")