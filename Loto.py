while True:
          import random
          try:
             a = str(input("Выберите от 1 до 7 - сильную цифру\n"))
          except ValueError:
              print(a)
          try:
             b = str(input("Выберите 6 цифр от 1 до 37, если нажмете ENTER система предложет вам автоматом\n"))
          except ValueError:
              print(b)
          for i in range (6):
           print((random.randint(1,37)),':', end = '')
          print ()
          for i in range (6):
           print((random.randint(1,37)),':', end = '')
          print()
          for i in range(6):
           print((random.randint(1,37)),':', end = '')
          print()
          for i in range(6):
           print((random.randint(1,37)),':', end = '')
          print()