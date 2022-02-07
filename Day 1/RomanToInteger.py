def romanToInt(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    strList = list(s)
    length = len(strList)
    total = 0  
    index = 0
    while index < length:
        # 1st condition IV, IX, ...
        if index + 1 < length:
            combineStr = strList[index] + strList[index + 1]
            if values.get(combineStr) is not None:
                total += values[combineStr]
                index += 2
            else:
                total += values[strList[index]]
                index += 1
        # 2nd condition I, V, ...
        else:
            total += values[strList[index]]
            index += 1
    return total


# input
roman = input()
print(romanToInt(roman))
