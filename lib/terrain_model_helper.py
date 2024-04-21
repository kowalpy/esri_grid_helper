import re


class TerrainModelHelper:
    def __init__(self):
        self.header = ""

    def create_esri_header(self, width, height):
        self.header = f"ncols {width}\n"
        self.header += f"nrows {height}\n"
        self.header += "xllcorner     0.0\nyllcorner     0.0\ncellsize      1.0\nNODATA_value  -9999\n"

    def create_empty_esri(self, file_path, size):
        with open(file_path, "w") as f:
            self.create_esri_header(size, size)
            f.write(self.header)
            one_row = ""
            for i in range(0, size):
                one_row += "0 "
            one_row += "\n"
            for i in range(0, size):
                print(i)
                f.write(one_row)


class Combiner4(TerrainModelHelper):

    WIDTH = "7200"
    HEIGHT = "7200"

    def __init__(self, src_NW, src_SW, src_NE, src_SE, dst):
        super().__init__()
        self.src_NW = src_NW
        self.src_SW = src_SW
        self.src_NE = src_NE
        self.src_SE = src_SE
        self.dst = dst
        self.create_esri_header(self.WIDTH, self.HEIGHT)

    def add_header(self):
        with open(self.dst, "w") as dst:
            dst.write(self.header)

    @staticmethod
    def combine2(left_lines, right_lines, file_handler):
        for n, line in enumerate(left_lines):
            if re.search(r"^\d+", line):
                left_line = line.replace("\n", "")
                left_line = left_line.strip()
                right_line = right_lines[n].replace("\n", "")
                right_line = right_line.strip()
                file_handler.write(f"{left_line} {right_line}\n")

    def combine4(self):
        self.add_header()

        with open(self.src_NW, 'r') as nw:
            nw_lines = nw.readlines()

        with open(self.src_NE, 'r') as ne:
            ne_lines = ne.readlines()

        with open(self.src_SW, 'r') as sw:
            sw_lines = sw.readlines()

        with open(self.src_SE, 'r') as se:
            se_lines = se.readlines()

        with open(self.dst, 'a') as dst:
            self.combine2(nw_lines, ne_lines, dst)
            self.combine2(sw_lines, se_lines, dst)


class Reducer(TerrainModelHelper):

    WIDTH = "3600"
    HEIGHT = "3600"

    def __init__(self, src_file, dst_file):
        super().__init__()
        self.src = src_file
        self.dst = dst_file
        self.create_esri_header(self.WIDTH, self.HEIGHT)

    def add_header(self):
        with open(self.dst, "a") as dst:
            dst.write(self.header)

    def reduce_by_2(self):
        self.add_header()
        with open(self.src, "r") as src:
            src_lines = src.readlines()
        with open(self.dst, "a") as dst:
            for n, line in enumerate(src_lines):
                if re.search(r"^\d+", line):
                    if n % 2 == 0:
                        dst.write(self.reduce_line_elements(line))

    @staticmethod
    def reduce_line_elements(line_to_reduce):
        line_contents = line_to_reduce.replace("\n", "")
        line_contents = line_contents.split(" ")
        reduced_line = ""
        for n, i in enumerate(line_contents):
            if n % 2 == 0:
                reduced_line += f"{i} "
        reduced_line += "\n"
        return reduced_line


class Trimmer(TerrainModelHelper):
    def __init__(self, src_file, dst_file, x_start, y_start, how_many_cut):
        super().__init__()
        self.src_file = src_file
        self.dst_file = dst_file
        self.x_start = x_start
        self.y_start = y_start
        self.how_many_cut = how_many_cut
        self.create_esri_header(how_many_cut, how_many_cut)

    def cut(self):
        with open(self.src_file, "r") as src:
            src_lines = src.readlines()
        src_lines = [x for x in src_lines if re.search(r"^\d+", x)]
        with open(self.dst_file, "w") as dst:
            dst.write(self.header)
            for n, line in enumerate(src_lines):
                if n < self.y_start or n >= self.y_start + self.how_many_cut:
                    pass
                else:
                    trimmed_line = self.trim_row(line)
                    dst.write(trimmed_line)

    def trim_row(self, raw_row):
        row_elements = raw_row.split(" ")
        trimmed_string = ""
        for n, elem in enumerate(row_elements):
            if n < self.x_start or n >= self.x_start + self.how_many_cut:
                pass
            else:
                trimmed_string += f"{elem} "
        trimmed_string += "\n"
        return trimmed_string
