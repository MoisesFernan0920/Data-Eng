# Romanizer

This project provides a simple utility to convert Arabic numerals (integers) into their Roman numeral equivalents. It includes a function that can take an array of integers and return their corresponding Roman numerals, following the standard rules of Roman numeral representation.

## Problem Description

Given an integer or a list of integers, convert each to its Roman numeral equivalent.

- **Input:** An array of integers, each ranging from 1 to 1000.
- **Output:** An array of strings, where each string is the Roman numeral representation of the corresponding integer.

### Roman Numeral Reference Table

| Arabic | Roman | Arabic | Roman |
|--------|-------|--------|-------|
|   1    |   I   |   40   |  XL   |
|   2    |  II   |   50   |   L   |
|   3    | III   |   90   |  XC   |
|   4    |  IV   |  100   |   C   |
|   5    |   V   |  400   |  CD   |
|   6    |  VI   |  500   |   D   |
|   7    | VII   |  900   |  CM   |
|   8    |VIII   | 1000   |   M   |
|   9    |  IX   |        |       |
|  10    |   X   |        |       |

## Example

**Input:**
```
numbers = [1, 49, 23]
```

**Output:**
```
["I", "XLIX", "XXIII"]
```

### Sample Case

**Input:**
```
5
1
2
3
4
5
```

**Output:**
```
I
II
III
IV
V
```

## How It Works

The conversion is performed by repeatedly subtracting the largest possible Roman numeral value from the input number and appending the corresponding symbol to the result string. The process continues until the input number is reduced to zero.

### Romanizer Function

The main logic is contained in the `romanizer` function:

```python
def romanizer(numbers):
    val_syms = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    ans = []
    for num in numbers:
        roman = ""
        n = num
        for val, sym in val_syms:
            while n >= val:
                roman += sym
                n -= val
        ans.append(roman)
    return ans
```

## Usage

1. Pass a list of integers (each between 1 and 1000) to the `romanizer` function.
2. The function will return a list containing the Roman numeral representation of each integer.

## Constraints

- 1 ≤ n ≤ 1000
- 1 ≤ numbers[i] ≤ 1000

## License

This project is provided as-is for educational purposes.