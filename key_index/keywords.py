from bs4 import BeautifulSoup
import html5lib
import re

def getKeywords(path):
    keywordsHTML = getMetaTags(path)[1]
    
    isInContent = False
    numOfQuotes = 0
    keywordsHTML = keywordsHTML.lower()
    i = 0    
    keywords = ""

    while i < len(keywordsHTML):
        if not isInContent:
            if keywordsHTML[i: i+7] == "content":
                i += 7
                isInContent = True
            else:
                i += 1
        else:
            if numOfQuotes == 0:
                if keywordsHTML[i] == "\"":
                    numOfQuotes += 1
                i += 1
            else:
                if keywordsHTML[i] == "\"" and numOfQuotes == 1:
                    break
                else:
                    keywords += keywordsHTML[i]
                    i += 1
    keywords = keywords.split(",")
    response = []
    for keyword in keywords:
         response.append(keyword.strip())
    return response

def getMetaTags(path):
    f = open(path,'r+')
    c = f.read()
    f.close()    
    
    original = c
    c = c.lower()
    print(c)
    keys = ["", "", "", ""]
    numBrackets = 0
    i = 0
    j = 0
    while i < len(c):
        if c[i] == '[':
            numBrackets += 1
            if numBrackets == 1:
                i += 1
                continue
        if numBrackets == 0:
            if j == 3:
                if c[i: i+5] == "title":
                    while c[i] != ">" and i < len(c):
                        i += 1
                    numBrackets += 1
            i += 1
            continue
        if c[i] == ']':
            numBrackets -= 1

            if numBrackets == 0:
                i += 1
                j += 1
                continue
        
        if c[i] == "<" and j == 3:
            originalI = i
            i += 1
            while (c[i] != "/" or c[i] != "<") and i < (len(c) - 5):
                i += 1
            if c[i] == "<":
                i = originalI
            else:
                while c[i: i + 5] != "title" and i < len(c):
                    i += 1
                if i > len(c):
                     i = originalI
                else:
                     break
        keys[j] += original[i] 
        i += 1
    print(keys)
    return keys
    
    

def getTitle(path):
    f = open(path,'r+')
    c = f.read()
    f.close()

    return getMetaTags(path)[3]
