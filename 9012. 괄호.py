class Stack(list):
    push = list.append    # Insert
    pop = list.pop        # Delete

    def is_empty(self):   # 데이터가 없는지 확인
        if not self:
            return True
        else:
            return False


if __name__ == "__main__":
    num = int(input())
    for _ in range(num):
        check = True
        s = Stack()
        string = input()
        for i in range(len(string)):
            if string[i] == '(':
                s.push(string[i])
            else:
                if not s.is_empty():
                    if s.pop() == '(':
                        continue
                    else:
                        check = False
                        break
                else:
                    check = False
                    break

        if check and s.is_empty():
            print("YES")
        else:
            print("NO")
