#there are too many codes from string libraries
#some expamples from string libraries:

#text.find(x) ->for searching a position of a number or string 
text = "Hello world:   0.8475"
#identify the position of 0 in the string line of text
#position=15(integer number)
positionx=text.find('0')
#number=float number in text starting in positionx and finishing in
#the end of the string (0 is in positionx=15 and 5 in the end)
number=float(text[positionx:])
#print the number of the string 
print(number) 

#capitalizing strings
text = "alejandro"
Text=str.capitalize(text)
#will print alejandro Alejandro
print (text,Text)

#replace
text='Hello alejandro'
newtext=text.replace('alejandro','juana')
ntext=text.replace('a','4')
#print='Hello alejandro' newtext='Hello juana' ntext='Hello 4lej4ndro'
print(text,newtext,ntext)

#startswith
text='Hello alejandro'
#print=True (because the text starts with Hello)
print(text.startswith('Hello'))

#newline 