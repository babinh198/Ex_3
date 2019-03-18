
file_name = ["newfile.txt", " photoshop.psd.txt.docx"]
result =[]
for index in range(len(file_name) - 1, -1, -1):
    if file_name[index] == ".":
        result.append(file_name[index-1::-1])
        break   
  
result = result[0][::-1]
print(result)


## newfile, photoshop.psd.txt
