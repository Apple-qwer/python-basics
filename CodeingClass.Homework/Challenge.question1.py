Justin_and_Jun = [ {'Justin' : 'smart', 'Jun' : 'foolish'}, {'Justin' : 'young', 'Jun' : 'old'}]

new_list = []

def values(x): 
   if isinstance(x, dict):
     return list(x.values())
  
new_list = list(map(values, Justin_and_Jun)) 

final_list = []
for ele in new_list:
   for nested_ele in ele:
      final_list.append(nested_ele) 

print(final_list) 