def fileread(file):
    f = open(file, 'r')
    line = ''
    for i in f:
        line = line + i + ' '
    line.strip()
    line = line.replace('\n', ' ')
    line = line.replace('\t', ' ')
    line = line.split(' ')
    try:
        while True:
            line.remove('')
    except Exception:
        pass
    for i in line:
        try:
            number = float(i)
        except Exception:
            return "NO"
    return line


def min_num():
    try:
        listnum = fileread('numbers.txt')
        if listnum != "NO":
            for i in range(0, len(listnum)):
                if "." in listnum[i]:
                    listnum[i] = float(listnum[i])
                else:
                    listnum[i] = int(listnum[i])
            minimal = listnum[0]
            for i in range(0, len(listnum)):
                if minimal > listnum[i]:
                    minimal = listnum[i]
            return minimal
        else:
            return "NO"
    except OverflowError:
        return "OverflowError"


def max_num():
    try:
        listnum = fileread('numbers.txt')
        if listnum != "NO":
            for i in range(0, len(listnum)):
                if "." in listnum[i]:
                    listnum[i] = float(listnum[i])
                else:
                    listnum[i] = int(listnum[i])
            maximal = listnum[0]
            for i in range(0, len(listnum)):
                if maximal < listnum[i]:
                    maximal = listnum[i]
            return maximal
        else:
            return "NO"
    except OverflowError:
        return "OverflowError"


def summ_num():
    try:
        listnum = fileread('numbers.txt')
        if listnum != "NO":
            for i in range(0, len(listnum)):
                if "." in listnum[i]:
                    listnum[i] = float(listnum[i])
                else:
                    listnum[i] = int(listnum[i])
            summ = 0
            for i in range(0, len(listnum)):
                summ = summ + listnum[i]
            return summ
        else:
            return "NO"
    except OverflowError:
        return "OverflowError"


def mult_num():
    try:
        listnum = fileread('numbers.txt')
        if listnum != "NO":
            for i in range(0, len(listnum)):
                if "." in listnum[i]:
                    listnum[i] = float(listnum[i])
                else:
                    listnum[i] = int(listnum[i])
            multik = 1
            for i in range(0, len(listnum)):
                multik = multik * listnum[i]
            return multik
        else:
            return "NO"
    except OverflowError:
        return "OverflowError"
