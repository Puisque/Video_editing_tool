
def addNum(fileName):
    with open(fileName, 'r') as f:
        listofLines = f.readlines()
        count = 0
        for i in range(0, len(listofLines)):
            line = listofLines[i]
            if len(line) == 30 and line[13:16] == "-->":
                count+=1
                if len(listofLines[i-1])==1:#empty line
                    listofLines[i-1] = str(count) + "\n"
    with open(fileName, 'w') as f:
        f.writelines(listofLines)



# if __name__ == '__main__':
#     addNum('testFile3.txt')