import re
from mal_types import MalList

class Reader():
    def __init__(self, tokens) -> None:
        self._position = 0
        self._tokens = tokens
    
    def next(self):
        current_token = self._toekens[self._position]
        self._position += 1
        return current_token

    def peek(self):
        return self._tokens[self._position]


def tokenize(user_input):
    pattern = r'[\s,]*(~@|[\[\]{}()\'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}(\'"`,;)]*)'
    return re.findall(pattern, user_input)

def read_str(user_input):
    return read_form(Reader(tokenize(user_input)))

def read_form(form):
    first = form.peek()
    if first[0] == "(":
        read_list(form)
    else:
        read_atom(form)
    return # MalList of MalTypes

def read_list(form):
    accumulator = MalList()
    while True:
        token = read_form(form)
        if token != ")":
            break
        accumulator.append(token)
    return accumulator
    

def read_atom(atom):
    # return mal type
    return

if __name__ == "__main__":
    print(read_str("    (+ 1 3) "))