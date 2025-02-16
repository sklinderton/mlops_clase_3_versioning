def suma (a, b):
    return a + b

def login(username: str, password: str):
    if username == 'admin':
        return "login successful"
    else:
        return "login unsuccessful"

def resta(a:int, b:int) -> int:
    return a - b

if __name__ == '__main__':
    print(suma(2, 3))
    print(login('admin', 'admin'))