import os

# 遍历目录
for root, dirs, files in os.walk("./"):
    for file in files:
        file_path = os.path.join(root, file)
        if not file.endswith('.md'):
            continue
        lines = open(file_path, encoding='utf8').readlines()

        if '******\n' not in lines:
            print(f'skip {file_path}')
            continue

        start = lines.index('******\n')
        end = lines[start+1:].index('******\n')
        end += start
        common_lines = open('README.md').readlines()
        if start >= end:
            print(f'skip {file_path}')
            continue
        print(f'processing {file_path}')
        lines = lines[:start + 1] + common_lines + lines[end:]
        file = open(file_path, 'w')
        for line in lines:
            line = line.replace('images/orders.png', '../images/orders.png')
            file.write(line)
        file.close()
