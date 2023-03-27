#01.
def sum(a, b):
    return a + b

#02
def sub(a, b):
    return a - b

#03.
def mul(a, b):
    return a * b

#04.
def div(a, b):
    return a / b

#05.
def distance(x1, y1, x2, y2):
    a = (x1-x2)**2
    b = (y1-y2)**2
    d = (a + b)**(1/2)
    return d

#06.
def title():
    lylics = "Switch sides and I'm beside you."
    return lylics[-11:-1]
print (title())

#07.
def reverseStr(string):
    return string[::-1]
string = "경희대학교"
print (reverseStr(string))

#08.
def introduce():
    a = input("이름을 입력하세요 : ")
    b = input("취미를 입력하세요 : ")
    c = input("재학 중인 학교를 입력하세요 : ")
    d = input("생일을 입력하세요 : ")
    return "제 이름은 {0}입니다. 취미는 {1}입니다. 저는 {2}를 다니고 있습니다. 제 생일은 {3}입니다." .format(a,b,c,d) 
print (introduce())

#09.
def calc():
    a = input("첫 번째 수를 입력하세요 : ")
    b = input("두 번째 수를 입력하세요 : ")
    a = int(a)
    b = int(b)
    sum = a + b
    sub = a - b
    mul = a * b
    div = a // b
    print("두 수의 합 : %d" %sum)
    print("두 수의 차 : %d" %sub)
    print("두 수의 곱 : %d" %mul)
    print("두 수의 몫 : %d" %div)
print(calc())