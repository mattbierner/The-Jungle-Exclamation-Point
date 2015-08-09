import ast
import sys

def count(tokens):
    words = len(tokens)
    exclamations = tokens.count('Jurgis')
    return float(exclamations) / words

def count_chapters(chapters):
    return [count(x) for x in chapters]

print count_chapters(ast.literal_eval(sys.stdin.read()))