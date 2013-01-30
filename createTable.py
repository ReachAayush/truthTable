#@author = "Aayush Agarwal"
#Truth Table Creator
#Only edit the "check" function
#asks for num inputs when program is run

def createRow(n,v):
    res = [0,0,0,0,0,0]
    s = bin(n)[2:]
    a = list(s)
    m = len(a)
    if(m < v):
        new = res[:v - m] + a
        final = []
        for e in new:
            final.append(int(e))
        return final
    else:
        final = []
        for e in a:
            final.append(int(e))
        return final

def createTable(numVariables):
    res = []
    for i in xrange(2**numVariables):
        res.append(createRow(i, numVariables))
    return res

def printTable(table):
    for row in xrange(len(table)):
        print "[ ",
        for col in xrange(len(table[0])):
            a = str(table[row][col])
            if(col == len(table[0]) - 1):
                print (" ==> "+a),
            else:
                print (a + "   "),
        print "]"

"""
THIS SHOULD BE THE ONLY FUNCTION YOU TOUCH.
The input is the row, which is a list of ints.
"""
def check(r):
    p0 = r[0]
    p1 = r[1]
    d0 = r[2]
    p2 = r[3]
    d1 = r[4]
    d2 = r[5]
    sum1 = p0 + d0 + d1
    sum2 = p1 + d0 + d2
    sum3 = p2 + d1 + d2
    check1 = sum1 % 2
    check2 = sum2 % 2
    check3 = sum3 % 2
    check = check1 + check2 + check3
    if(check == 0):
        return 0
    return 1

def createTruthTable(a):
    res = []
    for row in a:
        row.append(check(row))
        res.append(row)
    return res

def main():
    x = raw_input("how many inputs does your function have? ")
    a = createTable(int(x))
    b = createTruthTable(a)
    printTable(b)
    
main()
