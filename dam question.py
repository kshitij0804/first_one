n=int(input('enter the number of places'))
l=0
ml=0
a=0
b=0
lit=[]
mil=[]
q=0
for i in range(1,n+1):
    liters=int(input('water in liters'))
    lit.append(liters)
    milli=int(input('water in milliters'))
    mil.append(milli)
   


a=sum(lit)
b=sum(mil)
q=b%1000


#print(lit)
#print(mil)

l=list(map(lambda n:n%1000,mil))

print(l)

print(a)
print(b)

ml=sum(l)
print(ml)


v=ml-q*100
w=a+v//1000


print(v)
print(w)



2.)

n=int(input())
l=0
ml=0
a=0
b=0
lit=[]
mil=[]
t=0
u=0


for i in range(1,n+1):
    liters=int(input())
    lit.append(liters)
    milli=int(input())
    mil.append(milli)



a=sum(lit)
b=sum(mil)
q=b%1000

l=list(map(lambda n:n%1000,mil))

ml=sum(l)
if(ml>=1000):
    u=ml//1000
    t=ml-u*1000
    
v=ml-q
w=a+v//1000

print(w)
print(t)




Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters12
water in milliters1200
water in liters17
water in milliters1800
[12, 17]
[1200, 1800]
[200, 800]
29
3000
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters12
water in milliters1200
water in liters17
water in milliters1800
[12, 17]
[1200, 1800]
[200, 800]
29
3000
1000
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters12
water in milliters200
water in liters17
water in milliters400
[12, 17]
[200, 400]
Traceback (most recent call last):
  File "C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py", line 25, in <module>
    if(mil>=1000):
TypeError: '>=' not supported between instances of 'list' and 'int'
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters200
water in liters18
water in milliters700
[17, 18]
[200, 700]
0
35
900
Traceback (most recent call last):
  File "C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py", line 32, in <module>
    ml=sum(l)
TypeError: 'int' object is not iterable
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters200
water in liters18
water in milliters700
[17, 18]
[200, 700]
35
900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters700
[17, 18]
[1200, 700]
35
1900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters200
water in liters18
water in milliters700
[17, 18]
[200, 700]
[200, 700]
35
900
900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
900
2900
2935
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
2900
2935
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
2900
37900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
2900
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
2000
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
[17, 18]
[1200, 1700]
[200, 700]
35
2900
900
2000
37
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters1200
water in liters18
water in milliters1700
900
37
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places2
water in liters17
water in milliters600
water in liters18
water in milliters200
800
35
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places3
water in liters2
water in milliters500
water in liters3
water in milliters400
water in liters1
water in milliters700
1600
6
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places3
water in liters2
water in milliters500
water in liters3
water in milliters400
water in liters1
water in milliters700
[2, 3, 1]
[500, 400, 700]
[500, 400, 700]
6
1600
1600
0
6
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places3
water in liters2
water in milliters500
water in liters3
water in milliters400
water in liters1
water in milliters700
[500, 400, 700]
6
1600
1600
0
6
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places3
water in liters2
water in milliters500
water in liters3
water in milliters400
water in liters1
water in milliters700
[500, 400, 700]
6
1600
1600
0
6
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places3
water in liters2
water in milliters500
water in liters3
water in milliters400
water in liters1
water in milliters700
[500, 400, 700]
6
1600
1600
1599
7
>>> 
 RESTART: C:/Users/KSHITIJ/AppData/Local/Programs/Python/Python37-32/afmndfl.py 
enter the number of places3
water in liters2
water in milliters500
water in liters3
water in milliters400
water in liters1
water in milliters700
[500, 400, 700]
6
1600
1600
1000
7
>>> 
