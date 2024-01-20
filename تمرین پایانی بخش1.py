
AA=input("what_s your name?...")
a=int(input("how old are you?....."))
A=int(input("how much is your salary?...."))
aa=float(input("what is yor total score?....."))
BB=input("what_s your name?...")
b=int(input("how old are you?....."))
B=int(input("how much is your salary?...."))
bb=float(input("what is yor total score?....."))
ccc=input("what_s your name?...")
c=int(input("how old are you?......"))
C=int(input('how much is your salary?.....'))
cc=float(input("what is yor total score?....."))
DD=input("what_s your name?...")
d=int(input("how old are you?....."))
D=int(input("how much is your salary?...."))
dd=float(input("what is yor total score?....."))

x=((aa+bb)//2-(cc+dd)//2)
xx=((aa+bb+cc+dd)//4)

print((a+b)/2)
print((((a*365)*24)*60)*60)
print(((a*6)*60)*60)
print(x,xx)
print(x%2,xx%2)

if aa>=17.50:
    print("great")
elif aa>15.10:
    print("good")
elif aa>=10.00:
    print("not bad")
else:
    print("very bad")

if B>=12000000 and bb>=16.02:
    print("right")
elif B>=12000000 and bb<=15.50:
    print("wrong")
elif B>=7000000 and bb>=15.50:
    print("not bad")
else:
    print("soory")

if x<0 or x%2==0:
    print("neg or even")
elif x<0 and x%2==0:
    print("yes")
elif x>0 or x%3==0:
    print("pos or odd")
elif x>0 and x%3==0:
    print("yes_right")
elif x<0 and x%2!=0:
    print("ok")
elif x>0 and x%3!=0:
    print("oookkk")
elif x>=xx or x<=xx:
    print("one right")
else:
    print("nothing")

if x>0 and xx>0:
    print("even")
elif x<0 and xx<0:
    print("odd")
else:
    print("nothing")

if x%2!=0 and xx%2!=0:
    print("odd")
elif x%3!=0 and xx%3!=0:
    print("even")
elif x%2==0 or xx%2==0:
    print("a even")
else:
    print("nothing")

 #.......................................    

a,b,c=3,4,5

if (a**2)+(b**2)==(c**2) or (c**2)+(b**2)==(a**2) or (a**2)+(c**2)==(b**2):
    print("ok")
elif (a**2)+(b**2)==(c**2) and (a**2)+(c**2)==(b**2) and (c**2)+(b**2)==(a**2):
    print("this right")
else:
    print("nothing")

if a+b<c or a+c<b or b+c<a:
    print("somthing wrong")
elif a+b<c and a+c<b and b+c<a:
    print("all wrong")
elif a+b>c or a+c>b or b+c>a:
    print("simthing right")
elif a+b>c and a+c>b and b+c>a:
    print("all right")
else:
    print("sorry")

#........................................

days=int(input("enter a number......."))
days=(input("enter a day......."))

if days==1:
    print("saturday")
elif days==2:
    print("sunday")
elif days==3:
    print("monday")
elif days==4:
    print("tuesday")
elif days==5:
    print("wednsday")
elif days==6:
    print("thersday")
elif days==7:
    print("friday")
else:
    print("nooo")

if days=="saturday":
    print("1")
elif days=="sunday":
    print("2")
elif days=="monday":
    print("3")
elif days=="tuesday":
    print("4")
elif days=="wednsady":
    print("5")
elif days=="thersday":
    print("6")
elif days=="friday":
    print("7")
else:
    print("nothing")