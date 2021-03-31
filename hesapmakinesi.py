print("Hesap makinemiz sayı->işlem->sayı->işlem->...->'=' şeklinde çalışmaktadır.'=' girişi işlemi sonlandırır.")
a = float(input("'+' toplama\n'-' çıkarma\n'*' çarpma\n'/'  bölme\n'**' üs alma\n'***' karekök alma\nGiriş yapınız.\n"))
d = 'q'
while d != '=':
    d = input()
    if d == '+':
        b = input()
        b = float(b)
        a = a + b
        print("Total: ",a)
    elif d == '-':
        b = input()
        b = float(b)
        a = a - b
        print("Total: ",a)
    elif d == '*':
        b = input()
        b = float(b)
        a = a * b
        print("Total: ",a)
    elif d == '/':
        b = input()
        b = float(b)
        a = a / b
        print("Total: ",a)
    elif d == '**':
        b = input()
        b = float(b)
        a = a ** b
        print("Total: ",a)
    elif d == '***':
        a = a ** (1/2)
        print("Total: ",a)
    else:
        print ("Geçerli bir işlem türü giriniz.")
print("Hesap makinesi kapanıyor...\nTotal = ",a)
    