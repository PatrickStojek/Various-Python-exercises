beginning, end = map(int, input('Podaj początek zakresu oraz koniec zakresu jako liczby rodzielone spacją: ').split())
divider = int(input('Podaj dzielnik: '))

count = (end // divider) - ((beginning - 1) // divider)
print(count)
""" write me a code which will print how  many numbers in a given range are divisible by the divider  """
""" write this code without using a loop """
""" for instance for range [5, 15] and a divider 5 the output should be 3 """