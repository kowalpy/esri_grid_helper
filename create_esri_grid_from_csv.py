# This script takes csv file and creates esri grid file from it
# CSV file example format:
# 609382, 200663, 13.6
# 609382, 200728, 14.8
# 609382, 200793, 22.3
# 609382, 200858, 19.5
# 609382, 200923, 27.5
# ...

# replace below example paths with yours
src_file = "/home/marcin/model_terenu/dane_z_gugik/kotlina_klodzka.txt"
dst_file = "/home/marcin/model_terenu/dane_z_gugik_obrobione/kotlina_klodzka.asc"
src_file = "/home/marcin/model_terenu/baltyk/iowtopo2_rev03_converted.csv"
dst_file = "/home/marcin/model_terenu/baltyk/iowtopo2_rev03_converted.asc"

lines = []


class Point:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def __repr__(self):
        repr_str = f"x={self.x}, y={self.y}, h={self.h}"
        return repr_str


with open(src_file, "r") as f:
    lines = f.readlines()

points = []

for i in lines:
    i_split = i.split(",")
    new_point = Point(i_split[0].strip(), i_split[1].strip(), i_split[2].strip())
    points.append(new_point)

print(points)

points_by_x = {}

for j in points:
    if j.x not in points_by_x.keys():
        points_by_x[j.x] = []
    points_by_x[j.x].append(j)

print(points_by_x.keys())

keys = list(points_by_x.keys())

ncols = str(len(points_by_x[keys[0]]))
nrows = str(len(points_by_x.keys()))

esri_grid = f"ncols {ncols}\nnrows {nrows}\n"
esri_grid += """xllcorner     0.0
yllcorner     0.0
cellsize      1.0
NODATA_value  -9999
"""

unique_columns_number = []

for k in points_by_x.keys():
    how_many_columns = 0
    for p in points_by_x[k]:
        esri_grid += p.h + " "
        how_many_columns += 1
    esri_grid = esri_grid[:-1]
    esri_grid += "\n"
    print(how_many_columns)
    if how_many_columns not in unique_columns_number:
        unique_columns_number.append(how_many_columns)

with open(dst_file, "w") as f:
    f.write(esri_grid)

print(f"unique_columns_number: {unique_columns_number}")
