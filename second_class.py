# my_string = "This is 1840 naira"
# st2 = "This 570 is lovely"


# first_num = my_string[8:12]
# second_num = st2[5:8]
# added = int(first_num)  +  int(second_num)

# print(f"The sum of {first_num} and {second_num} is {added}")

# print("The sum of %s and %s is %d" % (first_num, second_num, added))


# print("This is ayo's book")
# print('This is ayo\'s book')


# print("Dear, Buhari.\nPlease don't run for president again.\n\tYours in the Country.\n\t\tAstroverse Team.")


# print("""This is a wonderful string




#                     Yours in country.
#                     The Astroverse team.""")


# my_sentence = "A quick brown, fox jumps over, a lazy dog"

# a = my_sentence.split(",")
# print(a)


# num = ['0','4','3','2']

# otp = "".join(num)

# print(otp)



# s1 = "Ault"
# s2 = "Kelly"

# print("Original Strings are", s1, s2)

# # middle index number of s1
# mi = len(s1) // 2

# # get character from 0 to the middle index number from s1
# x = s1[:mi] + s2 + s1[mi:]

# print(x)



# str1 = 'Emma-is-a-data-scientist'

# print(str1.replace('-', ' '))


# print(" ".join(str1.split('-')))


# str1 = "/*Jon is @developer & musician"

# final_answer = str1.replace("/","").replace("*","").replace('@',"").replace("& ", "")

# print(final_answer)


##### LIST #####


my_list = ["I", 'am', "good"]
a_list = ["She", "is", "a", "queen"]

x= my_list + a_list
print(x[::2])

["I", "good", "is", "queen"]


#Given the list below:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Get 5000 and 500 out of the list and add them together.
# Print the result on the terminal
#Keep slicing until there's nothing to slice anymore!!!😎😎😎


print(list1[2][2][0] + list1[2][3])