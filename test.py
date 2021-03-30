import codecs

def search(file):
    fd = open(file,"r")
    fd = codecs.open(file,mode="r",encoding="utf-8")
    text = fd.readlines()
    fd.close()
    arr = []
    for lines in text:
        lines.replace("\u00A0"," ")
        arr.append(lines)
    print(arr)
        
    
