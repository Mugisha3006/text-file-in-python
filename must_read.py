doc_path = "must_read.txt"

#opening file in read mode
doc = open(doc_path, "r")

#reading entire content of the file
content = doc.read()

#closing file
doc.close()

#print the content
print(content)
