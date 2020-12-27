list=[]
while True:
    num=int(input('Type a number:'))
    list.append(num)
    cont=str(input('Do you want to continue [Y/N]'))
    if cont in 'Nn':
        break
if 5 in list:
    print('Number 5 is in the list')
else:
    print('Number 5 was not found')
list.sort(reverse=True)
print(f'Your list has  {len(list)} numbers')
print(f'The numbers in backward display are  {list}')
