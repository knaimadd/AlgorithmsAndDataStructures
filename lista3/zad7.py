from Stack import Stack
import os

def tags(str):
    """Function that filters valid tags from string"""
    beg = False
    tg = []
    j = 0
    for i in str:
        if i == '<' and not beg:
            p = j
            beg = True
            if str[j+1] == ' ' or str[j+1] == '!':
                beg = False
        if i == '>' and beg:
            tg.append(str[p:j+1])
            beg = False
        j += 1
    return tg

def validator(file):
    """Function that validate if file has good used tags"""
    with open(file) as f:
        str = f.read()
    li = tags(str)
    st = Stack()
    j = 0
    cond = False
    exceptions = ['area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr']
    for i in li:
        for ex in exceptions:
            if i[1:len(ex)+1] == ex:
                cond = True
                break
        if cond:
            cond = False
            continue
        if len(st) > 0 and i[1] == '/':
            if st.peek()[1:len(i[2:-1])+1] == i[2:-1]:
                st.pop()
            else:
                return False
        else:
            st.push(i)
        j += 1
    if len(st) == 0:
        return True
    else:
        return False


if __name__ == '__main__':

    print(validator(os.path.join(os.getcwd(), 'index.html')))