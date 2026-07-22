# Write your code here.
def hello():
    return 'Hello!'
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"
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
        elif defaultValue == 'modulo':
            return val1 % val2
        elif defaultValue == 'int_divide':
            return val1 // val2
        elif defaultValue == 'power':
            return val1 ** val2
        else:
            return 'Error: Unknown operation'
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!" 
print(calc(2, 3, 'multiply'))
print(calc(9, 3, 'divide'))
print(calc('1', 'hi', 'multiply'))
print(calc(2, 0, 'divide'))

# Task 4
def data_type_conversion(value, data_type):# data type=float, str or int
    try:
        if data_type == 'float':
            return float(value)
        elif data_type == 'str':
            return str(value)
        elif data_type == 'int':
            return int(value)
        else: 
            return f"You can't convert {value} into a {data_type}."
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    except TypeError:
        return f"You can't convert {value} into a {data_type}."
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
        return "Invalid data was provided."
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

# Task 7
def student_scores(choice, **kwargs):
    if choice == "best":
        student_with_best_scores = max(kwargs, key=kwargs.get)
        return student_with_best_scores
    elif choice == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        raise ValueError("Invalid option, please choose 'best' or 'mean'" )
print(student_scores("best", Hanna=85, Zoe=95, Aria=75, tim=75))
print(student_scores("mean", math=95, history=80, science=95))

# Task 8
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"] 
    words = text.split() 
    
    if not words:
        return ""    
    # process the string based on its position and content 
    for i, word in enumerate(words):   
        # convert the word to lower case first
        word_lower = word.lower()
        if i == 0 or i == len(words) - 1:
            words[i] = word_lower.capitalize() # capitilize
        elif word_lower in little_words:
            words[i] = word_lower 
        else:
            words[i] = word_lower.capitalize()# capitilize litle_words       
    # return a new string 
    return " ".join(words)
print(titleize("apple bee's"))
print(titleize("a clash of clans"))
print(titleize("after on"))

# Task 9
def hangman(secret: str, guess: str) -> str: 
    # variable that will hold the new string
    result = []
     
    for letter in secret:
        if letter.lower() in guess:
            result.append(letter)
        else:
            result.append("_")
    return "".join(result)
print(hangman("difficulty", "ic"))

# Task 10
def pig_latin(str_input):
    vowels = set("aeiou")
    result = []
  
    for word in str_input.split():
       # starts with a vowel
       if word[0] in vowels:
           new_word = word + "ay"   
       else:
           # check for consonant - if first letter is a cons. save it to first_vowel
           first_vowel = 0
           for i, char in enumerate(word):
               if char in vowels:
                   first_vowel = i
                   break 
           # does str starts with a consonant cluster
           consonant_cluster = word[:first_vowel]

           # handle "qu"
           if word[first_vowel-1:first_vowel + 1] == "qu":
               consonant_cluster += 'u'
               first_vowel += 1
           elif word[first_vowel:first_vowel + 2] == "qu":
               consonant_cluster += "qu"
               first_vowel += 2      
           new_word = word[first_vowel:] + consonant_cluster + "ay"   
           #print("here: ",consonant_cluster)  
       result.append(new_word)      
    return " ".join(result)
print(pig_latin("the quick brown fox"))
print(pig_latin("yellow"))
print(pig_latin("square"))
print(pig_latin("quiet"))