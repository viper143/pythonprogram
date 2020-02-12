def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

index = 0
while 1:
    number = fibo(index)
    if number > 50:
        break
    print(number)
    index += 1
