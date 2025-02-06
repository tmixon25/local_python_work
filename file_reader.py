from pathlib import Path

# path=Path('pi_digits.txt')
path=Path('pi_million_digits.txt')
contents=path.read_text()
# contents=path.read_text().rstrip()
# contents=contents.rstrip()
# print(contents)
lines=contents.splitlines()
# for line in lines:
    # print(line)
pi_string=''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))