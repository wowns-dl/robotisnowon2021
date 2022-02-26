addrlist = [
    {"idx":0, "name":'김강현',"phone":'010-2245-8471',"addr":'노원구'},
    {"idx":1, "name":'이재준',"phone":'010-2145-8471',"addr":'노원구'},
    {"idx":2, "name":'채종민',"phone":'010-2245-8471',"addr":'노원구'},
    {"idx":3, "name":'우수연',"phone":'010-2345-8471',"addr":'노원구'},
    {"idx":4, "name":'김경',"phone":'010-2445-8471',"addr":'노원구'}
]

def menu():
    print("1.입력 2. 출력 3. 검색 4. 수정 5. 삭제 6. 종류")
    no = int(input("선택>>>"))
    return no

def outputdata():
    print("#### 출력 ####")
    for i in addrlist:
        print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(i["idx"],i["name"],i["phone"],i["addr"]))
        
def inputdata():
    pass

factory = [inputdata, outputdata, searchdata, modifydata, deletedata]

def run(no):
    print("{}번이 선택되었습니다!".format(no))
    if no == 6:
        print("#### 종류 ####")
        exit(0)
    if no in range(1, len(factory)+1):
        factory[no-1]()
    else :
        print("해당 사항 없음")
        
def main():
    while True:
        print("{:=^40}".format("주소록"))
        no = menu()
        run(no)
        
if __name__ == '__main__':
    main()
