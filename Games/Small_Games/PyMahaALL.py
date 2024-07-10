'''Python Programming Examples'''
'''This section covers the basic and simple python programming examples.'''

print("All python COde here")


#Sample Hello World Program
def hello():
    print('hello world!')
    print('i am Maha , Speed 0.004kbps memory 1Mb')
hello()


#How to add Two Numbers
def sum(a,b):
    print(a+b)
print('\nHow to add Two Numbers')
sum(2,7)


#Arithmetic Operations
def oper(a,b):
    print('add=',a+b)
    print('sub=',a-b)
    print('mul=',a*b)
    print('div=',a/b)
    print('modul=',a%b)
    print('div int=',a//b)
print('\nArithmetic Operations')
oper(8,4)


#Calendar Program
def cal():
    print("SUN\tMON\tTUE\tWED\tTHUR\tFRI\tSAT\n",end='\n')
    for i in range(1,31):
        print(i,end='\t')
        if(i%7==0):
            print('\n')
print('\nCalendar Program')
cal()


#Cube of a Number
def cube(a):
    print(a*a*a)

print('\nCube of a Number no=3')
cube(3)

#Largest of Two Numbers
def lar2(a,b):
    if(a>b):print(a,'is larger')
    else:print(b,'is larger')
print('\nLargest of Two Numbers')
lar2(8,1)
#Largest of Three Numbers
def lar3(a,b,c):
    if(a>b and a>c):print(a,'id larger')
    elif(b>c):print(b,'is larger')
    else:print(c,'is larger')
print('\nLargest of Three Numbers')
lar3(2,3,4)

#Print Natural number from 1 to N
def natu(n):
    for i in range(1,n+1):
        print(i,end='\t')
print('\nNatural number from 1 to N')
natu(10)
#Print Natural Number in Reverse Order
def natr(n):
    i=0
    while(i!=n):
        print(n-i,end='\t')
        i+=1
print('\nNatural number from Reverse Order')
natr(10)
#Sum and Average of Natural Numbers
def avgn(n):
    s=0
    for i in range(0,n+1):
        s=s+i
    avg=s/n
    print('sum=',s,'avg=',avg)
print("\nSum and Average of Natural Numbers")
avgn(100)

#Leap Year
def leap(n):
    if(n%4==0):
        print("leap year")
    else:print('non leap year')
print("\nLeap Year")
leap(2020)

#Odd or Even
def odRev(n):
    if(n%2==0):print('the number',n,'is even')
    else:print('the number',n,'is odd')
print("\nOdd or Even =>7657685")
odRev(7657685)

#Even Numbers from 1 to 100
def evn(n):
    for i in range(1,n+1):
        if(i%2==0):print(i,end='\t')
print("\nEven Numbers from 1 to 100")
evn(100)
#Odd Numbers from 1 to 100
def odn(n):
    for i in range(1,n+1):
        if(i%2!=0):print(i,end='\t')
print("\nOdd Numbers from 1 to 100")
odn(100)
#Positive or Negative
def PoN(n):
    if(n>0):print('Positive')
    else:print('Negative')
print("\nPositive or Negative =>-2")
PoN(-2)
#Profit Or Loss

#Square of a Number
def sqr(n):
    print(n*n)
print("\nSquare of a Number =>4")
sqr(4)
#Square root of a Number
import math
def sqrt(n):
    print(math.sqrt(n))
print("\nSquare root of a Number =>44")
sqrt(44)
#Compound Interest

#Number is Divisible by 5 and 11
def divi(n):
    if(n%5==0):print('The No. ',n,'is divisible by 5',end=' ')
    else:print('The No. ',n,'is not divisible by 5',end=' ')
    if(n%11==0):print('also divisible by 11')
    else:print('and not divisible by 11')
print("\nNumber is Divisible by 5 and 11=>44")
divi(44)
#Power of a Number
def pow(a,b):
    print(a**b)
print("\nPower of a Number =>2,5")
pow(2,5)
#Multiplication Table
def Table(n):
    for i  in range(1,21):
        print(n,'x',i,'=',i*n)
print("\nMultiplication Table =>18")
Table(18)
#Roots of a Quadratic Equation
def roots():
    a=int(input("Enter a :"))
    b=int(input("Enter b :"))
    c=int(input("Enter c :"))
    b1=b*b
    c1=4*a*c
    D=b1-c1
    print('roots of equation',a,'x^2+',b,'x+',c,'is',end=' ')

    if(D>=0):
        r1=(-b + math.sqrt(D) )/(2*a)
        r2=(-b - math.sqrt(D) )/(2*a)
        print(r1,'and',r2)
    else:
        print(-b/2,'+',(math.sqrt(-D)/2),'i and ',-b/2,'-',(math.sqrt(-D)/2),'i')
print("\nRoots of a Quadratic Equation")
roots()
#Student Grade
def grade(n):
    if(n<=100 and n>=0):
        print('GRADE :',end='')
        if(n>=75):
            print('Excellent')
        elif(n>=50):
            print('1 st CLASS')
        elif(n>=35):
            print('2 nd CLASS')
        elif(n<35):
            print("FAIL")
    else:print('INVAlID INPUT')
print("\nStudent Grade =>78")
grade(78)
#Simple Interest
#Electricity Bill
#Total Average and Percentage of Five Subjects
def prog():
    a = [0]
    sumofall = 0
    for i in range(1,6):
        k=int(input('Enter subject Marks'))
        a.append(k)
    for i in range(1,6):
        sumofall += a[i]
    averagemark = sumofall/5
    print(averagemark)
print("\nTotal Average and Percentage of Five Subjects")
prog()



'''Python Sum Programs'''
'''The following Python programs will find'''
#Sum of Natural Numbers
def snat(n):
    s=n*(n+1)/2
    print(s)
'''Advanced Python Number Programs'''
'''The following python programming examples are helpful to work with Numbers'''
#Armstrong Number
def Arm(n):
    a=b=n
    c=su=0
    while(b!=0):
        b=b//10
        c+=1
    while(a!=0):
        k=a%10
        l=1
        for i in range(c):
            l=k*l
        su=su+l
        a=a//10
    if(su==n):print('Armstrong')
    else:print('not')
print("\nArmstrong Number =>entered 153")
Arm(153)
#Count Number of Digits in a Number
def Cou(n):
    c=0
    while(n!=0):
        n=n//10
        c+=1
    print('There are',c,'digits')
print("\nCount Number of Digits in a Number => 15165")
Cou(15165)
#Fibonacci Series program
def fib(n):
    print('0\t1',end='\t')
    t1=0
    t2=1
    for i in range(n-2):
        t3=t1+t2
        print(t3,end='\t')
        t1=t2
        t2=t3
print("\nFibonacci Series program =>13")
fib(13)
#Factors of a Number
def ftr(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end='\t')
print("\nFactors of a Number =>36")
ftr(36)
#Factorial of a Number
def fac(n):
    fac=1
    for i in range(1,n+1):
        fac *= i
    print(fac)
print("\nFactorial of a Number =>5")
fac(5)
#First two Digits of a Number
def fid(n):
    c=0
    k=1
    a=n
    while(a!=0):
        a=a//10
        c+=1
    for i in range(c-2):
        k=10*k
    m=n//k
    print(m)
print("\nFirst two Digits of a Number")
fid(155456)
#GCD of Two Numbers
def gcd(n,m):
    if(n>m):w=m
    else:w=n
    for i in range(1,w+1):
        if(n%i==0 and m%i==0):gcd=i
    print(gcd)
print("\nGCD of Two Numbers,=>of 12,78 ")
gcd(12,78)
#Last Digit in a Number
#LCM of Two Numbers
def lcm(n,m):
    if(n>m):w=n
    else:w=m
    while(True):
        if(w%n==0 and w%m==0):
            lcm=w
            break
        w += 1
    print(lcm)
print("\nLCM of Two Numbers ,=>of 12,78 ")
lcm(12,78)
#Natural Numbers in Reverse Order
def NaturalRev(n):
    for i in range(n,0,-1):
        print(i,end='  ')
print("Natural Numbers in Reverse Order")
NaturalRev(100)
#Palindrome Program
#Palindrome numbers from 1 to 100
#Perfect Number
#Prime Number
#Prim Numbers from 1 to 100
#Prime Factors of a Number
#Reverse a Number
#Strong Number
#Strong Numbers from 1 to 100
#Sum of Digits in a Number
#Swap Two Numbers


'''Python Programming examples on Characters'''
'''Below python examples are used to work on characters'''
#Alphabet or not
def Alp():
    a=(input("Enter a charecter : "))
    if((a>='a' and a<='z') or (a>='A' and a<='Z')):
        print('Alphabet')
    else:print('Not an Alphabet')
print("\nAlphabet or not")
Alp()
#Alphabet or Digit
def AoD():
    a=(input("Enter a charecter : "))
    if((a>='a' and a<='z') or (a>='A' and a<='Z')):
        print('Alphabet')
    elif(a>='0' and a<='9'):
        print('Digit')
    else:
        print('Not an Alphabet or Digit')
print("\nAlphabet or Digit")
AoD()
#Character is an Alphabet, Digit or Special Character

#Digit or Not
#Lowercase or not
#Lowercase or Uppercase
#Uppercase or not
#Vowel or Consonant
def vow():
    a=(input("Enter a charecter : "))
    if((a>='a' and a<='z') or (a>='A' and a<='Z')):
        if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
            print('vowel')
        else:
            print('constant')
print("\nVowel or Consonant")
vow()


'''Python String Programs'''
'''The following are the list of python programming examples on strings.'''
#ASCII Value of a Single Character
def asc():
    a=(input("Enter a charecter : "))
    print(ord(a))
print("\nASCII Value of a Single Character")
asc()
#ASCII Value of Total Characters in a String
def ascii():
    import array
    ele=str(input('enter'))
    for i in range(len(ele)):
        print("ascii value of",ele[i],'is :',ord(ele[i]))
print("\nASCII Value of Total Characters in a String")

ascii()

#Concatenate Strings

#Convert String to Uppercase
def STRtUpp():
    s=str(input("Enter the String"))
    for i in range(len(s)):
        if(s[i]>='a' and s[i]<='z'):
            val=ord(s[i])-32
            k=chr(val)
            print(k,end='')
        else:
            print(s[i],end="")
print("\nConvert String to Uppercase")
STRtUpp()
#Convert String to Lowercase
def STRtLwr():
    s=str(input("Enter the String"))
    for i in range(len(s)):
        if(s[i]>='A' and s[i]<='Z'):
            val=ord(s[i])+32
            k=chr(val)
            print(k,end='')
        else:
            print(s[i],end="")
print("\nConvert String to Lowercase")
STRtLwr()
#Copy String
def cpystr():
    s=str(input("Enter the String"))
    news="\0"
    rev="\0"
    for i in range(len(s)):
        news = s[i] + news
    for i in range(len(s)):
        rev = news[i] + rev
    print(rev)
print("\nCopy String")
cpystr()
#Counting Occurrence of a Character in a String
def str_Occ():
    s=str(input("Enter the String"))
    c=str(input('Enter charecter to be searched'))
    occ=0
    for i in range(len(s)):
        if(s[i]==c):
            occ=occ+1
    print("no of times occoured : ",occ)
print("\nCounting Occurrence of a Character in a String")
str_Occ()
#Count Total Characters in a String
def tcha():
    s = str(input("Enter the String"))
    t=0
    for i in s:
        t=t+1
    print('Total char is ',t)

print("\nCount Total Characters in a String")
tcha()

#Count Total Number of Words in a String
def tchc():
    s = str(input("Enter the String"))
    t=0
    for i in range(len(s)):
        if(s[i]==' '):
            t+=1
    print('Total char is ',t+1)
print("\nCount Total Number of Words in a String")
tchc()

#Counting Vowels in a String
#Count Vowels and Consonants in a String
#Count Alphabets Digits and Special Characters in a String
#First Occurrence of a Character in a String
#Last Occurrence of a Character in a String
#Palindrome or Not
#Print Characters in a String
#Replace Blank Space with Hyphen in a String
#Replace Characters in a String
#Remove Odd Characters in a String
#Remove Odd Index Characters in a String
#Removing First Occurrence of a Character in a String
#Remove Last Occurred Character in a String
#Reverse a String
#String Length
#Total Occurrence of a Character in a String
#Toggle Characters Case in a String
#Add two Lists
#Arithmetic Operations on Lists
#Count Even and Odd Numbers in a List
#Largest Number in a List
#Largest and Smallest Number
#Length of a List
#Print Elements in a List
#Print Even Numbers in a List
#Printing Odd Numbers
#Print Positive Numbers
#Print Negative Numbers
#Put Even and odd Numbers in Separate List
#Put Positive and Negative Numbers in Separate List
#Reverse List Items
#Second Largest Number in a List
#Sort Elements in Ascending Order
#Smallest Element in a List
#Sum of All Elements
#Sum of Even and Odd Numbers in a List
#Python Dictionary Programs
#Add Key-Value Pair to a Dictionary
#Check if a Given key exists in a Dictionary
#Count words in a String using Dictionary
#Create Dictionary of keys from 1 to n and values are square of keys
#Create Dictionary of Numbers 1 to n in (x, x*x) form
#Map two lists into a Dictionary
#Merge Two Dictionaries
#Multiply All Items in a Dictionary
#Remove Given Key from a Dictionary
#Sum of Items in a Dictionary
'''Python Examples on Area and Volume'''
'''This sections covers python programs on Areas, Volume and Surface Area with examples'''
#Area
#Circle
#Diameter, Circumference, and Area Of a Circle
#Equilateral Triangle
#Check Triangle is Valid or Not
#Find angle of a Triangle if two angles are given
#Triangle
#Triangle area using base and height
#Trapezoid
#Area of a Rectangle using length and width
#Perimeter of a Rectangle using length and width
#Rectangle
#Right Angled Triangle
#Volume and Surface Area
#Sphere
#Cylinder
#Cube
#Cone
#Cuboid
#Python Programs on Series
#Sum of Arithmetic Progression Series
#Sum of Geometric Progression Series
#Find Sum of Series 1²+2²+3²+….+n²
#Sum of Series 1³+2³+3³+….+n³




'''Python Pattern Programs'''
'''The following Python Programming examples show you the pattern programs. This section uses Star patterns and 0, 1 patterns.'''



#Bubble Sort
def bsort():
    import array
    arr = array.array('i',[0])
    n=int(input("Enter no of array elements"))
    arr[0]=int(input("Enter"))
    for i in range(n-1):
        r=int(input("Enter"))
        arr.append(r)
    print('before Sorting')
    for i in range(n):
        print(arr[i],end='\t')
    for i in range(n):
        for j in range(n):
            if(arr[i]<arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print('\nafter Sorting')
    for i in range(n):
        print(arr[i],end='\t')

print("\nBubble Sort")
print("\n\tUncomment bsort fun in code !")
#bsort()

#1 and 0 in Alternative Columns
def col(n):
    for i in range(n):
        if(i%2==0):print('0',end=' ')
        else:print('1',end=' ')
    print()
print("\n1 and 0 in Alternative Columns")
col(8)
#1 and 0 in Alternative Rows
def row(n):
    for i in range(n):
        if(i%2==0):print('0',end='\n')
        else:print('1',end='\n')
    print()
print("\n1 and 0 in Alternative Rows")
row(8)
#Box Pattern of Numbers 1 and 0
def box(n):
    for j in range(n):
        for i in range(n):
            if(j%2==0):
                if(i%2==0):print('0',end=' ')
                else:print('1',end=' ')
            else:
                if(i%2==0):print('1',end=' ')
                else:print('0',end=' ')
        print(end='\n')
    print()
print("\nBox Pattern of Numbers 1 and 0")
box(8)
#Floyd’s Triangle
def floyd(n):
    k=1
    for i in range(n+1):
        for j in range(i):
            print(k,end=' ')
            k+=1
        print(end='\n')
print("\nFloyd’s Triangle")
floyd(9)
#Hollow Box Pattern of Numbers of 1 and 0
def hob(n):
    for i in range(n):
        for j in range(n):
            if((i==0 or i==(n-1)) or (j==0 or j==(n-1))):
                if(j%2==0):
                    if(i%2==0):print('0',end=' ')
                    else:print('1',end=' ')
                else:
                    if(i%2==0):print('1',end=' ')
                    else:print('0',end=' ')
            else:
                print(end='  ')
        print(end='\n')

print("\nHollow Box Pattern of Numbers of 1 and 0")
hob(10)
#Hollow Rectangle Star Pattern
def recs(n,m):
    for i in range(n):
        for j in range(m):
            if((i==0 or i==(n-1))or (j==0 or j==(m-1))):
                print('*',end=' ')
            else:print(end='  ')
        print(end='\n')

print("\nHollow Rectangle Star Pattern")
recs(8,16)
#Square Star Hollow Pattern
def sqs(n):
    for i in range(n):
        for j in range(n):
            if((i==0 or i==(n-1))or (j==0 or j==(n-1))):
                print('*',end=' ')
            else:print(end='  ')
        print(end='\n')
print('\nSquare Star Hollow Pattern')
sqs(5)
#Inverted Right Triangle of Numbers - invert Floyd’s Triangle
def floydi(n):
    k=1
    for i in range(n,0,-1):
        for j in range(i):
            print(k,end=' ')
            k+=1
        print(end='\n')
print("\nInverted Right Triangle of Numbers ")
floydi(9)
#Inverted Right Triangle Star Pattern
def StarInv(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('*',end=' ')
        print(end='\n')
print("\nInverted Right Triangle Star Pattern")
StarInv(10)
#Reverse Mirrored Right Triangle Star Pattern
def StarInvMirr(n):
    q = 0
    for i in range(n,0,-1):
        for j in range(i):
            print('*',end=' ')
        print(end='\n')
        q+=1
        print('  '*q,end='')
print("\nReverse Mirrored Right Triangle Star Pattern")
StarInvMirr(10)
#Increasing Star Pattern
def exs(n):
    for i in range(n):
        for j in range(i):
            print('*',end=' ')
        print(end='\n')
    print()
print("\nIncreasing Star Pattern")
exs(10)
#Mirrored Right Triangle Star Pattern
def exsi(n):
    q = n
    for i in range(n):
        for j in range(i):
            print('*',end=' ')
        q -= 1
        print(end='\n')
        print('  '*q,end='')
    print()
print("\nMirrored Right Triangle Star Pattern")
exsi(10)
#Triangle iso
def TriIso(n):
    q = n
    for i in range(n):
        for j in range(i):
            print('*',end=' ')
        q -= 1
        print(end='\n')
        print(' '*q,end='')
    print()
print("\nTriangle iso")
TriIso(10)
#Square Star Pattern
def SqrInStar(n):
    for i in range(n):
        for j in range(n):
            print('*',end='  ')
        print(end='\n')
print("\nSquare Star Pattern")
SqrInStar(10)
#Square Number Pattern
def SqrInNumb(n):
    k=1
    for i in range(n):
        for j in range(n):
            print(k,end=' ')
            k+=1
        print(end='\n')
print("\nSquare Number Pattern")
SqrInNumb(10)

#DIAMOND FINAL

def Diamond(n):
        q = n
        for i in range(n):
            for j in range(i):
                print('*',end=' ')
            q -= 1
            print(end='\n')
            print(' '*q,end='')
        q = 0
        for i in range(n-1,0,-1):
            for j in range(i):
                print('*', end=' ')
            q += 1
            print(end='\n')
            print(' ' * q, end='')

print( "----> D I A M O N D - P A T T R E N <----")
Diamond(10)
