import os
import shutil
import addNum, fileRewrite

# directory = "asl_pondering_sentenceLevel30"
#
# parent_dir = "/Users/aislin/Desktop/asl/processing/"
#
# path_new = os.path.join(parent_dir, directory)
# # creating new folder
# os.mkdir(path_new)
# print("Directory '% s' created" % directory)
#
# print(path_new)
# os.chdir(path_new)
# cwd = os.getcwd()
# print("Current working directory is:", cwd)
# # make a copy of the video
# src = "/Users/aislin/Desktop/asl/asl_ponderings/30/hannahtest.mp4"##modify path on this
# dst = cwd
# shutil.copy2(src, dst)
# initial = "/Users/aislin/Desktop/asl/processing/asl_pondering_sentenceLevel30/hannahtest.mp4"##modify asl_pondering_sentenceLevel15 after this
# final = "/Users/aislin/Desktop/asl/processing/asl_pondering_sentenceLevel30/hci01.mp4"##modify this
# os.rename(initial, final)
# # make a copy of the text file
# txt_src = "/Users/aislin/Desktop/asl/asl_ponderings/30/hannahtest.txt"##change this
# txt_dst = "/Users/aislin/Desktop/asl/processing/testFile3.txt"
# shutil.copy2(txt_src, txt_dst)
# # done just made the copy of the text file
#
# # adding number to testFile3
# addNum.addNum(txt_dst)
# originalScript = "/Users/aislin/Desktop/asl/processing/testFile3.txt"
# dst_file_path = "/Users/aislin/Desktop/asl/processing/asl_pondering_sentenceLevel29"
# shutil.copy2(originalScript, dst_file_path)
# copy file3 to file1 and file2
file3 = "/Users/aislin/Desktop/asl/processing/testFile3.txt"
file1 = "/Users/aislin/Desktop/asl/processing/testFile1.txt"
file2 = "/Users/aislin/Desktop/asl/processing/testFile2.txt"
shutil.copy2(file3, file1)
shutil.copy2(file3, file2)

# checking current directory
cwd_curr = os.getcwd()
print("Current working directory is:", cwd_curr)

# running rewrite
video = "/Users/aislin/Desktop/asl/processing/asl_pondering_sentenceLevel30/hci01.mp4"##modify this [after asl_pondering_sentenceLevel15]
fileRewrite.fileProcess(file1, video)
