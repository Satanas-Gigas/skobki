# -*- coding: windows-1251 -*-
open_br = '([{'
close_br = ')]}'
check_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
}
test_str_inp = input("VVedite skobki")
test_str = [test_str_inp]

class Stack:

    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self, new_el):
        self.stack.append(new_el)
        return

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_balanced(brackets_sequence):
    temp_list = Stack([])
    for bracket in brackets_sequence:
        if bracket in open_br:
            temp_list.push(bracket)
        elif bracket in close_br:
            if temp_list.is_empty():
                return '����������������'
            else:
                if temp_list.peek() == check_dict[bracket]:
                    temp_list.pop()
                else:
                    return '����������������'
    if temp_list.is_empty():
        return 'C�������������'
    else:
        return '����������������'


if __name__ == '__main__':
    for my_str in test_str:
        print(is_balanced(my_str))