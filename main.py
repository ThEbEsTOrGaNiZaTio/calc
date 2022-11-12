def_tokens = ['*', '/', '+', '-', '(', ')']


def parse(string):
    tokens = []
    currToken = ''
    counter = 0
    while counter < len(string):
        symbol = string[counter]
        if symbol == ' ':
            if currToken != '':
                tokens.append(currToken)
                currToken = ''
        else:
            if symbol in def_tokens:
                if currToken != '':
                    tokens.append(currToken)
                    currToken = ''
                tokens.append(symbol)
            else:
                currToken += symbol

        counter += 1

    if currToken != '':
        tokens.append(currToken)
    return tokens


tokens = []
pos = 0


def check(token):
    global tokens, pos
    if pos >= len(tokens):
        return False
    curr = tokens[pos]
    if curr != token:
        return False
    pos += 1
    return True


def add():
    global tokens, pos
    res = multiply()

    while True:
        if check('+'):
            res = res + multiply()
            continue
        if check('-'):
            res = res - multiply()
            continue
        break
    return res


def multiply():
    global tokens, pos
    res = unary()

    while True:
        if check('*'):
            res = res * unary()
            continue
        if check('/'):
            res = res / unary()
            continue
        break
    return res


def unary():
    global tokens, pos
    if check('-'):
        return -1 * primary()
    if check('+'):
        return primary()
    return primary()


def primary():
    global tokens, pos
    curr = tokens[pos]
    if check('('):
        ret = add()
        pos += 1
        return ret
    else:
        pos += 1
        return float(curr)




def calc(tokens_):
    global tokens, pos
    tokens = tokens_
    pos = 0
    return add()


print(calc(parse("-50 * 2 + 10 + 10 * (5 - 100) * 10 / 5 + 2.5")))



