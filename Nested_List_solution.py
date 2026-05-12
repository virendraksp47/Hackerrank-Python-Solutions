if __name__ == '__main__':
    records=[]
    score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score,name])
        score_list.append(score)
        
records.sort()
score_list.sort()
f=list(set(score_list))
score_list=f

for i in records:
    if i[0]==score_list[1]:
        print(i[1])