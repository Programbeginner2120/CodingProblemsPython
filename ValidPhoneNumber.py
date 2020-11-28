# URL: https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python

'''Valid Phone Number: Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.
Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)'''


def validPhoneNumber(phoneNumber):
    validPhoneNumberFormat = "(xxx) xxx-xxxx"  # This is the format of all valid phone numbers
    digitSet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}  # set of digits in a phone number
    for i in phoneNumber:
        if i in digitSet:
            phoneNumber = phoneNumber.replace(i, "x")  # replace digit with x
    return phoneNumber == validPhoneNumberFormat  # will return True if phone number is valid, False otherwise


print(validPhoneNumber("(123) 456-7890"))  # returns True
print(validPhoneNumber("(1111)555 2345"))  # returns False
print(validPhoneNumber("(098) 123 4567"))  # returns False
