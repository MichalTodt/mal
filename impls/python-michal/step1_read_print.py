from reader import read_str
from printer import pr_str

def READ(prompt):
    return read_str(prompt)

def EVAL(prompt):
    return prompt

def PRINT(prompt):
    return pr_str(prompt)

def rep(user_input):
    return PRINT(EVAL(READ(user_input)))

if __name__ == "__main__":
    while True:
        user_input = input("user> ")
        print(rep(user_input))

