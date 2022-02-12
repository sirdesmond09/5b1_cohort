
import string
import random
# def is_odd(n):
#     return n%2!=0


# def is_odd(n):
#     if n%2==0:
#         return False
#     else:
#         return True
    


# a = is_odd(5)
# print(a)

def is_prime(n):
    if n == 1:
        return False
    
    if n == 2:
        return True
    
    if n>2 and n % 2 == 0:
        return False
    
    square_root = int(n**0.5)
    for i in range(2, square_root + 1):    
        if n%i == 0:
            return False
    return True
        

# print(is_prime(19))

def validate_password(password):
    isValid=True
    
    
    if len(password) < 8:
        print("Password length should not be less than 8")
        isValid= False
    if not  any(char.isdigit() for char in password):
        print("Password should contain at least a number")
        isValid= False
    if not any(char.islower() for char in password):
        print("Password should contain at least a lowercase letter [a-z]")
        isValid= False
    if not any(char.isupper() for char in password):
        print("Password should contain at least a uppercase letter [A-Z]")
        isValid= False
    if not any(char in string.punctuation for char in password):
        print(f"Password should contain at least a special character {''.join(string.punctuation)}")
        isValid = False
        
    if isValid:
        return "Strong Password"
    else:
        return "Not strong enough"


# print(string.punctuation)
def generate_password():
    a = []
    for _ in range(3):
        a.append(random.choice(string.ascii_lowercase))
        a.append(random.choice(string.ascii_uppercase))
        a.append(random.choice(string.digits))
        a.append(random.choice(string.punctuation))
    random.shuffle(a)
    return "".join(a)
        
    
print(generate_password())


# dat = validate_password("Desmond")
# print(dat)