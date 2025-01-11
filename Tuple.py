def check_tuple(tuple_1:tuple, tuple_2:tuple):
    print(all(item in tuple_1 for item in tuple_2))


check_tuple(tuple(input('Первый кортеж: ')), tuple(input('Второй кортеж: ')))