pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.4, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted = sorted(numbers)
print(sorted)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)