def get_lines_and_count(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        count = len(lines)
    return lines, count
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"Имя файла: {item[0]}\n")
            file.write(f"Количество строк: {item[1]}\n")
            file.writelines(item[2])

filenames = ['1.txt', '2.txt', '3.txt']
file_data = []

for name in filenames:
    lines, count = get_lines_and_count(name)
    file_data.append((name, count, lines))

file_data.sort(key=lambda x: x[1])

write_to_file('combined.txt', file_data)
