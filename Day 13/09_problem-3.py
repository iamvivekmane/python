# filter numbers divisible by 5
a = [1,2,4,5,6234,990,100,210]

b = lambda x:x%5==0

c = filter(b,a)

print(list(c))