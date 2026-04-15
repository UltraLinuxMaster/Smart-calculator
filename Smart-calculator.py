import operator
signsfor_n = {
    "/":" / ",
    "//":" // ",
    "^":" ^ ",
    "-":" - ",
    "+":" + ",
    "**":" ** ",
    "*":" * ",
    "%":" % "
}
signs =  { 
    "/":operator.truediv,
    "//":operator.floordiv,
    "^":operator.pow,
    "-":operator.sub,
    "+":operator.add,
    "**":operator.pow,
    "*":operator.mul,
    "%":operator.mod
    }
while True:
    su = 0
    counter = 0
    n = input()
    l = len(n)
    s = ""
    while counter != l:
        s += n[counter] 
        if n[counter] == '*' or n[counter] == '**' or n[counter] == '%' or n[counter] == '^' or n[counter] == '-' or n[counter] == '+' or n[counter] == '//' or n[counter] == '/':
            s = s.replace(n[counter], signsfor_n[n[counter]])
        counter += 1
    counter = 0
    p = s.split()
    le = len(p)
    if le % 2 == 0:
        print("ERROR1")
        break
    if le == 3:
        sign = 1
    elif le > 3:
        sign = 1 + ((le - 3) // 2)
    else:
        print("ERROR2")
        break
    for i in range(le - sign):
        if p[counter].isdigit() == False:
            print("ERROR3")
            break
        counter += 2
    counter = 1
    for j in range(sign):
        if p[counter] == '*' or p[counter] == '/' or p[counter] == '//' or p[counter] == '^' or p[counter] == '**' or p[counter] == '-' or p[counter] == '+' or p[counter] == '%':
            continue
        else:
            print("ERROR4")
            break
        counter += 2
    counter = 0
    counterofsign = 3
    counterofnumber = 4
    for k in range(sign):
        if counter == 0:
            su = signs[p[1]](int(p[0]), int(p[2]))
        else:
            su = signs[p[counterofsign]](su, int(p[counterofnumber]))
            counterofnumber += 2
            counterofsign += 2
        counter += 1       
    print(su)