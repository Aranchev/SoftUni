a = input()
b = ''
c = 0

while a != b:
    b = input()
    if b == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {c} books.')
        break
    if a == b:
        print(f'You checked {c} books and found it.')
    c += 1
