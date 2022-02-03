# import random



# data = {
#     "3947758475" : {
#         "name":"Desmond",
#         "dob": "09-09-09",
#         "bvn": "123456789",
#         "pin": "1234",
#         "bal" : 120900
#     },
#     "3927758475" : {
#         "name":"Ife",
#         "dob": "09-09-79",
#         "bvn": "123416789",
#         "pin": "1214",
#         "bal" : 12000
#     },
# }

# print("Welcome to the AstroBank App")
# print("Enter s to signup or l to login:")
# choice = input(">").lower()

# if choice == 'l':
#     acc_num = input("Enter your account num:\n>")
#     pin = input("Enter your pin:\n>")
    
#     user = data.get(acc_num)
    
#     if user and user['pin'] == pin:
#         print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
        
#         print("""\nWhat would you like to do?
#               Press 1 to withdraw
#               Press 2 to deposit
#               Press any other key to quit.""")
        
#         user_input = input(">")
        
#         if user_input == '1':
#             amount = int(input("How much?\n>"))
#             if amount >= user['bal']:
#                 print("Insufficient Funds")
#             else:
#                 user['bal']-=amount
#                 print("Please take your cash")
#                 print(f"Balance is {user['bal']}")
                
#         elif user_input == '2':
#             amount = int(input("How much?\n>"))
            
#             user['bal']+=amount
#             print("Successful")
#             print(f"Balance is {user['bal']}")
#         else:
#             print("Good bye")
#     else:
#         print("Invalid Login")
        
# elif choice == 's':
#     name = input("Enter your name:\n>")
#     dob= input("Enter your date of birth:\n>")
#     bvn= input("Enter your BVN:\n>")
#     pin = input("Enter your PIN:\n>")
#     details = [('name', name), 
#                ('dob', dob), 
#                ('bvn', bvn), 
#                ('pin', pin), 
#                ('bal',0) 
#             ]
    
#     #generate account number
#     num = [1,2,3,4,5,6,7,8,9,0]
#     acc_num_list = [str(random.choice(num)) for _ in range(10)]
    
    
#     acc_num = "".join(acc_num_list)
    
#     data[acc_num] = dict(details)

# else:
#     print("Invalid input")
    


# # print(data)
# # import random
# # num = [1,2,3,4,5,6,7,8,9,0]
# # print(random.choice(num))
# # # print(num)




import random
num = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(num)


trial = 3
score = 0 

while trial != 0:
    
    choice = random.choice(num)
    play = int(input('Enter your number\n>'))
    
    if play == choice:
        trial +=1
        score+=3
        print("Correct!")
        print("You have been given an extra trial")
        print("Yayyy! 🎉🥳")
    else:
        trial -=1
        print("Incorrect!")
        print(f"You have {trial} trail(s) left")
    
    print(choice)