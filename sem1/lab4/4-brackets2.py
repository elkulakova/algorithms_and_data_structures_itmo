from stack_class import *
from measurments import *
from random_string import *

@measure_performance
def check_brackets(text):
    open_brackets = ['[', '{', '(']
    close_brackets = [']', '}', ')']
    brackets = open_brackets + close_brackets
    size = len(text)
    stack = Stack(size) # макс размер ставим, так как все скобки открывающие могут быть
    for i in range(size):
        el = text[i]
        if el in brackets:
            if el in close_brackets:
                if stack.is_empty():
                    return i+1
                else:
                    if open_brackets.index(stack[stack.top][0]) != close_brackets.index(el):
                        return i+1
                    else:
                        stack.pop() # удаляем, так как нашлась пара
                        continue
            stack.push((el, i+1))
        continue
    if stack.is_empty():
        return 'Success'
    else:
        return stack[stack.top][1]

if __name__ == "__main__":
    #generate_string()
    with open('input.txt') as f:
        line = f.readline()

    result = check_brackets(line)
    with open('output.txt', 'w') as f:
        f.write(str(result))
    print(result)