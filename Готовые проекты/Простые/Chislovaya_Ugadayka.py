import random
again = 'да'
while again.lower() == 'да':

    count=0
    N=int(input('Выберите до какого числа N будет подбор случайного числа (от 1 до N). N='))
    a=random.randint(1,N)
    print('Добро пожаловать в числовую угадайку')
    n=int(input(f'Введите предполагаемое целое число от 1 до {N}:'))

    def is_valid(num):
        if int(num) in range(1,N):
            return True
        else:
           return False

    while is_valid(n)==False:
       n=int(input(f'А может быть все-таки введем целое число от 1 до {N}?'))

    while n!=a:
      if n<a:
        n=int(input('Ваше число меньше загаданного, попробуйте еще разок'))
        count+=1
      elif n>a:
        n=int(input('Ваше число больше загаданного, попробуйте еще разок'))
        count+=1
    if n==a:
        print('Вы угадали, поздравляем!')
        print('Количество попыток, до победного варианта:', count+1)
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    again = input('Сыграем еще? (да = да, нет = нет): ')