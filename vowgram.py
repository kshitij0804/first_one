a=input()
c=set()
l=['a','e','i','o','u']
for i in a:
    if(i in l):
        c.add(i)
if(len(c)==5):
    print('vow')
else:
    print('no')
