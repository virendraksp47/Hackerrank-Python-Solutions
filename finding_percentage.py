if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

index=0
addition=0


for i in student_marks:
    if i==query_name:
        for x in student_marks[i]:
            index+=1
            addition=addition+x
            #print(addition)

average=addition/index
#average=round(average,2)
print(f"{average:.2f}")