from typing import List
from dataclasses import dataclass

@dataclass
class Operator:
    symbol: str
    precedence: int
    operands: int
    isltr: bool # left ot right

@dataclass
class Operators:
    operators: List[Operator]

    def __init__(self, operators: List[Operator]):
        self.operators = operators
    
    def __contains__(self, item):
        return item in [operator.symbol for operator in self.operators]
    
    def __getitem__(self, key):
        item = None
        for i in self.operators:
            if i.symbol == key:
                item = i
        return item

#precedence from https://en.cppreference.com/w/c/language/operator_precedence
operators = Operators([
    Operator(symbol='**', precedence=1, operands=1, isltr=False),

    Operator(symbol='!', precedence=2, operands=1, isltr=False),
    Operator(symbol='~', precedence=2, operands=1, isltr=False),
    Operator(symbol='*', precedence=3, operands=2, isltr=True),
    Operator(symbol='/', precedence=3, operands=2, isltr=True),
    Operator(symbol='%', precedence=3, operands=2, isltr=True),
    Operator(symbol='-', precedence=4, operands=2, isltr=True),
    Operator(symbol='+', precedence=4, operands=2, isltr=True),
    Operator(symbol='>>', precedence=5, operands=2, isltr=True),
    Operator(symbol='<<', precedence=5, operands=2, isltr=True),
    Operator(symbol='&', precedence=8, operands=2, isltr=True),
    Operator(symbol='^', precedence=9, operands=2, isltr=True),
    Operator(symbol='|', precedence=10, operands=2, isltr=True),
    Operator(symbol='&&', precedence=11, operands=2, isltr=True),
    Operator(symbol='||', precedence=12, operands=2, isltr=True),
])

def toReversePolishNotation(a):
    def helper(stack, i):
        return stack and (stack[-1] in operators and (operators[stack[-1]].precedence <= operators[i].precedence)) and operators[i].isltr

    stack = []
    res = []
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        elif i in operators:
            while helper(stack, i):
                temp = stack.pop()
                res.append(temp)
            stack.append(i)
        else:
            res.append(i)
    for i in stack[::-1]:
        res.append(i)
    return res

def test(data: str, expected: str):
    a = data.split()
    b = expected.split()
    given = toReversePolishNotation(a)
    assert given == b, f"Expected {b}, but got {given}. data: {a}"

test("! ~ x", "x ~ !")
test("! ! value", "value ! !")
test("a * b / c % d", "a b * c / d %")
test("1 + 3 * 2 - 4", "1 3 2 * + 4 -")
test("( 8 + 2 * 5 ) / ( 1 + 3 * 2 - 4 )", "8 2 5 * + 1 3 2 * + 4 - /")
test("x << 2 >> 1", "x 2 << 1 >>")
test("x << 2 >> 1", "x 2 << 1 >>")
test("a & b ^ c | d", "a b & c ^ d |")
test("cond1 && cond2 || cond3", "cond1 cond2 && cond3 ||")
test("~ x * 2 + y >> 1 & mask", "x ~ 2 * y + 1 >> mask &")
test("! ( ( x * 2 ) >> ( y + z || mask ) )", "x 2 * y z + mask || >> !")
test("( ( a & ( b | ( c ^ d ) ) ) + ( e << ( f % 5 ) ) )", "a b c d ^ | & e f 5 % << +")

test("2 ** 3 ** 2", "2 3 2 ** **")
test("a ** b * c + d", "a b ** c * d +")
test("x + y ** z * 2", "x y z ** 2 * +")
test("( a + b ) ** ( c % d )", "a b + c d % **")
test("! x ** 3", "x 3 ** !")
test("a ** b ** c ** d", "a b c d ** ** **")
test("( x ** y ) ** z", "x y ** z **")

print("All tests passed!")