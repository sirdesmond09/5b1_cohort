my_array = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

# def newString(my_array): 
#     str = ''
#     for i in my_array:
#         str += f"{i} "
#     return str
    
# print(newString(my_array))
    
    
# print(" ".join(my_array))



# new_list = ['this', "brown", 55, "oxen", True, 0.85]

# new_list[4] = False

# print(new_list)

# list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# print(list[1:4])


# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# prompt = input("Please enter your color:\n>")
# color_list.append(prompt)
# print(color_list)



# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


# print(color_list.index('Red'))



# print("Welcome to the astroverse!!")

# choice = input("Enter your favourite color:\n>")
# position = int(input("Enter the position:\n>"))

# color_list.append(choice)

# color_list.insert(position, choice)
# print(color_list)


# data = input("Enter your colours seperated by space:\n>")

# cleaned_data = data.split()

# color_list.extend(cleaned_data)

# print(color_list)


#### TUPLES


# my_tuple = 1,2,3,4,5,6
# print(my_tuple)



# a = {1,2,4,6}
# b = {2,4,1,5}

# c = a.symmetric_difference(b)
# # b.intersection_update(a)
# print(c)


english = input("Enter roll number for english students:\n>")
french = input("Enter roll numbers for french students:\n>")


english_list = english.split()
french_list = french.split()

english_set = set(english_list)
french_set = set(french_list)

# total = english_set.symmetric_difference(french_set)

total = english_set.union(french_set)

print(len(total))

