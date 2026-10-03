#Get the card number from user
number = input("Enter a valid credit card number: ")
number = number.replace(" ", "").replace("-", "") #Error handling - Spacing
while not number.isdigit():
    print("Please enter digits only")
    number = input("Enter a valid credit card number: ")
    number = number.replace(" ", "").replace("-", "") #Error handling - Spacing

number = int(number)

# Return true if the card number is valid
def isValid(number):
    size = getSize(number)
    
    # 1. Check length: Must be between 13 and 16 digits
    if not (13 <= size <= 16):
        return False
        
    # 2. Check prefix: Must start with 4, 5, 37, or 6
    if not (prefixMatched(number, 4) or 
            prefixMatched(number, 5) or 
            prefixMatched(number, 37) or 
            prefixMatched(number, 6)):
        return False

    # 3. Calculate Luhn algorithm: sum of even places + sum of odd places
    total_sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    
    # 4. Final check: Is the total sum divisible by 10?
    if total_sum % 10 == 0:
        return True
    else:
        return False

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sum_even = 0
    num_str = str(number)
    
    # Loop from second-to-last digit from right to left
    for i in range(len(num_str) - 2, -1, -2):
        digit = int(num_str[i])
        sum_even += getDigit(digit * 2)
        
    return sum_even

# Return this number if it is a single digit, otherwise, return the sum of the two digits
def getDigit(number):
    if number< 10:
        return number
    else:
        return (number//10) + (number%10)

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sum_odd = 0
    num_str = str(number)
    
    # Iterate through every odd place digit from right to left
    for i in range(len(num_str) - 1, -1, -2):
        sum_odd += int(num_str[i])
        
    return sum_odd

# reurn true if the digit d is a prefix for the number
def prefixMatched(number, d):
    return getPrefix(number, getSize(d)) == d

# Return the nuber od digits in d 
def getSize(d):
    return len(str(d))

# Return the first k number of digits from number. If the number of digits in number is less than k, return number.
def getPrefix(number, k):
    size = getSize(number)
    if size <= k:
        return number
    return number // (10 ** (size - k))

# Return the card type based on the prefix (extra feature)
def getCardType(number):
    if prefixMatched(number, 4):
        return "Visa"
    elif prefixMatched(number, 5):
        return "MasterCard"
    elif prefixMatched(number, 37):
        return "American Express"
    elif prefixMatched(number, 6):
        return "Discover"
    else:
        return "Unknown"

#Printing result
if isValid(number):
    print(number, "is valid")
    print("Card type:", getCardType(number))
else:
    print(number, "is invalid")