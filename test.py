alist = ["Apple=0.04\n", "Banana=0.15\n", "Grape=0.1\n"]
a = {}
for i in alist:
    i = i.strip()
    fruit, price = i.split("=")
    a[fruit.strip()] = float(price.strip())
print(a)