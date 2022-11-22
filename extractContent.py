
def contentExtract(fileName):
    with open(fileName, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)-2):
            line = lines[i]

            if len(line) <= 10 and len(line) != 1:
                contentString = lines[i+2]
                print(contentString)
                newName = "message{}.txt".format(line.strip())
                print(newName)
                newFile = "file{}".format(line.strip())
                print(newFile)
                with open(newName, 'w') as newFile:
                    newFile.write(contentString)


if __name__ == '__main__':
    contentExtract('testFile2.txt')