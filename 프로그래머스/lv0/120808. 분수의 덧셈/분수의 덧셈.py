from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    result = []
    a = Fraction(numer1, denom1)
    b = Fraction(numer2, denom2)
    c = a+b
    result.append(c.numerator)
    result.append(c.denominator)
    return result