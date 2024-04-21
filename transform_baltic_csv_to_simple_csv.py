# This is file to convert Leibniz institute Baltic Sea topographic map into simple CSV file

src_file = "/home/marcin/model_terenu/baltyk/iowtopo2_rev03.dat"
dst_file = "/home/marcin/model_terenu/baltyk/iowtopo2_rev03_converted.csv"

converted = ""
src_lines = []
converted_lines = []
with open(src_file, "r") as f:
    src_lines = f.readlines()

src_lines = src_lines[2:]

for line in src_lines:
    contents = line.split(" ")
    contents = [x for x in contents if x]
    contents = [contents[0], contents[1], contents[2]]
    print(contents)
    converted_lines.append(contents)

for content in converted_lines:
    converted += f"{content[1]}, {content[0]}, {content[2]}\n"

with open(dst_file, "w") as f:
    f.write(converted)
