import numpy as np

while True:
    f_a = float(input('var f_a'))
    
    f_b = float(input('var f_b'))
    
    f_c = float(input('var f_c'))
    
    i_d = int(input('var i_d'))
    
    act = input('act')
    
    if act == '+':
        print(f_a + f_b)
    elif act == '-':
        print(f_a - f_b)
    elif act == '*':
        print(f_a * f_b)
    elif act == '/':
        print(f_a / f_b)
    elif act == '**':
        print(f_a ** f_b)
    elif act == '%':
        print(f_a % f_b)
    elif act == '//':
        print(f_a // f_b)
    elif act == 'abs':
        print(abs(f_c))
    elif act == 'sqrt':
        print(np.sqrt(f_c))
    elif act == 'log':
        print(np.log(f_c))
    elif act == 'sin':
        print(np.sin(f_c))
    elif act == 'cos':
        print(np.cos(f_c))
    elif act == 'tan':
        print(np.tan(f_c))
    elif act == '!':
        print(np.factorial(i_d))
    elif act == 'rd':
        print(round(f_c, i_d))
    elif act == 'cbrt':
        print(np.cbrt(f_c))
    else:
        print(f'error: act {act} not found')
    if KeyboardInterrupt():
        break
