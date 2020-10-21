#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved.
# ------------------- ΠΑΡΑΔΕΙΓΜΑ A---------------------
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + " " + question_text
# Prints "Hey there! How are you doing?"
print(full_text)

# ------------------- ΠΑΡΑΔΕΙΓΜΑ B---------------------
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
full_birthday_string = birthday_string + str(age) + birthday_string_2

print(full_birthday_string)
print(birthday_string, age, birthday_string_2)
print(f'I am {age} years old today!')
print('I am {} years old today!'.format(age))

# ------------------- ΑΣΚΗΣΗ ---------------------
"""
Συνδυάστε τις συμβολοσειρές και αποθηκεύστε το μήνυμα που σχηματίζουν στην μεταβλητή message.
Εκτυπώστε και εκτελέστε τον κωδικό σας για να δείτε το αποτέλεσμα στο τερματικό!
"""

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = ...
# Print message
