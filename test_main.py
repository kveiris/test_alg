import random
import main
import numpy
import timeit
import os.path


def test_min_num():
    numtype = ["int", "float"]
    for test_num in range(0, 69):
        ex_num_test = []
        nums_count = 100
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        assert min(ex_num_test) == main.min_num()


def test_max_num():
    numtype = ["int", "float"]
    for test_num in range(0, 69):
        ex_num_test = []
        nums_count = 100
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        assert max(ex_num_test) == main.max_num()


def test_summ_num():
    numtype = ["int", "float"]
    for test_num in range(0, 69):
        ex_num_test = []
        nums_count = 100
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        assert sum(ex_num_test) == main.summ_num()


def test_mult_num():
    numtype = ["int", "float"]
    for test_num in range(0, 69):
        ex_num_test = []
        nums_count = 100
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        assert numpy.prod(ex_num_test) == main.mult_num()


def test_speed_min_num():
    numtype = ["int", "float"]
    ex_num_test = []
    for test_num in range(0, 69):
        nums_count = 500
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        print("Время работы: ", timeit.timeit(stmt="main.min_num()", number=1, globals=globals()), "размер файла: ",
              os.path.getsize("numbers.txt"))


def test_speed_max_num():
    numtype = ["int", "float"]
    ex_num_test = []
    for test_num in range(0, 69):
        nums_count = 500
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        print("Время работы: ", timeit.timeit(stmt="main.max_num()", number=1, globals=globals()), "размер файла: ",
              os.path.getsize("numbers.txt"))


def test_speed_summ_num():
    numtype = ["int", "float"]
    ex_num_test = []
    for test_num in range(0, 69):
        nums_count = 500
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        print("Время работы: ", timeit.timeit(stmt="main.summ_num()", number=1, globals=globals()), "размер файла: ",
              os.path.getsize("numbers.txt"))


def test_speed_mult_num():
    numtype = ["int", "float"]
    ex_num_test = []
    for test_num in range(0, 69):
        nums_count = 500
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, nums_count):
            if numtype[random.randint(0, 1)] == "int":
                ex_num_test.append(random.randint(bot_border_int, top_border_int))
            else:
                ex_num_test.append(random.uniform(bot_border_float, top_border_float))
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_num_test)):
            line = line + (str(ex_num_test[i]) + ' ')
        line = line[0:len(line) - 1]
        f.write(line)
        f.close()
        print("Время работы: ", timeit.timeit(stmt="main.mult_num()", number=1, globals=globals()), "размер файла: ",
              os.path.getsize("numbers.txt"))


def test_validation_fileread():
    for test_num in range(0, 500):
        types = ["int", "float", "space", "tab", "enter"]
        ex_val_test = []
        numbers = []
        symbol_count = 500
        bot_border_int = -228322
        top_border_int = 228322
        bot_border_float = -228322.0
        top_border_float = 228322.0
        for i in range(0, symbol_count):
            if types[random.randint(0, 4)] == "int":
                number = str(random.randint(bot_border_int, top_border_int))
                ex_val_test.append(number)
                numbers.append(number)
                ex_val_test.append(' ')
            elif types[random.randint(0, 4)] == "float":
                number = str(random.uniform(bot_border_float, top_border_float))
                ex_val_test.append(number)
                numbers.append(number)
                ex_val_test.append(' ')
            elif types[random.randint(0, 4)] == "space":
                ex_val_test.append(' ')
            elif types[random.randint(0, 4)] == "enter":
                ex_val_test.append('\n')
            elif types[random.randint(0, 4)] == "tab":
                ex_val_test.append('\t')
        f = open('numbers.txt', 'w')
        line = ''
        for i in range(0, len(ex_val_test)):
            line = line + ex_val_test[i]
        f.write(line)
        f.close()
        assert numbers == main.fileread("numbers.txt")
