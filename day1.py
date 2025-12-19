# function that returns largest of the input three integers
def largeNumber(a,b,c):
    if a>b>c:
        return(a,b)
    

# function that returns true only when exactly any 2 of the 3 inputs are True
def code2(a:bool, b:bool, c:bool) -> bool:
    l = [a,b,c]
    count = 0
    for i in l(l+1):
        if i == True:
            count = count+1
        else:
            return False
        
        
# function to find sum of all unique integers from the given list
total = 0
def sumUniqueNum(a:list) -> list:
    for i in a(a+1):
        if i != i+1:
            total += i
            
    return total

# function to get the collatz sequence with the given number
def collatzSeq(a: int) -> list:
    final_list = []

    while a != 1:
        final_list.append(a)
        if a % 2 == 0:
            a = a // 2
        else:
            a = a * 3 + 1

    final_list.append(1)
    return final_list

collatzSeq(7)

# function to print fizz for 3 multiples, buzz for 5 multiples and common multiples for both should be fizz-buzz and all in strings only
def fizzBuzz(num: int) -> list[str]:
    final = []
    for i in range(1, num):
        if i % 15 == 0:
            final.append("fizz-buzz")
        elif i % 3 == 0:
            final.append("fizz")
        elif i % 5 == 0:
            final.append("buzz")
        else:
            final.append(i)
    return final


print(fizzBuzz(20))
