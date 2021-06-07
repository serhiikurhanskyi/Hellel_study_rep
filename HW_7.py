list_number = [1, 2, 3, 4, 5, 6, 7, 8]
numbers_sum_list = 0
for number in list_number:
    numbers_sum_list = numbers_sum_list + number
print(numbers_sum_list)

str_list = ['cat', 'cash', 'civic']
x = sum(string.count('a') for string in str_list)
print(x)

list_1 = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7]
x = int(input('Введите число: '))
for i in list_1:
    if i == x:
        print('ok!')
        break
else:
    print("No")
