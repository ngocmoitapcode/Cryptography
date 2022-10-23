def format_data(p):
    data = []
    for i in range (0, p):
        v = i * i
        mod = v % p
        if (mod not in data):
            data.append(mod)
    return data

class Response:
    def __init__(Myobject, i, is_include, x1, x2):
        Myobject.i = i
        Myobject.is_include = is_include
        Myobject.x1 = x1
        Myobject.x2 = x2
 
    def print(inst):
        print("i: " + inst.i)
        print("is_include: " + inst.is_include) 
        print("x1: " + inst.x1) 
        print("x2: " + inst.x2)

def main(a, b, p):
    data = format_data(p)
    count = 1
    res = []
    for i in range(1, len(data)):
        y = pow(i, 3) + a * i + b
        mod = y % p
        x1 = 0
        x2 = 0

        if (mod in data):
            count += 2
            j = 1
            while (j < p):
                t = j*j
                tmod = t % p
                if (tmod == mod):
                    x1 = j
                    x2 = p - j
                    break
                j += 1

        res.append(Response(i, mod in data, x1, x2))

    print(count)
        
#main(5, 4, 937)
main(5, 4, 9433)
#main(5, 4, 1496641)