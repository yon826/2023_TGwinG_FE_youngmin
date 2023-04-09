# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    n = len(lst)
    lst.sort()
    x = 0
    for i in range(n):
        for j in range(n):
            if lst[i]*2 == lst[j]:
                x = x + 1
    return x

# 2번
n=5
def pascal(n):
    arr = [n * [0] for _ in range(n)]
    for i in range(n):
        arr[i] = [1]*(i+1)
    for j in range(2,n):
        for k in range(1,j):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]
    return arr[n-1]

# 3번
def beerRefrigerator(n):
    x = 9999999999
    for i in range(1,n+1):
        if n%i == 0:
            for j in range(1,(n//i)+1):
                if n % (i*j) == 0:
                    for k in range ((n//(i*j))+1):
                        if i*j*k == n:
                            sum = i*j +j*k + k*i
                            if sum < x:
                                x = sum
                                a = i
                                b = j
                                c = k
    return "{0} X {1} X {2}" .format (a,b,c)

# 4번
def matrixMul(mat1, mat2):
    n = len(mat1)
    m = len(mat1[0])
    m = len(mat2)
    k = len(mat2[0])
    arr = [k * [0] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for l in range(m):
                arr[i][j] = arr[i][j] + mat1[i][l]*mat2[l][j]
    return arr