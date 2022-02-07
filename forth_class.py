import random
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
# Your task is to complete the signup, withdrawal and deposit features.
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
DATA = {
    "0947493434" : [ 
                                 { "amount" : 1000,
                                "type" : "credit",
                                 "action" : "deposit"
                               },
                               { "amount" : 1500,
                                "type" : "debit",
                                 "action" : "withdraw"
                               },
               ]
}
print("Welcome to the AstroBank App")
print("Enter s to signup or l to login:")
choice = input(">").lower()

if choice == 'l':
    acc_num = input("Enter your account num: \n>")
    pin = input("Enter your pin: \n>")
    
    user = data.get(acc_num)
    
    if user and user['pin'] == pin:
        print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
        print("Enter d to Deposit or w to Withdraw or t to transfer or q to quit:")
        choice_2 = input(">").lower()
       
        if choice_2 == "d":
            acc_num_1 = input("Enter your account num: \n>")
            pin_1 = input("Enter your pin: \n>")
            
            user_1 = data.get(acc_num_1)
            
            if user_1 and user_1['pin'] == pin_1:
                print(f"Welcome {user_1['name']}.\nYour account balance is ${user_1['bal']}")
                dep_amount_1 = input("Enter Deposit amount: \n>") 
                dep_amount_1= int(dep_amount_1)
                user_1["bal"] += dep_amount_1
                DATA[acc_num_1]= [{ "amount" : dep_amount_1,
                                "type" : "credit",
                                 "action" : "deposit"
                               }]
                print(user_1)
                print(DATA)

            else:
                print("Invalid Login") 
                # print("4 more tries")
           
        elif choice_2 == "w":  
              acc_num_4 = input("Enter your account num\n>")
              pin_4 = input("Enter your pin:\n>")
            
              user_4 = data.get(acc_num_4)
            
              if user_4 and user_4['pin'] == pin_4:
                print(f"Welcome {user_4['name']}.\nYour account balance is ${user_4['bal']}")
                withdrawal_amount = input("Enter Withdrawal amount: \n>") 
                withdrawal_amount = int(withdrawal_amount)
                user_4["bal"] -= withdrawal_amount
                DATA[acc_num_4]= [{ "amount" : withdrawal_amount,
                                "type" : "debit",
                                 "action" : "withdrawal"
                               }]
                print(user_4)
                print(DATA)
              else:
                print("Invalid Login") 
                # print("4 more tries")
        elif choice_2 == "t":  
              acc_num_5 = input("Enter account num to debit\n>")
              tr_acc_num_5 = input("Enter account num to credit\n>")
            #   tr_acc_num_5= int(tr_acc_num_5)
              pin_5 = input("Enter your pin:\n>")
            
              user_5 = data.get(acc_num_5)
              tr_user_5 = data.get(tr_acc_num_5)
              if user_5 and user_5['pin'] == pin_5 and tr_acc_num_5 in data:
                print(f"Welcome {user_5['name']}.\nYour account balance is ${user_5['bal']}")
                tr_amount = input("Enter transfer amount: \n>") 
                tr_amount = int(tr_amount)
                user_5["bal"] -= tr_amount
                tr_user_5['bal'] += tr_amount
                DATA[acc_num_5]= [{ "amount" : tr_amount,
                                "type" : "debit",
                                 "action" : "transfer"
                               }]
                print(user_5)
                print(DATA)
                print(tr_user_5)
              else:
                print("Invalid Login") 
                # print("4 more tries")

        if choice_2 == "q":  
           print("Goodbye from Astroverse Bank")
    else:
        print("Invalid Login")
