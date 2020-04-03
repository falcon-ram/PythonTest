# Translator

# Convert all vowels to g
def translate(phrase):
    translation = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou": # use of in to check if the letter is in the string
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# testing if/in
num = input("Enter a number: ")
if num in range(10):
    print("Hello")

