#Program 3: Palindrome number program using while loop

Num = int(input("Enter a value:"))  
Temp = num  
Rev = 0  
while(num > 0):  
    dig = num % 10  
    revrev = rev * 10 + dig  
    numnum = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")


#Enter the value: 2551
#This value is not a palindrome number!

#Enter the value: 1221
#This value is a palindrome number!
