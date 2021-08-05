def CaesarCipher(strParam, num):
    upperIndexes = set()
    for i in range(len(strParam)):
        if strParam[i].isupper():
            upperIndexes.add(i)
    strParam = strParam.lower()
    bytes_data = []
    num = num % 26
    for i in range(len(strParam)):
        if 97 <= ord(strParam[i]) <= 122:  # 97 is ascii code for 'a' and 122 is ascii code for 'z'
            cipherByteCode = ord(strParam[i]) + num
            if cipherByteCode > 122:
                cipherByteCode += -122 + 96
                bytes_data.append(cipherByteCode)
            else:
                bytes_data.append(cipherByteCode)
        else:
            bytes_data.append(ord(strParam[i]))
    resultList = []
    for i in range(len(bytes_data)):
        resultList.append(chr(bytes_data[i]))

    for i in range(len(bytes_data)):
        if i in upperIndexes:
            resultList[i] = resultList[i].upper()

    return ''.join(resultList)


print(CaesarCipher(input()))
