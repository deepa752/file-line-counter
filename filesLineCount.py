import os, send2trash
path = os.getcwd()
count = 0
file_name= raw_input("Enter txt filename: ")
# extension= raw_input("enter the file extension which you want to count: ")
files= open(filename, "r")
data= files.readlines()
ignore_file_list=[]

for line in data:
    line=line.split("\n")
    if line[0]!='':
        ignore_file_list.append(line[0])

countable_files = []
for folderName, subfolders, filenames in os.walk(path):
    for folder in subfolders:
        if folder in ignore_file_list:
            send2trash.send2trash(folderName+"/"+folder)
    for main_file in filenames:
        if main_file in ignore_file_list:
            print "i will ignore this file", main_file
        else:    
            if main_file not in countable_files:
                    countable_files.append(main_file)
                # if extension in main_file:
                    print main_file
                    files = open(folderName+"/"+main_file , "r")
                    data = files.readlines()
                    for i in data:
                        count+=1
                    print count
print count                        