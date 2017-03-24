# find_needle

def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')

def find_needle(haystack):
    for i in range(0, len(haystack)):
        if haystack[i] == 'needle':
            return "found the needle at position %s" % (i)

# square or square root num
def square_or_square_root(arr):
    result = []
    for num in arr:
        if num ** 0.5 % 1 == 0:
            result.append(num ** 0.5)
        else:
            result.append(num ** 2)
    return result

# Basic math operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# return string with words reversed
def reverse(s):
    a = s.split(" ")
    a.reverse()
    a = " ".join(a)
    return a
