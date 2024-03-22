import easyocr
reader = easyocr.Reader(['hi']) # this needs to run only once to load the model into memory
result = reader.readtext('hq720.jpg')

finaltext=""

for coord,text,prob in result:
    finaltext+=text+" "

print(finaltext)

with open('output.txt','w',encoding='utf-8') as file:
    file.write(finaltext)