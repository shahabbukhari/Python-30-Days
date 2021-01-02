# Factorial Using recursion 
def recursiveFac(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * recursiveFac(n-1)
        #       3 * recursiveFac(2)
        #       3 * 2 * recursiveFac(1) now when it goes to one it will return 1 recursion will stop
        #       3 * 2 * 1

# user_input = int(input('Enter a Number: ')) 
# print(recursiveFac(user_input)) 

# fibonacci series using recursion
# 0 1 1 2 3 5 8 13 21 
def feboSeries(n):
    if n == 1:      # BASE CASE 
        return 0   
    elif n == 2:    # BASE CASE
        return 1
    else:           # b1               b2            #     RECURSIVE CASE
        return feboSeries(n-1)  + feboSeries(n-2)

# print(feboSeries(5)) # a


# Reverse the string 
name = 'ShaHab'

def reversestr(name):
    reverse_name = ' '
    if len(name) <= 1:
        return name
    else:
        for i in range(len(name)):
            reverse_name += name[-(i+1)] 
    return reverse_name

def rec_reverse(name):
    result = ''
    if len(name) <= 1:
        return name
    else:
        return result + rec_reverse(name[])
print(rec_reverse(name))

# # sum to n
# def sumto(n):
#     result = n
#     if n <= 1:
#         return n
#     else:
#         # for i in range(n+1):
#         #     result = result + i
#         result = sumto(result-1) + n
#     return result
# print(sumto(3))