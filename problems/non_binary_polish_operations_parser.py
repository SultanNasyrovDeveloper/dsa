"""
(*(+ 3 4 5) 82)
"""
from __future__ import annotations
from operator import add, sub, mul, truediv


OPERATOR_MAP = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


class ExpressionTreeNode:
    text: str
    operation: str
    operands: list[int | ExpressionTreeNode]

    def __init__(self, text: str):
        self.text = text
        self.operands = []

    def print(self):
        print(self.text)
        for operand in self.operands:
            if type(operand) is ExpressionTreeNode:
                operand.print()

    def parse(self):
        self.operation = self.text[1]
        brackets_stack: list[int] = []
        for index in range(1, len(self.text) - 1):
            if self.text[index] == '(':
                brackets_stack.append(index)
            elif self.text[index] == ')':
                expression_start = brackets_stack.pop()
                node = ExpressionTreeNode(self.text[expression_start:index + 1])
                node.parse()
                self.operands.append(node)
            elif self.text[index] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') and len(brackets_stack) == 0:
                self.operands.append(int(self.text[index]))

    def calculate(self) -> int:
        result = 0
        first_operand = self.operands[0]
        if type(first_operand) is ExpressionTreeNode:
            result = first_operand.calculate()
        else:
            result = first_operand
        for operand in self.operands[1:]:
            ...


syntactic_tree = ExpressionTreeNode('(+ (+1 2 3) 3 5)')
syntactic_tree.parse()
syntactic_tree.print()


