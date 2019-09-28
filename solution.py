NAME_FILE = 'tasks'

f = open(NAME_FILE)
line = f.readline().replace('\n', '')
all_writes = []

while line:
    example = line.split(" ")
    if example[1] == '+':
        to_write = f'{line} = {int(example[0]) + int(example[2])}'
    elif example[1] == '-':
        to_write = f'{line} = {int(example[0]) - int(example[2])}'
    else:
        to_write = f'Cannot find solution in {line}'
    all_writes.append(to_write)
    line = f.readline().replace('\n', '')
f.close()

f = open(NAME_FILE, 'w')
for line in all_writes:
    f.write(line + '\n')