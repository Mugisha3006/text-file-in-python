file_path = "read.txt"

#open file in read mode
file = open(file_path, "r")

#read entire content of the file
flip = file.read()

#close file
file.close()

#print file
print(flip)