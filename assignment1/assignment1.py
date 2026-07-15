# Write your code here.
def hello():
    return 'hello!'
print(hello())

# Task 2
def greet(name):
    return ('Hello, ' + name + '!')
print(greet('Zoe'))

# Task 3
def calc(val1, val2, defaultValue='multiply'):
    try:
        if defaultValue == 'add':
            return val1 + val2
        elif defaultValue == 'subtract':
            return val1 - val2
        elif defaultValue == 'multiply':
            return val1 * val2
        elif defaultValue == 'divide':
            return val1 / val2
        elif defaultValue == 'module':
            return val1 % val2
        elif defaultValue == 'int_divide':
            return val1 // val2
        elif defaultValue == 'power':
            return val1 ** val2
        else:
            return 'Error: Unknown operation'
    except ZeroDivisionError:
        return "Error: You can't divide by 0!"
    except TypeError:
        return "Error: You can't multiply those values!" 
print(calc(2, 3, 'multiply'))
print(calc(9, 3, 'divide'))
print(calc('1', 'hi', 'multiply'))
print(calc(2, 0, 'divide'))

# Task 4
def data_type_conversion(value, type='str'):# data type=float, str or int
    try:
        if type == 'float':
            return float(value)
        elif type == 'str':
            return str(value)
        elif type == 'int':
            return int(value)
        else: 
            return f"You can't convert {value} into a {type}"
    except ValueError:
        return f"You can't convert {value} into a {type}"
    except TypeError:
        return f"You can't convert {value} into a {type}"
print(data_type_conversion("5", "float"))#float
print(data_type_conversion(91.1, "str"))#string
print(data_type_conversion("110", "int"))#integer
print(data_type_conversion("nonsense", "float"))#type error
print(data_type_conversion("abc", "int"))# type error

# Task 5
def grade(*args):
    try:
        #compute the average, and return the grade
        average = sum(args) / len(args)
        #determine the letter grade
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:   
            return "F"
    except TypeError:
        return  "Invalid data was provided."
print(grade(85))
print(grade(65))
print(grade(75))
print(grade(95))
print(grade('hello'))

# Task 6
def repeat(string:str, count:int):
    # return a new string
    new_str = ""
    for _ in range(count):
        new_str += string
    return new_str
print(repeat("hi", 3))

# Task 7-revise it
def student_scores(choice, **kwargs):
    if not kwargs:
        return None  
    if choice == 'best':
        return max(kwargs, key=kwargs.get)
    elif choice == 'mean':
        return sum(kwargs.values() / len(kwargs))
print(student_scores('best'))

# Task 8
def titleized(str):

   # store the input string splitted in the 'words' variable 
    words = str.split()

    # if input is empty return an empty string
    if not words:
        return ""

    # Add little_words to an array
    litle_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    # process the string based on its position and contnt
    for i, word in enumerate(words):

        # capitilized the 1st letter of the 1st word
        #  and the 1st letter of the 2nd word
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        # keep little_words in lowercase
        elif word.lower() in litle_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    #return a new string         
    return " ".join(words)
print(titleized("apple bee's"))

# Task 9
def hangman(secret: str, guess: str) -> str: 
    #The secret is some word that the caller doesn't know. So the caller 
    # guesses various letters, which are the ones in the guess string.
    secret = "alphabet"
    # variable that will hold the new string
    result = []
     
    for letter in secret:
        if letter.lower() in guess:
            result.append(letter)
        else:
            result.append("-")
    return ' '.join(result)
print(hangman(" ", "hit"))

# Task 10
def pig_latin(str):
    #  If the string starts with a vowel 
    # (aeiou), "ay" is tacked onto the end.
    vowels = "a,e,i,o,u"
    # break a single string into a list of smaller substring and save that in 'words'
    words = str.split()
    # create a  empty list and assign it to 'result'
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            vowel_index = next((i for i, char in enumerate(word) if char in vowels), None)

            if vowel_index is None:
                result.append(word + "ay" )
            else:
                result.append(word[vowel_index:] + word[:vowel_index] + "ay")
            return " ".join(result)
print(pig_latin("glove"))# word start with two consts word = oveglay
print(pig_latin("cat"))# word start with const, the const is attached at the edn and "ay" is added at the end of it
print(pig_latin("quick")) # word start with a vowel "ay" is attach at the end- egg = eggay
print(pig_latin("yellow"))# const is add at the end then 'ay' = ellowyay