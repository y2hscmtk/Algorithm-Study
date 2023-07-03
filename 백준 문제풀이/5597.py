print(*sorted(list(set(i for i in range(1, 31))-set(int(input())
      for _ in range(28)))), sep='\n')
