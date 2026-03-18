#wap take a string from kwy board found no character,no of alphabet no of upper case no of lower case no of vowel
# no of consonant, no of digit,no of spaces,no of symbols,no of words 
# s="12ab#"
# print(s.isalnum())
# s="ab"
# print(s.isalpha())
s = input("Enter a string: ")

char_count = len(s)
alpha = upper = lower = vowel = consonant = digit = space = symbol = 0

for ch in s:
    if ch.isalpha():
        alpha += 1
        
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
        
        if ch.lower() in "aeiou":
            vowel += 1
        else:
            consonant += 1
    
    elif ch.isdigit():
        digit += 1
    
    elif ch.isspace():
        space += 1
    
    else:
        symbol += 1

# word count
words = len(s.split())

# output
print("Total characters:", char_count)
print("Alphabets:", alpha)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digit)
print("Spaces:", space)
print("Symbols:", symbol)
print("Words:", words)