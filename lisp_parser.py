# Lisp tokenizer and parser


def tokenize(content: str):
    token = ''
    skip_line = False
    for ch in content:
        if skip_line and ch in "\r\n":
            skip_line = False
            continue
        if ch in " \t\r\n":
            if len(token) > 0:
                yield token
                token = ''
            continue
        elif skip_line:
            continue
        elif ch in "#":
            skip_line = True
            continue
        elif ch in "()[]{}":
            if len(token) > 0:
                yield token
                token = ''
            yield ch
            continue
        else:
            token += ch
    if len(token) > 0:
        yield token
    yield None


def parse(content: str):
    sexp = []
    stack = []
    tokenizer = tokenize(content)
    while True:
        token = next(tokenizer)
        if token is None:
            break
        elif token in "([{":
            stack.append(sexp)
            sexp = []
        elif token in ")]}":
            temp = sexp
            sexp = stack.pop()
            sexp.append(temp)
        else:
            sexp.append(token)
    return sexp
