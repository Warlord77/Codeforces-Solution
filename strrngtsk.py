n = raw_input()
 
p = n.translate(None, 'aeioyuAEIOUY')
a = p.lower()
print "."+".".join(a)



