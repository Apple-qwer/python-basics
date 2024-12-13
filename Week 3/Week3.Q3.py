x = input("Put in the sentnece: ")
y = -1
for letter in (x):
    y += 1 
    if x[y:y+13] == 'advertisement' or x[y:y+13] == "Advertisement":
            print (f"{x} is spam")
            break
else: 
      print (f"{x} is legitamate")