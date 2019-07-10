
import sys

fi = sys.stdin
fo = sys.stdout
fe = sys.stderr


for line in fi:
    if "pg_" in line and "swp" not in line: 
        print(line, end="")
