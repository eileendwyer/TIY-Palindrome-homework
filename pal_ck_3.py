import string

my_string = input("Enter a word, sentence or list of numbers. ").lower()
my_string = my_string.replace(' ' , '')

for item in string.punctuation:
    my_string = my_string.replace(item, "")

if my_string == my_string[::-1]:
        print(" {} is a palindrome!".format (my_string))
else:
        print(" {} is not a palindrome!".format(my_string))
P