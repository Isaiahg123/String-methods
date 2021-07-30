# author:
# date:

# --------------- Section 1 --------------- #

# 1 | String Methods
#
# 1 - Save your name to a variable named name.
#   a. Center that variable within 30 characters. Print it.
#   b. Print the variable in all upper case.
#   c. Print the variable in all lower case.
#   d. Print the variable capitalized (Look to documentation.)



my_name='isaiah'

#so what this does is it puts your name in the middle of 30 characters
print(my_name.center(30))

#this puts your name string in ALL caps
print(my_name.upper( ))

#this puts your name string in all lowercase
print(my_name.lower( ))

#this capitalizes the FIRST LETTER of the name string
print(my_name.capitalize( ))



# 2 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first instance of the letter a. Print that position.
#you don't have to do b and c

#set it equal to input from the user. the prompt should simply be "enter a sentence"
text=input('enter a sentece')

#now, we have to specify what exactly we're finding! for positionA, we are looking for the letter a, so put "a" in the parentheses! make sure it's in quotations
positionA=text.find('a')
positionE=text.find('e')
positionI=text.find('i')
positionO=text.find('o')
positionU=text.find('u')

#now, we'll simply print out the positions
#simply print out each of the variables individually with a message specifying what it means!
#positionA should be outside of quotation marks! you can put something like  "first appearance of letter a:" in the quotations

#example: print("first appearance of a", positionA)
print(positionA)
 



# 3 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the position of every vowel in text. Save them each to a variable.
#   b. Using a built-in function, print the position of the vowel that shows up last.
#   c. Using a built-in function, print the position of the vowel that shows up first.


# 4 | String Indexing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the 0th letter of the text using string indexing.
#   b. Print the 1st, 2nd, and 3rd letters of the text using string indexing.
#   c. Print the last letter of the text using string indexing.
#       HINT: There are multiple ways of doing this. Is there a function that we can use that will find
#           the position of the last letter, or atleast one off from it?


# 5 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Slice text from the 2nd position to the 5th. Print that.
#   b. Slice text from the 0th position to the 8th. Print that.
#   c. Slice text from 3rd position to end. Print that.
#   d. Slice text from the beginning to 5 positions before the last character. Print that.
#       HINT: Use a function to get the last position of the string.


# 6 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the text, but only every 2nd character.
#   b. Print the text, but only every 3rd character.
#   c. Print the text, but in reverse order.

