file = open("in.txt", "r")
newFile = open("fixed.txt", "w")
lastline = "q"
for line in file:
    if not '[' in line:
        newFile.write(line)
    if (line == "\n" ) and ("[" in lastline):
        newFile.write("<endoftext>")
    lastline = line
newFile.close()
