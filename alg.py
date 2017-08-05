import re
a= "Samsung GaLaxy(543)"
print(a)
a=re.sub(r'\(.+?\)\a*', '', a)
a= re.split(r'[^\w]',a, re.I| re.M)
a= ''.join(a)
a= str.lower(a)
print(a)
a= re.split(r'[^\w]',a, re.I| re.M)
a= ''.join(a)
a= str.lower(a)
a=re.sub(r'\(.+?\)\a*', '', a)
print(a)