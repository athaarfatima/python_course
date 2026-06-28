print(input("\nLet's play a quick game to check how well you know the PALINDROMES!"))

word = input("\nEnter any word: ").lower()

reversed = ""

for letter in word:
    reversed = letter + reversed
if word == reversed:
        print("\nGreat job! The given word is a palindrome.")
else:
        print("\nOops! That wasn't a palindrome.\n   Better luck next time. ")