## If you have to print last digit of any number
## divide the last digit by % 10
## if you have to make any number small 
## than divide it by 10 [ x/10 ]
## when you dont know how much big the number is
## or you dont know till when the loop will work
## so in that case use WHILE LOOP
## when you know till when the loop will work
## so in that case use FOR LOOP

#print digits of number:-

num = int(input("Enter any number: "))

while(num > 0):
   #we want unit digits that why finding remainder 
    remainder = num % 10
   #print that digit 
    print(remainder)
   #decrease the number by removing unit digit 
    num = num//10
   #here used double slash (//) to get integer value not decimal value.