# Sign-up or Registration Process Algorithm -#1
elif choice == 's':
    user_name = input("Enter your full name:\n>").lower()
    user_dob = input("Enter your dob mm-dd-yyyy:\n>").lower()
    user_bvn = input("Enter your BVN :\n>").lower()
    # user_bvn = int(user_bvn)
    user_pin = input("Enter your 4 Digit PIN :\n>").lower()
    # user_pin = int(user_pin)
    
    if type(user_name) == type("String") and type(user_dob) == type("String") and type(user_bvn) == type("String") and len(user_bvn) == 10 and type(user_pin) == type("String") and len(user_pin) == 4:
    
       acct_data = {}
       acct_data["name"]= user_name
       acct_data["dob"] = user_dob
       acct_data["bvn"] = user_bvn
       acct_data["pin"] = user_pin
       acct_data["bal"] = 0
       user_acct_num = random.randrange(1111111111,9999999999)
       user_acct_num = str(user_acct_num)
       new_acct = {}
      #  new_acct[user_acct_num] = acct_data
       data.update(new_acct)

       
       print(f"Congratulations!, {acct_data['name']} You now have an accont on Astroverse Bank App and you account number is \n>")
       print(list(data.keys())[-1])
       new_user_tr_data = {}
       
       print("Enter d to Deposit or q to quit:")
       choice_2 = input(">").lower()
       
       if choice_2 == "d":
            acc_num_2 = input("Enter your account num: \n>")
            pin_2 = input("Enter your pin: \n>")
            # pin_2 = int(pin_2)
            user_2 = data.get(acc_num_2)
            
            if user_2 and user_2['pin'] == pin_2:
                print(f"Welcome {user_2['name']}.\nYour account balance is ${user_2['bal']}")
                dep_amount = input("Enter Deposit amount: \n>") 
                dep_amount= int(dep_amount)
                user_2["bal"] += dep_amount
                DATA[acc_num_2]= [{ "amount" : dep_amount,
                                "type" : "credit",
                                 "action" : "deposit"
                               }]
                print(user_2)
                print(DATA)
                print("Enter w to withdraw , t to transfer or q to quit \n>")
                choice_3 = input(">").lower()
                if choice_3 == "w":  
                  acc_num_3 = input("Enter your account num\n>")
                  pin_3 = input("Enter your pin:\n>")
            #   pin_3 = int(pin_3)
                  user_3 = data.get(acc_num_3)
            
                  if user_3 and user_3['pin'] == pin_3:
                    print(f"Welcome {user_3['name']}.\nYour account balance is ${user_3['bal']}")
                    withdrawal_amount = input("Enter Withdrawal amount: \n>") 
                    withdrawal_amount = int(withdrawal_amount)
                    user_3["bal"] -= withdrawal_amount
                    print(user_3)
                    DATA[acc_num_3]= [{ "amount" : withdrawal_amount,
                                "type" : "debit",
                                 "action" : "withdrawal"
                               }]
                elif choice_3 == "t":    
                    acc_num_3 = input("Enter account num to debit\n>")
                    tr_acc_num_3 = input("Enter account num to credit\n>")
                    #   tr_acc_num_5= int(tr_acc_num_5)
                    pin_3 = input("Enter your pin:\n>")
                    
                    user_3 = data.get(acc_num_3)
                    tr_user_3 = data.get(tr_acc_num_3)
                    if user_3 and user_3['pin'] == pin_3 and tr_acc_num_3 in data:
                        print(f"Welcome {user_3['name']}.\nYour account balance is ${user_3['bal']}")
                        tr_amount = input("Enter transfer amount: \n>") 
                        tr_amount = int(tr_amount)
                        user_3["bal"] -= tr_amount
                        tr_user_3['bal'] += tr_amount
                        DATA[acc_num_3]= [{ "amount" : tr_amount,
                                        "type" : "debit",
                                        "action" : "transfer"
                                    }]
                        print(user_3)
                        print(DATA)       
                    else:
                        print("Invalid Login") 
                        # print("4 more tries")
       elif choice_2 == "q": 
         print("Goodbye from Astroverse Bank")  
             
             
           
           
       
        
else:
        print("Invalid data") 

