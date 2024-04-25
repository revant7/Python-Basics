user_input = str(input("Select an Operator: [/,*,+,-] : "))
first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))


if user_input == '/':
    result = first_num / second_num
    print("Your Result is :",result)

elif user_input == '*':
    result = first_num * second_num
    print("Your Result is :",result)

elif user_input == '+':
    result = first_num + second_num
    print("Your Result is :",result)

elif user_input == '-':
    result = first_num - second_num
    print("Your Result is :",result)

else:
    print("Please Write a Valid Input")
