import easyocr
reader = easyocr.Reader(['kn']) # this needs to run only once to load the model into memory
result = reader.readtext('kanimg.jpg')

finaltext=""

for coord,text,prob in result:
    for ch in text:
        if ch.isdigit():
            finaltext+=" "
        else:
            finaltext+=ch
    finaltext=finaltext+" "

print(finaltext)

with open('output2.txt','w',encoding='utf-8') as file:
    file.write(finaltext)