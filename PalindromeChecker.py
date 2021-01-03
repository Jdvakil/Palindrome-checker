#H8_jay.py
"""
This program has been commanded to find if a string entered by the user is palindrome or it isn't (palindrome : a word or a phrase that reads the same
backward as forward. ). If the string is palindrome, the output would display "True", if the string is not palindrome, then the output would display "False".
"""

#Input :
def get_input():
    string = str(input("Enter the word/phrase here : "))
    return string
"""
Here, the user enters the word or the phrase the user wants to check if it is palindrome or not.
no arguments for function get_input().
"""
#process and output :
def isPalindrome(string):
    lenght = len(string)
    index = 0
    while index < lenght:
        if string[index] != string[-index -1]:#this determines whether the string qualifies to be palindrome.
            return(False)
            break
            index += 1
            break
        else:
            return(True)
            break
"""
This function "isPalindrome" is the main processing part of the whole program, here it checks if the string entered is palindrome.
string variable from get_input(), is the main argument for this function.
"""
def main():
    string = get_input()
    print(isPalindrome(string))
"""
This is the functions that calls all the other functions.
"""
if __name__ == "__main__":
    main()#This calls the main function that calls the other functions 
