'''
Convert Number to Word Name
'''

def number_to_words(n):
    ones = [
        "", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    words = ""

    if n >= 1000:
        words += ones[n // 1000] + " thousand "
        n = n % 1000

    if n >= 100:
        words += ones[n // 100] + " hundred "
        n = n % 100

    if n >= 20:
        words += tens[n // 10] + " "
        n = n % 10

    if n >= 10:
        words += teens[n - 10]
        n = 0

    if n > 0:
        words += ones[n]

    return words.strip()


# Example from the book
number = 2562

print("Number:", number)
print("Word name:", number_to_words(number))
