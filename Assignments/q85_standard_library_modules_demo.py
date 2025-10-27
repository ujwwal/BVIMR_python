import os
import sys
from datetime import datetime, date, timedelta
import random
import statistics
from pathlib import Path
import itertools
from collections import Counter, defaultdict

if __name__ == "__main__":
    print("os.getcwd():", os.getcwd())
    print("sys.version:", sys.version.splitlines()[0])

    now = datetime.now()
    print("datetime.now():", now)
    print("date.today():", date.today())
    print("timedelta(days=7) from now:", now + timedelta(days=7))

    print("random.randint(1, 10):", random.randint(1, 10))
    print("random.choice(['a','b','c']):", random.choice(['a','b','c']))

    data = [1, 2, 2, 3, 4, 4, 4]
    print("statistics.mean:", statistics.mean(data))
    print("statistics.median:", statistics.median(data))
    print("statistics.mode:", statistics.mode(data))

    p = Path(".")
    print("pathlib.Path('.') absolute:", p.resolve())
    print("Python files in current dir:", [str(x) for x in p.glob("*.py")])

    print("itertools.combinations([1,2,3], 2):", list(itertools.combinations([1,2,3], 2)))
    print("itertools.permutations('ab', 2):", list(itertools.permutations("ab", 2)))

    text = "mississippi"
    print("collections.Counter:", Counter(text))
    dd = defaultdict(int)
    for ch in text:
        dd[ch] += 1
    print("collections.defaultdict counts:", dict(dd))