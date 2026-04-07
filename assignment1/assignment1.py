# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"
    
# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add": return a + b
            case "subtract": return a - b
            case "multiply": return a * b
            case "divide": return a / b
            # ... add the rest ...
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
    if __name__ == "__main__":
    print(f"Task 3 Test (Add): {calc(13, 5, 'add')}")          # Expected: 18
    print(f"Task 3 Test (Default): {calc(10, 6)}")            # Expected: 60
    print(f"Task 3 Test (Zero): {calc(10, 0, 'divide')}")     # Expected: You can't divide by 0!
    print(f"Task 3 Test (Type): {calc('hi', 'bye')}")       # Expected: You can't multiply those values!

    # Task 4 
    
    def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Invalid type requested"
                
    except (ValueError, TypeError):
        # We catch both because some 'nonsense' inputs trigger TypeError 
        # while others trigger ValueError.
        return f"You can't convert {value} into a {type_name}."
    if __name__ == "__main__":
    # Successful conversions
    print(data_type_conversion("124", "int"))      # Expected: 124
    print(data_type_conversion(11.5, "str"))      # Expected: "11.5"
    
    # Failing conversion
    print(data_type_conversion("nonsense", "float")) 
    # Expected: You can't convert nonsense into a float.
    

# Task 5
def grade(*args):
    try:
        # Step 1: Check if any arguments were actually provided
        # to avoid a ZeroDivisionError (sum / 0)
        if not args:
            return "F" 
            
        # Step 2: Compute the average
        average = sum(args) / len(args)
        
        # Step 3: Determine the letter grade
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
        # This catches "nonsense" like passing a string instead of a number
        return "Invalid data was provided."
    
if __name__ == "__main__":
    print(grade(91, 90, 87))       # Expected: "A" (Average is 90)
    print(grade(71, 80))           # Expected: "C" (Average is 75)
    print(grade(95, "oops"))      # Expected: "Invalid data was provided."


#Task 6 

def repeat(string, count):
    # Initialize an empty string to hold our result
    result = ""
    
    # The underscore (_) is a common Python convention when 
    # you don't actually need the number (0, 1, 2...) inside the loop.
    for _ in range(count):
        result += string
        
    return result

if __name__ == "__main__":
    print(f"Repeat 3 times: '{repeat('Chirp', 3)}'")   # Expected: 'ChirpChirpChirp'
    print(f"Repeat 0 times: '{repeat('host', 0)}'")  # Expected: ''
    print(f"Repeat 1 time:  '{repeat('One', 1)}'")   # Expected: 'One'

#Task 7

def student_scores(action, **kwargs):
    # Step 1: Handle the case where no student data is provided
    if not kwargs:
        return 0 if action == "mean" else None

    # Step 2: Extract all the scores (the values in the dictionary)
    scores = kwargs.values()

    if action == "best":
        # We need to find the name (key) associated with the highest score
        best_student = None
        highest_score = -1
        
        for name, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = name
        return best_student

    elif action == "mean":
        # Calculate the average of all scores
        return sum(scores) / len(scores)
    
    return "Invalid action"

if __name__ == "__main__":
    # Test for "best"
    print(student_scores("best", Joe=85, Faith=92, Charles=78))  
    # Expected: "Faith"

    # Test for "mean"
    print(student_scores("mean", Joe=80, Faith=90))              
    # Expected: 85.0

    #Task 8

    def titleize(title_string):
    # Step 1: Create our list of "little words"
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    
    # Step 2: Split the string into a list of words
    words = title_string.split()
    
    # If the string is empty, return it as is
    if not words:
        return ""
    
    result_words = []
    last_index = len(words) - 1
    
    # Step 3: Loop through with index (i) and the word itself
    for i, word in enumerate(words):
        # Rule 1 & 2: First word (i == 0) or Last word (i == last_index)
        if i == 0 or i == last_index:
            result_words.append(word.capitalize())
        
        # Rule 3: Middle words
        else:
            if word.lower() in little_words:
                # Keep it lowercase if it's a "little word"
                result_words.append(word.lower())
            else:
                # Capitalize it otherwise
                result_words.append(word.capitalize())
                
    # Step 4: Join the list back into a single string with spaces
    return " ".join(result_words)
if __name__ == "__main__":
    print(titleize("the art of war"))           # Expected: "The Art of War"
    print(titleize("the catcher in the rye"))   # Expected: "The Catcher in the Rye"
    print(titleize("is this a test"))           # Expected: "Is this a Test"

# Task 10

    def hangman(secret, guess):
    # This is our "bucket" to build the result
    result = ""
    
    # Loop through every character in the secret word
    for letter in secret:
        # Check if this specific letter exists anywhere in the guesses
        if letter in guess:
            # If it's a match, keep the letter
            result += letter
        else:
            # If not, hide it with an underscore
            result += "_"
            
    return result
if __name__ == "__main__":
    # The example from the task
    print(hangman("alphabet", "ab"))      # Expected: "a___ab__"
    
    # Testing a full guess
    print(hangman("python", "pythno"))    # Expected: "python"
    
    # Testing no matches
    print(hangman("secret", "xyz"))       # Expected: "______"


#task 10 
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    translated_words = []

    for word in words:
        # Rule 1: Starts with a vowel
        if word[0] in vowels:
            translated_words.append(word + "ay")
        
        # Rule 3: Special case for "qu"
        elif word.startswith("qu"):
            translated_words.append(word[2:] + "quay")
            
        # Rule 2: Starts with one or more consonants
        else:
            vowel_index = 0
            # Find the first vowel to know where to "cut"
            for i, char in enumerate(word):
                if char in vowels:
                    vowel_index = i
                    break
            else:
                # If no vowel is found (e.g., "sky"), treat the whole word 
                # as consonants and just add "ay"
                vowel_index = len(word)

            # Move consonants to the end and add "ay"
            prefix = word[:vowel_index]
            suffix = word[vowel_index:]
            translated_words.append(suffix + prefix + "ay")

    return " ".join(translated_words)

if __name__ == "__main__":
    print(pig_latin("apple"))          # Expected: "appleay"
    print(pig_latin("smile"))          # Expected: "ilesmay"
    print(pig_latin("quiet"))          # Expected: "ietquay"
    print(pig_latin("the quick fox"))  # Expected: "ethay ickquay oxfay"
