def READ(prompt):
    return prompt

def EVAL(prompt):
    return prompt

def PRINT(prompt):
    return prompt

def rep(user_input):
    return PRINT(EVAL(READ(user_input)))

if __name__ == "__main__":
    while True:
        user_input = input("user> ")
        print(rep(user_input))

