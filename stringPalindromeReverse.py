#Begin we are going to reverse a string
#after that we want to check if its a palindrome ex(racecar)
#then check for how many vowels are in a word
userInput=input("Enter your word-> ").lower()



userInputLen=len(userInput)
userReverse=""
userVowel=0
userPalindrome=False
for x in reversed(userInput):
    userReverse+=x
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y":
        userVowel+=1

if userInput==userReverse:
    userPalindrome=True







print(userInput,"is the current string")
print("String is",userInputLen,"characters long")
print(userReverse,"This is",userInput,"Reversed")
print("Palindrome",userPalindrome)
print(userInput,"has",userVowel,"vowels")
