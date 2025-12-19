
# function that loops a number until it returns 6174 (Kaprekar's constatnt)

def kaprekarConstant(num: int) -> list[int]:
    if len(num) == 4:
        digits = list(str(num))
        largest = int(''.join(sorted(digits, reverse=True)))
        smallest = int(''.join(sorted(digits)))
        print (largest, smallest)
    else:
        return "Input 4 digit number only"
    
    constant = 6174
    while  difference != constant:
        difference = largest - smallest
        print(difference)
        break
    
    

# function to check an integer represents a leap year
def leapYear(num: int) -> bool:
    return (num % 400 == 0) or (num % 4 == 0 and num % 100 != 0)

# Armstrong number function
def is_armstrong(num: int) -> bool:
    digits = str(num)
    power = len(digits)

    total = sum(int(d)**power for d in digits)

    return total == num

# Build pyramid in the center with given input
def pyramid(steps: int):
    for i in range(1, steps + 1):
        spaces = steps - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
        

def pyramid2(steps: int):
    for i in range(1, steps + 1):
        spaces = steps - i
        pattern = ''.join('*' if pos % 2 else ' '
                          for pos in range(1, 2 * i))
        print(" " * spaces + pattern)   
        

# Build pyramids of different formats
STAR = "*"
SPACE = " "
CRLF = "\n"
WIDTH = 80
START_PATTERN = STAR
REPEAT_PATTERN = STAR + STAR
END_PATTERN = ""

def pyramid(size: int) -> list[str]:
    return [line(n) for n in range(size)]

def line(n: int) -> str:
    return start(n) + repeat(n) + end(n)

def start(n: int) -> str:
    return START_PATTERN

def repeat(n: int) -> str:
    return n * REPEAT_PATTERN

def end(n: int) -> str:
    return END_PATTERN

def make_pyramid(lines: list[str]) -> str:
    return CRLF.join([line.center(WIDTH//2) for line in lines])

def make_diamond(size: int) -> list[str]:
    return pyramid(size) + pyramid(size)[::-1][1:]

def make_arrow(lines: list[str]) -> str:
    return CRLF.join(lines)

arrow = make_arrow(make_diamond(10))
print(arrow)

# A, D, P, V, X - function to find string format
def is_ascending(text: str) -> bool:                            # A
    return all(text[i] < text[i+1] for i in range(len(text)-1))

def is_descending(text: str) -> bool:                           # D
    return all(text[i] > text[i+1] for i in range(len(text)-1))

def is_peak(text: str) -> bool:                                 # P
    for i in range(1, len(text)-1):
        if is_ascending(text[:i+1]) and is_descending(text[i:]):
            return True
    return False

def is_valley(text: str) -> bool:                               # V
    for i in range(1, len(text)-1):
        if is_descending(text[:i+1]) and is_ascending(text[i:]):
            return True
    return False

def find_string(text: str) -> str:
    if is_ascending(text):
        return "A"
    if is_descending(text):
        return "D"
    if is_peak(text):
        return "P"
    if is_valley(text):
        return "V"
    return "X"
    
print(find_string("abcba"))

# Odometer readings
def is_ascending(s: str) -> bool:
    return all(a < b for (a, b) in zip(s, s[1:]))

def verify(reading: int) -> bool:
    if len(str(reading)) != 3:
        return False
    return is_ascending(str(reading))
        
def prev_num(reading: int) -> int:
    num = reading - 1
    
    while num>=123:
        if verify(num):
            return num
        num -= 1
        
def next_num(reading: int) -> int:
    num = reading + 1
    while num<=789:
        if verify(num):
            return num
        num += 1


# ROT13 function

def rotate_char(ch: str, shift: int = 13) -> str:
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

    return ch


def rot13(text: str) -> str:
    return "".join(rotate_char(ch) for ch in text)


# function for crossword grid analysis from given pattern

def get_rows(pattern: str) -> list[str]:
    rows = []
    current = ""

    for ch in pattern:
        if ch == '\n':
            if current.strip() != "":
                rows.append(current)
            current = ""
        else:
            current += ch

    if current.strip() != "":
        rows.append(current)

    return rows


def get_row_count(rows: list[str]) -> int:
    return len(rows)


def get_column_count(rows: list[str]) -> int:
    max_len = 0
    for row in rows:
        if len(row) > max_len:
            max_len = len(row)
    return max_len


def count_black_cells(rows: list[str]) -> int:
    count = 0
    for row in rows:
        for ch in row:
            if ch == 'x':
                count += 1
    return count


def analyze_grid(pattern: str) -> dict:
    rows = get_rows(pattern)

    row_count = get_row_count(rows)
    col_count = get_column_count(rows)
    total_cells = row_count * col_count

    black_cells = count_black_cells(rows)
    white_cells = total_cells - black_cells

    return {
        "rows": row_count,
        "columns": col_count,
        "total_cells": total_cells,
        "black_cells": black_cells,
        "white_cells": white_cells
    }