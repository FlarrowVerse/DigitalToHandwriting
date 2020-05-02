import os
import cv2
import numpy as np

def getCompressed(img, dim): # to get the smaller image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

'''def getTerminalPixels(matrix): # this module only applies to the terminal output
    writing = []
    for row in matrix:
        temp = ''
        for col in row:			
            if col != 255:				
                temp += '*'
	    else:
                temp += '-'
        writing.append(temp)
    return writing'''

def getPixels(matrix):
    writing = []
    for row in matrix:
        temp = []
        for col in row:			
            temp.append(col)
        writing.append(temp)
    return writing

def writeToConsole(writing): # for terminal writing only
    for row in writing:
        print(row)

def writeImage(url, dim): # handler module for program
    print('url:', url, end=' ')
    img = cv2.imread(url)
    print('[+] Reading Done....', end=' ')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print('[+] Grayscale Done....', end=' ')
    smaller = getCompressed(gray, dim)
    print('[+] Compression Done....')
    return smaller

def getSymbolFile(char):
    
    with open(os.path.join("Satyaki_hw", "symbol", "index.txt")) as file:
        value = file.read().split('\n')
        for v in value:
            if v.split()[0] == char:
                return v.split()[1]    

def getUrl(char): # supplies the correct url for the alphabet, digit or symbol image file
    filename = char + '.jpg'
    if char >= 'A' and char <= 'Z': # for upper case characters
        #return 'Satyaki_hw\\upper\\' + char + '.jpg'
        return os.path.join("Satyaki_hw","upper",filename)
    elif char >= 'a' and char <= 'z': # for lower case characters
        #return 'Satyaki_hw\\lower\\' + char + '.jpg'
        return os.path.join("Satyaki_hw","lower",filename)
    elif char >= '0' and char <= '9': # for digits
        #return 'Satyaki_hw\\digit\\' + char + '.jpg'
        return os.path.join("Satyaki_hw","digit",filename)
    elif char == ' ': # for any kind of whitespace
        #return 'Satyaki_hw\\whitespace.jpg'
        return os.path.join("Satyaki_hw","whitespace.jpg")
    else: # for symbols
        return os.path.join("Satyaki_hw","symbol",getSymbolFile(char))
    

def writeLine(line, dim):
    lineImg = writeImage(getUrl(line[0]), dim)
    for index in range(1, len(line)):
        url = getUrl(line[index])
        if url == None:
            print(line[index])
        temp = writeImage(getUrl(line[index]), dim)
        bckp = cv2.hconcat([lineImg, temp])
        lineImg = bckp
    return lineImg

def formatLines(lines):
    maxLen = len(lines[0])
    for i in range(1, len(lines)):
        maxLen = max(maxLen, len(lines[i]))
    for i in range(0, len(lines)):
        if len(lines[i]) < maxLen:
            lines[i] += ' ' * (maxLen - len(lines[i]))    
    return lines

def writeText(text, dim):
    textList = text.split('\n')
    textList = formatLines(textList)
    finalImg = writeLine(textList[0], dim)
    for index in range(1,len(textList)):
        temp = writeLine(textList[index], dim)
        bckp = cv2.vconcat([finalImg, temp])
        finalImg = bckp

    cv2.imshow('result', finalImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    outFile = os.path.join('Output', 'result.jpg')
    cv2.imwrite(outFile,finalImg)



if __name__ == '__main__': # this section executes when only this file is being executed
	
    dim = tuple(map(int, input().split()))
    text = input()
    while text[-2:len(text)] != ':q':
        text += '\n' + input()
    text = text[:-2]
    writeText(text, dim)
    print('Done')
