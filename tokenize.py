import argparse
import re
from cStringIO import StringIO
import subprocess
import sys

def npl_tokenize(file):
    p = subprocess.Popen(["apache-opennlp-1.5.3/bin/opennlp", "SimpleTokenizer"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate(file.read())
    return out

def tokenize(file):
    return re.findall('(\w+|\!)', file.read())

def tokenize_per_chapter(file):
    chapters = re.split('Chapter\s+\d+', file.read(), flags=re.M)
    return [tokenize(StringIO(x)) for x in chapters[1:]]

def tokenize_per_chapter_no_quotes(file):
    no_quote_text = re.split('"[^"]*"', file.read(), flags=re.M)
    chapters = re.split('Chapter\s+\d+', " ".join(no_quote_text), flags=re.M)
    return [tokenize(StringIO(x)) for x in chapters[1:]]


print tokenize_per_chapter_no_quotes(sys.stdin)