import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

my_list = []
my_list.extend(uppercase)
my_list.extend(lowercase)
my_list.extend(digits)
my_list.extend(punctuation)

length = int(input("Enter the length of the password which is going to generate : "))
print("".join(random.sample(my_list, length)))