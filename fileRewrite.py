def fileProcess(fileName, videoName):
    with open(fileName, 'r+') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]

            if len(line) <= 10 and len(line) != 1:
                num = line
                timeString = lines[i + 1]

                startTime = timeString[0:12]
                endTime = timeString[17:29]

                # make new folder for sentence level content
                f.write("\n")
                newFolder = "sentence{}".format(num.strip())
                f.write("mkdir" + " " + newFolder)

                # enter the new folder for storage
                f.write("\n")
                f.write("cd" + " " + newFolder)
                newName = "cut{}.mp4".format(num.strip())
                print(newName)
                # print(num)
                newString = "ffmpeg -ss " + startTime + " -i " + videoName + " -to " + endTime + " -c copy -copyts " + newName
                print(newString)
                f.write("\n")
                # storing sentence level video segments
                f.write(newString)

                # transfering text content to the correct folder
                f.write("\n")
                message_txt = "message{}.txt".format(num.strip())
                old_path = "/Users/aislin/Desktop/asl/processing/" + message_txt
                new_path = "/Users/aislin/Desktop/asl/processing/asl_pondering_sentenceLevel30/" + newFolder + "/"
                f.write("mv" + " " + old_path + " " + new_path)

                # further, cut into frames
                # ffmpeg -i cut21.mp4 -r 1 output_%04d.jpeg
                f.write("\n")
                f.write("ffmpeg -i " + newName + " -r 1 output_%04d.jpeg ")

                #return back to the root file
                f.write("\n")
                f.write("cd /Users/aislin/Desktop/asl/processing/asl_pondering_sentenceLevel30")
                # ending of one action
                f.write("\n")
                f.write("    ")

# #
# # if __name__ == '__main__':
# #
#     fileProcess('testFile1.txt', "29.mp4")
