# Easy: Text मध्ये "Python" word आहे का check करणारा program लिही.
"""
input:- I'm learning a python for AI/ML
output:- found

i want to make a program which found a python text

step 1: import a re module
step 2: create a variable and add a text= I'm learning a python for AI/ML
step 3: found a text 'python'
step 4: print


"""

# import re

# text = "I'm learning a python for AI/ML"

# if re.search("python", text):
#     print("Found")
# else:
#     print("Not found")

# import re

# sentence = input("Enter a sentence:- ")
# word = input("Enter a word to find:- ")

# if re.search(word, sentence):
#     print("Found")
# else:
#     print("Not found")

# import re

# names = ["Lokesh", "Piyush", "Dattu", "Ankit"]

# for name in names:
#     if re.search("Dattu", name):
#         print("Found")
#         break
# else:
#     print("Not found")

# import re

# sentence = input("Enter a word:- ")
# if re.search("[aeiou]", sentence):
#     print("Found!")
# else:
#     print("Not found")

# Medium (corrected): User कडून एक 3-letter word घे, आणि तो पॅटर्न असा आहे का check कर — पहिलं letter फक्त b, c, d, f, किंवा g
# यापैकी एक असावं, आणि नंतर "at" यावं (उदा: "bat", "cat", "fat" match व्हावेत; "eat", "oat", "hat" match होऊ नयेत).
# import re

# word = input("Enter a word:- ")
# if re.search("[bcdfg][a][t]", word):
#     print("Found")
# else:
#     print("Not found")

# Hard: User कडून एक string घे आणि त्यात कुठलाही digit (0-9) आहे का check कर — असेल तर "Found" नाहीतर "Not found"
# (range वापरून, individual digits list न करता).
import re

string = input("enter any word:- ")

if re.search("[0-9]", string):
    print(f"Found::- {string}")
else:
    print("Not found")
