1.Написать функцию для вычисления n-ого элемента последовательности Фибоначчи (используя рекурсию).
Пример: 6 -> 8
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2) 

print(fibo(10))

2. Из двух списков удалить все элементы, которые есть в обоих списках.
Пример: [1,2,3,4,5,6], [4,5,6,7,8,9] -> [1,2,3], [7,8,9]

a = [1, 2, 3, 4, 5, 6]
b = [4, 2, 5, 6, 7, 8, 9]

def remov(k, m):
    for i in range (len(k)+1):
        if i in m:
            k.remove(i) 
            m.remove(i)
    return k, m

print(remov(a, b))


3.Извлечь из списка все элементы, которые встречаются не реже заданного числа раз.
Пример: [1,2,3,3,3,3,3], 4 -> 3

a = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8]
k = 2  
res = [] 

for i in set(a):  
    if a.count(i) >= k:
        res.append(i)

print('Эти элементы встречаются минимум 2 раза:')
print(*res, sep=', ')


4.Заменить в списке все вложенные списки суммой их элементов
Пример: [1, [2, [3,4]] -> [1, [2, 7]] -> [1, 9]
l = [1, [2, [3, 4]]]


def summa(x):
    a = []
    for i in x:
        if isinstance(i, list):
            try:
                b = sum(i)
                a.append(b)
            except TypeError:
                listik = [flatten(i)] 
                a.extend(summa(listik)) 
        else:
            a.append(i)
    return a


def flatten(x): # код взятый из прошлой лабы
    a = []
    for i in x:
        if isinstance(i, list):
            a.extend(flatten(i))
        else:
            a.append(i)
    return a

print (flatten(l))



print(summa(l))

5.Найти наибольшую возрастающую подпоследовательность в списке.
Пример: [1,2,3,2,4,5,6,7] -> [4,5,6,7]

l = [1, 2, 3, 6, 8, 9, 2, 1, 2, 4, 5, 6, 7]


def posl(x):
    current = [] 
    maximum = [] 
    for i in range(len(x)):
        if i == 0 or x[i] <= x[i - 1]: 
            current = [x[i]] 
        else:
            current.append(x[i]) 
        if len(current) > len(maximum): 
            maximum = current
    return maximum

print(posl(l))


6.Привести заданную строку к стилю “заборчиком”.
Пример: “чмаф всех в чатике” -> “ЧмАф ВсЕх В чАтИке”

def zabor(x):
    x = '' #сюда будет записываться результат
    for i in range (len(s)):
        if i % 2 == 0: 
            x += s[i].upper() 
        else:
            x += s[i].lower() 
    return x


s = 'я умер в 16 лет и теперь я всегда выгляжу как в 16 лет'
print(zabor(s))



7.На вход подается ширина и высота. По этим параметрам нарисовать ромб, используя на выбор один из символов: #, *, +
Пример:
   #
 #  #
#    #
 #  #
   #

width = 13
height = 7
symbol = '*'

def diamond(width, height, symbol):
    if height % 2 == 0:
        height -= 1  
    mid = height // 2 + 1 
    for i in range(1, height + 1):
        row = ''
        if i <= mid:  
            spaces = mid - i
            diamonds = i * 2 - 1
            row += ' ' * spaces + symbol * diamonds + ' ' * spaces
        else:  
            spaces = i - mid
            diamonds = (height - i + 1) * 2 - 1
            row += ' ' * spaces + symbol * diamonds + ' ' * spaces
        print(row.center(width, ' '))  

diamond(width, height, symbol)


8.Заполнить квадратную матрицу так, чтобы все числа первого столбца и первой строки были равны 1,
а каждое из оставшихся чисел равно сумме верхнего и левого соседей. Вывести на экран матрицу данного размера.
Пример:
1   1   1   1
1   2   3   4
1   3   6   10
1   4   10 20

def create_mat(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):  
        matrix[0][i] = 1 
        matrix[i][0] = 1
    for i in range(1, n): 
        for j in range(1, n):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] 
    return matrix


def pechat_mat(n):
    matrix = create_mat(n)
    for i in range(n): 
        for j in range(n):
            print(matrix[i][j], end=' ') 
        print()  


pechat_mat(4)

9.Найти сумму всех чисел в строке.
Пример: “В этой 1 строке 4 всего 5 четыре числа 9” -> 19


def sum_of_numbers(x):

    result = '' 
    for i in x:
        if i.isdigit() or i.isspace(): 
            result += i
        else:
            continue

    result = result.strip() 
    numbers_list = [int(num) for num in result.split() if num.isdigit()] # преобразуем строку чисел в список чисел
    numbers_sum = sum(numbers_list)

    return numbers_sum


x = "19коров и кита3 выш33ло в поле 1"
result = sum_of_numbers(x)
print(result)


10.То же самое, но без явной конвертации (не используя int())

def sum_of_numbers(x):
    result = ''
    for i in x:
        if i.isdigit() or i.isspace():
            result += i
        else:
            continue

    result = result.strip() 
    list = []
    number = 0
    for c in result:
        if c.isdigit():
            number = number * 10 + ord(c) - ord('0') 
        elif c.isspace(): 
            if number != 0:
                list.append(number)
                number = 0
        else:
            continue
    if number != 0: 
        list.append(number) 
    return sum(list)

x = "19коров и кита3 выш33ло в поле 1"
result = sum_of_numbers(x)
print(result)
