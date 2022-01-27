# my_dict = {"key":"This is the value", "key2":"This is another key"}



# # my_Dict = dict()
# a = {"key7":"This is the value", "key5":"This is another key"}


# my_dict.update(a)
# # print(my_dict.items())

# b = {('a_key', 'This is the value'), ('b_key2', 'This is another key'), ('key7', 'This is the value'), ('z_key5', 'This is another key')}

# b = dict(b)

# my_dict['key8'] = my_dict.pop("key7")


# print(my_dict)






##### conditionals


# if "ada" == "ada":
#     print("Correct")
# else:
#     print("Incorrect")


# user_data = {"desmond@univelcity.com":"Desmond Nnebue"}


# user_email = input("Enter your email:\n>").lower()

# if user_email.isspace() or user_email == "":
    
#     print("No entry")
# else:
#     if user_email in user_data.keys():
#         print("Account already exists")

#     else:
#         choice = input("Do you want to subscribe?(Y/y or N/n)\n>").lower()
        
#         if choice == 'y':
#             name = input("Enter your full name:\n>")
#             user_data[user_email] = name
#             print("successfully subscribed.")
            
#         elif choice == 'n':
#             print("Goodbye!")
        
#         else:
#             print("Invalid Input")
            

# print(user_data)



#### bank app v1
data = {
    "3947758475" : {
        "name":"Desmond",
        "dob": "09-09-09",
        "bvn": "123456789",
        "pin": "1234",
        "bal" : 120900
    },
    "3927758475" : {
        "name":"Ife",
        "dob": "09-09-79",
        "bvn": "123416789",
        "pin": "1214",
        "bal" : 12000
    },
}

print("Welcome to the AstroBank App")
print("Enter s to signup or l to login:")
choice = input(">").lower()

if choice == 'l':
    acc_num = input("Enter your account num:\n>")
    pin = input("Enter your pin:\n>")
    
    user = data.get(acc_num)
    
    if user and user['pin'] == pin:
        print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
    else:
        print("Invalid Login")