'''
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel

'''
char = input()

if char.isalpha():  # Check if the character is an alphabet
    if char.lower() in 'aeiou':  # Check if the character is a vowel
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
