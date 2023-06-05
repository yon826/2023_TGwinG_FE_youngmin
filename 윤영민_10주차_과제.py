class Subject:
    def __init__(self):
        self.score = None
        self.subject_name = None
        self.max_score = None

    def get_subject_name(self):
        return self.subject_name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_max_score(self):
        return self.max_score

class Korean(Subject):
    def __init__(self):
        self.subject_name = "국어"
        self.max_score = 100

class Math(Subject):
    def __init__(self):
        self.subject_name = "수학"
        self.max_score = 100

class History(Subject):
    def __init__(self):
        self.subject_name = "역사"
        self.max_score = 50

class Student:
    def __init__(self, name):
        self.name = name
        self.kor = Korean()
        self.math = Math()
        self.his = History()
        self.subjects = [self.kor, self.math, self.his]

    def get_name(self):
        return self.name
    
    def make_sum(self):
        return self.kor.get_score() + self.math.get_score() + self.his.get_score()
    
    def print(self):
        print(f"===== Student {self.get_name()} =====")
        print(f"{self.kor.get_subject_name()} : {self.kor.get_score()} / {self.kor.get_max_score()}")
        print(f"{self.math.get_subject_name()} : {self.math.get_score()} / {self.math.get_max_score()}")
        print(f"{self.his.get_subject_name()} : {self.his.get_score()} / {self.his.get_max_score()}")

def print_rank(students):
    b = []
    a = students[0]
    for i in students:
        b.append(i)

    for i in range(len(students)):
        for j in range(i):
            if (b[j].make_sum() < b[j+1].make_sum()):
                a = b[j]
                b[j] = b[j+1]
                b[j+1] = a

    for i in range(len(students)):
        print(f"Rank {i+1} : {b[i].get_name()} ( {b[i].make_sum()} / 250)")

# 실행 함수 (수정하지 마세요. 코드 테스트용 함수입니다.)
def Test():
    n = int(input("How many students: "))

    students = []

    for i in range(n):
        name = input("Name of Student: ")

        student = Student(name)

        for subject in student.subjects:
            score = int(input("Score of %s : " %subject.get_subject_name()))
            subject.set_score(score)

        print()
        student.print()
        print()
        students.append(student)

    print("===== Rank =====")
    print_rank(students)

Test()