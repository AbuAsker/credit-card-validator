# Credit Card Validator

A Python program that validates credit card numbers using the Luhn (Mod 10)
algorithm and identifies the card issuer.

**Course:** EE202 Object-Oriented Programming, ECE Department, KAU
**Assignment:** Group Assignment 1 (Team A)

## Features
- Accepts input with spaces or hyphens
- Rejects non-digit input, prints a message, and asks again
- Checks length (13-16 digits) and prefix (Visa, MasterCard, American Express, Discover)
- Validates the number with the Luhn algorithm
- Prints the card type for valid numbers

## How to Run
    python credit_card_validator.py

## Example
    Enter a valid credit card number: 4388 5760 1841 0707
    4388576018410707 is valid
    Card type: Visa

    Enter a valid credit card number: abc
    Please enter digits only

## Documentation
A detailed explanation of the code, with execution traces, is available in
[docs/Code_Explanation.docx](docs/Code_Explanation.docx).

## Team
| Member | GitHub | Contribution |
|--------|--------|--------------|
| Naif Adel Alghaith | [@username](https://github.com/username) | isValid, sumOfOddPlace |
| Hamzah Adel Abu-Askar | [@AbuAsker](https://github.com/AbuAsker) | getDigit |
| Abdulelah Mohammed Fatani | [@username](https://github.com/username) | sumOfDoubleEvenPlace |
| Fahad Abdullah Alosaimi | [@username](https://github.com/username) | prefixMatched, getSize |
| Abdulrahman Basurrah | [@username](https://github.com/username) | getPrefix, input error handling, result printing, report |
