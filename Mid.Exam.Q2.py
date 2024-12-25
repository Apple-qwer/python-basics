G = ['Albert Einstein', 'Stephen Hawking', 'Ralph Emerson', 'Antoine Lavoisier', 'Junyeong F. Ahn', 'Justin Python Lee', 'Richard Feynman']

# Write your code
Modified = []
for name in G: 
    parts = name.split()
    Name = parts[0] + ' ' + parts [-1]
    Modified.append(Name)
print (Modified)