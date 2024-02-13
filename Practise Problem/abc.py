def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(word_list):
    palindromes = [word for word in word_list if is_palindrome(word) and word.isalpha()]
    numeric_palindromes = [num for num in word_list if is_palindrome(str(num)) and num.isdigit()]
    
    return palindromes + numeric_palindromes

# Example usage:
word_list = ["level", "12321", "python", "radar", "45654", "civic", "hello"]

result = find_palindromes(word_list)
print(f"Palindromes in the list: {result}")