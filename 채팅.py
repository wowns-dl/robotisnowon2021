server_open = True
name = []
order = 0
i = 0
last = 0
while server_open:
    last = 0
    order = input()
    if order == 'list':
        if len(name) == 0:
            print('nobody')
            break
        i = len(name)
        for last in range(0,i):
            last += 1
        print(name[last-1])
    elif order == 'change name':
        pass
    elif order == 'enter':
        enter = input()
        name.append(enter)
        print(enter+'님이 들어왔습니다')
    elif order == 'exit':
        exit = input()
        name.remove(exit)
        print(exit+'님이 나갔습니다')
        
