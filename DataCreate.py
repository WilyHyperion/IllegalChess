file = open("in.txt", "r")
newFile = open("fixed.txt", "w")
lastline = "q"
for line in file:
    if not '[' in line:
        newFile.write(line)
<<<<<<< HEAD
    if (line == "\r\n") and (lastline == "\r\n") :
=======
    if (line == "\n" ) and ("[" in lastline):
>>>>>>> 0a3687454545490fe2954cb3b10970dab8075fd7
        newFile.write("<endoftext>")
    lastline = line
newFile.close()
