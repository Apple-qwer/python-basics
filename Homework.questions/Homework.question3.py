#Q3. In the list [910, 11, 3], add the following numbers 
      #[2394, 12390237, 11272, 2309, 23499, 8189270, 823732, 234, 1324, 389025, 
      #9902, 2389, 2304, 2039, 1929, 9485, 8388, 82847]
      #then print the 5th biggest number from the list.
        
li = [910, 11, 3] 
li.extend([2394, 12390237, 11272, 2309, 23499, 8189270, 823732, 234, 1324, 389025, 9902, 2389, 2304, 2039, 1929, 9485, 8388, 82847])
newlist = []
for ele in li:
    if isinstance(ele,list):
        for nested_ele in ele:
            newlist.append(nested_ele)
        else:
            newlist.append(ele)

newlist.sort()
num = newlist[5]
print (num)
