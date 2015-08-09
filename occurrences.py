# Prints index of every `!` from tokenized input.
import ast
import sys

def count(tokens):
    return [i for i, x in enumerate(tokens) if x == '!']

print count(ast.literal_eval(sys.stdin.read()))