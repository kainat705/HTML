#strings
text="random strings with a lots of character"
print( text[0-1])
#slice of a string
text2="I dont understand python"
print (text[0:1])
fruit ="pineaple"
print(fruit[:4])
print(fruit[4:])
#strings immutable
mesage="apple is red"
# message[2]="l"
#strings method
print (text.index("my"))
#str upr,str lwr

print(text.uper())
print(text.lower())

answer ='YES'
if answer.lower() == "yes":
    print("user said yes")
#str adv meth0ds
#to join 2 str=(.join)

print(text+"-"+ text2)
print("-".join(text ,text2))

#split ,broke into word by word
print ((text.split))
print((text.isalnum))
#strings formatting
name ="kainat"
number = (len name)*3
print("hello{},you have won {}pounds and your name is{}".format(name,number))

price =7.5
with_tax = price*1.09
print(price,with_tax)
7.5 
print("base price:${:}")
    
    


#def
def to_celsius(x):
  return(x-32)*5/9
for x in range(o,101,10):
  print("{:>3})F|{:>6.2f}C.format(temp,to_celsius(temp))")
