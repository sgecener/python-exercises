

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Cooked"] = "When a person gets absolutely destroyed at competitive events"
word_definitions["Cold"] = "A description of an event that is showing no mercy"
word_definitions["Tilted"] = "Nervousness when doing something under pressure resulting in increased heart rate, usually leads to mistakes"
word_definitions["Death"] = 42

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["Cold"])
print(word_definitions["Tilted"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

