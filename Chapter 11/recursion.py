from bakery import assert_equal
from dataclasses import dataclass


@dataclass
class Expression:
    pass


@dataclass
class BinaryExpression(Expression):
    operator: str
    left: Expression
    right: Expression


@dataclass
class IntegerExpression(Expression):
    value: int


###### Edit below #################################################################

def evaluate_math(expression: Expression) -> int:
    if isinstance(expression, IntegerExpression):
        # In this base case, you *know* that expression is an IntegerExpression!
        return expression.value
    # In this recursive case, you *know* that expression is a BinaryExpression!
    left_value = evaluate_math(expression.left)
    right_value = evaluate_math(expression.right)
    if expression.operator == "+":
        return left_value + right_value
    elif expression.operator == "*":
        return left_value * right_value


# 5 + 3
assert_equal(evaluate_math(BinaryExpression("+", IntegerExpression(5), IntegerExpression(3))), 8)
# 3 * 4
assert_equal(evaluate_math(BinaryExpression("*", IntegerExpression(3), IntegerExpression(4))), 12)
# (2 * 5) + (5 * 3)
assert_equal(evaluate_math(BinaryExpression("+",
                                            BinaryExpression("*", IntegerExpression(2), IntegerExpression(5)),
                                            BinaryExpression("*", IntegerExpression(5), IntegerExpression(3)))), 25)
# (2 * (5 + 5)) * 3
assert_equal(evaluate_math(BinaryExpression("*",
                                            BinaryExpression("*",
                                                             BinaryExpression("+", IntegerExpression(5),
                                                                              IntegerExpression(5)),
                                                             IntegerExpression(5)),
                                            IntegerExpression(3))), 23)