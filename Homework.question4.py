# Q5. Find parlindrome of the given strings. 

#Approach 1

S = 'Xiplisalsjdk akfsLksi iskLsfka kdjslasilpiX'

x = S == S[::-1]

if x == True:
    print ("This is palindrome")
elif x == False:
    print ("This isn\'t palindrome")
# else:
    # print ("This isn\'t palindrome")


# Approach 2 
s = 'sadfsadfjsdia;fjklsda'
# s = 'Xiplisalsjdk akfsLksi iskLsfka kdjslasilpiX'
length = len(s)

a = s[:length // 2]

b = s[length - 1 : length // 2 : -1]

if a == b:
    print ("This is palindrome")
else: 
    print ('This isn\'t palindrome')








