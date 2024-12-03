#Q2. Slice the the string from b to d. 
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaapiwwwocnnnaioapuapoiuaopiuaodaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

b = s.index('b')
d = s.index('d')
words = s[b:d+1]
print (words)
