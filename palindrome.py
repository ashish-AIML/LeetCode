# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Solution 1
def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return print('x is palindrome',x[::-1])
    else:
        return print('x is not palindrome',x[::-1])

x = 'abc'
isPalindrome(x)

# Solution 2
def isPalindrome(x):
    if x < 0:
        return False

    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num == x

x = 'abc'
isPalindrome(x)