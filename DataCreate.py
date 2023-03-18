file = open("in.txt", "r")
newFile = open("gamefiles.txt", "w")
lastline = "q"
for line in file:
    if not '[' in line:
        newFile.write(line)
    if (line == "\r\n") and (lastline == "\r\n") :
        newFile.write("<endoftext>")
    lastline = line
newFile.close()
