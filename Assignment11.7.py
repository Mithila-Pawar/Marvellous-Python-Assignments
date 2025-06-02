def triangle(x):
    if not x: return ''
    return f'{triangle(x-1)}{"*"*x}\n'
    
print(triangle(4))