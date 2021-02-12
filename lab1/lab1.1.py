a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
k = int(input("k: "))
d = int(input("d: "))
f = int(input("f: "))


if a==0 or b==0 or (a + b + c * (k - a / b**3))==0:
    var1 = "zero division"
else:
    var1 = abs(((a**2 / b**2) + (c**2 * a**2)) / (a + b + c * (k - a / b**3)) + c + (k/b - k/a)*c)


if a==0 or b==0:
    var2 = "zero division"
else:
    var2 = abs(((a**2 - b**3 - c**3 * a**2) * (b - c + c * (k - d / b**3)) - (k / b - k / a) * c)**3 - 20000)

if (c-a)==0:
    var3 = "zero division"
else:
    var3 = abs(1 - a * b**c - a * (b**2 - c**2) + (b - c + a) * (12 + b) / (c - a))

if a==0:
    var4 = "zero division"
else:
    var4 = abs(a - b * c * d**3 + (c**5 - a**2)/a + f**3 * (a - 213))


print(var1,var2,var3,var4,sep='\n')