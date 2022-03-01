def fibonacci():
  n = int(input("Até qual mês deseja calcular a reprodução dos coelhos?"))  
  f1 = 1
  f2 = 1
  fn = 0
  count = 3
  while count <= n:
    fn = f1 + f2
    f1,f2 = f2,fn
    print("No mês %d você possui %d casais de coelhos"%(count, fn))
    count+=1
fibonacci()