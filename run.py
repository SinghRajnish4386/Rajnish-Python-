f = open("filehandling/input.txt","r")
lines = f.readlines()

output = open("filehandling/output.txt","w")

for elem in lines:
    tmp = elem.strip('\n')
    n = int(tmp)

    ans = n*n 

    output.write(str(ans) + "\n")

f.close()
output.close()
