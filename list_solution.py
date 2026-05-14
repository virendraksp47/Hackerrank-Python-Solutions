if __name__ == '__main__':
    import re 
    list1=[]
    N = int(input())
    for i in range(0,N):
        command=input()
        numbers_from_command=re.findall(r'\d+',command)
        index1=0
        int1=0
        if len(numbers_from_command)==2:
            index1=int(numbers_from_command[0])
            int1=int(numbers_from_command[1])

        if len(numbers_from_command)==1:
            int1=int(numbers_from_command[0])

        insert_command=f"insert {index1} {int1}"
        remove_command=f"remove {int1}"
        append_command=f"append {int1}"
        print_command="print"
        sort_command="sort"
        pop_command="pop"
        reverse_command="reverse"
        if command==insert_command:
            list1.insert(index1,int1)
        elif command==remove_command:
            list1.remove(int1)
        elif command==append_command:
            list1.append(int1)
        elif command==print_command:
            print(list1)
        elif command==sort_command:
            list1.sort()
        elif command==pop_command:
            list1.pop()
        elif command==reverse_command:
            list1.reverse()
