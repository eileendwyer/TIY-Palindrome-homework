

my_string = input(" ")
no_punct = ""
for char in my_string:
    if char not in punctuations:
        no_punc = no_punc + char


my_string = my_string.replace(' ' , '')
my_string = my_string.lower()



if my_string == my_string[::-1]:
        print(" {} is a palindrome!".format (my_string))
else:
        print(" {} is not a palindrome!".format(my_string))
