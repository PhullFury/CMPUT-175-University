def mylen(some_list):
    some_list.append(None)
    len = 0
    return mylenrecurse(some_list, len)

def mylenrecurse(some_list, len):
    if (some_list[len] == None):
        return len
    else:
        len += 1
        return mylenrecurse(some_list, len)

def intDivision(dividend, divisor):
    if (dividend < 0 or divisor < 0):
        raise Exception("Can only use non-negative numbers")
    if (divisor == 0):
        raise Exception("Can't divide by 0")
    count = 0
    return intDivisionrecurse(dividend, divisor, count)

def intDivisionrecurse(dividend, divisor, count):
    count += 1
    sub = dividend - divisor
    if (dividend == 0):
        return 0
    elif (sub < divisor):
        return count
    else:
        return intDivisionrecurse(sub, divisor, count)

def sumdigits(number):
    if (number < 0):
        raise Exception("Can only use non-negative numbers")
    sum = 0
    return sumdigitsrecurse(number, sum)

def sumdigitsrecurse(number, sum):
    sum += number%10
    if (number//10 == 0):
        return sum
    else:
        number = number//10
        return sumdigitsrecurse(number, sum)

def reverseDisplay(number):
    if (number < 0):
        raise Exception("Can only use non-negative numbers")
    reverse = 0
    print(reverseDisplayrecurse(number, reverse))

def reverseDisplayrecurse(number, reverse):
    if (number == 0):
        return reverse
    else:
        reverse *= 10
        if not(number%10 == 0):
            reverse += number%10
        number //= 10
        return reverseDisplayrecurse(number, reverse)

def binary_search2(key, alist, low, high):
    if (low > high):
        return "Item is not in the list"
    else:
        guess = (high + low) // 2
        if (key == alist[guess]):
            return guess
        else:
            if (key < alist[guess]):
                high = guess - 1
            else:
                low = guess + 1
            return binary_search2(key, alist, low, high)

def main():
    alist=[43, 76, 97, 86]
    print(f"My len is: {mylen(alist)}")
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print(f"Integer division {n} // {m} = {intDivision(n,m)}")
    number = int(input('Enter a number: '))
    print(sumdigits(number))
    number = int(input('Enter a number: '))
    reverseDisplay(number)
    some_list = [-8, -2, 1, 3, 5, 7, 9]
    print(binary_search2(9, some_list, 0, len(some_list) - 1))
    print(binary_search2(-8, some_list, 0, len(some_list) - 1))
    print(binary_search2(4, some_list, 0, len(some_list) - 1))

main()