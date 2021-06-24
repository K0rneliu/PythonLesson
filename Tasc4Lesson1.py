# задача 4
# найти самую большую цифру в числе

numb = int(input("Enter number: "));
if numb < 0:
    numb = numb * (-1);
max = 0;
k = numb;
while k>0:
    rest = k % 10;
    if max == 9:
        break
    if rest > max:
        max = rest;
    k=k//10;
print(f'max {max}')
