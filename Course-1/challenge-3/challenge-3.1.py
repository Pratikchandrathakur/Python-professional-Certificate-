# Python code​​​​​​‌‌​​‌​‌​​‌‌‌​‌​​​​​​‌​‌‌‌ below
def encodeString(stringVal):
    # Your code goes here.
    encodedList = []
    prevChar = stringVal[0]
    count = 1  # Start counting from 1 for the first character

    for char in stringVal[1:]:  # Iterate from the second character
        if prevChar != char:
            encodedList.append((prevChar, count))
            prevChar = char
            count = 1
        else:
            count += 1
    encodedList.append((prevChar, count))  # Append the last character and its count
    return encodedList
pass


def decodeString(encodedList):
    # Your code goes here.
    decodedStr = ''
    for item in encodedList:
        decodedStr += item[0] * item[1]  # Append the character repeated 'count' times
    return decodedStr
pass

  
      
    
      
    
