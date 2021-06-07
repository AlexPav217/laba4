class Rational_num (object):
    def __init__(self, n, d):
        if not (type(n) == int and type(d) == int and d != 0):
            raise IOError('Неверный формат числа')
        elif d < 0:
            self.n = -1 * n
            self.d = -1 * d
        else:
            self.n = n
            self.d = d

    def __add__(self, other):  # сложение
            return Rational_num(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):  # вычитание
            return Rational_num(self.n * other.d - other.n * self.d, self.d * other.d)

    def __mul__(self, other):  # умножение
            return Rational_num(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):  # деление
            if other.n == 0:
                raise ZeroDivisionError
            return Rational_num(self.n * other.d, self.d * other.n)

    def __floordiv__(self, other):  # целочисленное деление
            if other.n == 0:
                raise ZeroDivisionError
            return (self.n * other.d) // (other.n * self.d)

    def __mod__(self, other):  # остаток от деления
            if other.n == 0:
                raise ZeroDivisionError
            return (self.n * other.d) % (other.n * self.d)

    def __eq__(self, other):  # равенство
            return self.n * other.d == other.n * self.d

    def __ne__(self, other):  # неравно
            return self.n * other.d != other.n * self.d

    def __lt__(self, other):  # меньше
            return self.n * other.d < other.n * self.d

    def __le__(self, other):  # меньше или равно
            return self.n * other.d <= other.n * self.d

    def __gt__(self, other):  # больше
            return self.n * other.d > other.n * self.d

    def __ge__(self, other):  # больше или равно
            return self.n * other.d >= other.n * self.d

    def __greatestCommonDivisor(self, a, b):  # наибольший общий делитель
            if a == 0:
                return b
            return self.__greatestCommonDivisor(b % a, a)

    def reduction(self):  # сокращение дроби
            greatestCommonDivisor = self.__greatestCommonDivisor(self.n, self.d)
            self.n = int(self.n / greatestCommonDivisor)
            self.d = int(self.d / greatestCommonDivisor)

    def decimalToPeriod(self):
        numer = abs(self.n)
        denom = abs(self.d)
        dec = str(numer // denom) + "."
        list = {}
        index = 0
        numer = numer % denom
        if numer == 0:
            return str(self.n / self.d)
        list[numer] = index
        flag = False
        while not flag:
            if numer == 0:
                break
            digit = numer * 10 // denom
            numer = numer * 10 - digit * denom
            if numer not in list:
                dec += str(digit)
                index += 1
                list[numer] = index
            else:
                dec += str(digit) + ")"
                dec = dec[:list.get(numer) + len(dec[:dec.index(".") + 1])] + "(" + dec[
                                                        list.get(numer) + len(dec[:dec.index(".") + 1]):]
                flag = True
        if self.n < 0:
            dec = "-" + dec
        return dec


def periodToDecimal(num):
    isPositive = True
    if num[0] == "-":
        isPositive = False
        num = num[1:]
    period = ""
    fraction = ""
    integer = ""
    isPeriod = False
    if "(" in num:
        array = num.split(".")
        integer = array[0]
        for e in array[1]:
            if isPeriod and e != ")":
                period += e
            if e != "(" and not isPeriod:
                fraction += e
            else:
                isPeriod = True
        denom = ""
        for i in range(0, len(period)):
            denom += "9"
        for i in range(0, len(fraction)):
            denom += "0"
        if len(fraction) == 0:
            fraction = 0
        else:
            fraction = int(fraction)
        denom = int(denom)
        integer = int(integer)
        period = int(period)
        numer = 0
        if fraction == 0:
            numer = period + integer * denom
        else:
            numer = fraction * period - fraction + integer * denom
    else:
        count = abs(num.find('.') - len(num)) - 1
        numer = int(float(num) * 10 ** count)
        denom = 10 ** count
    if isPositive:
        rational = Rational_num(numer, denom)
    else:
        rational = Rational_num(numer * (-1), denom)
    rational.reduction()
    return rational