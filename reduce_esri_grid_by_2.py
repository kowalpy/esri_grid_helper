# This is an example of reducing amount of points by 2

from lib.terrain_model_helper import Reducer

# replace example parameters with yours
base_dir = "/home/marcin/model_terenu/jaxa_data/tatry/"
src = f"{base_dir}tatry_zlozone_z_4.asc"
dst = f"{base_dir}tatry_zlozone_z_4_redukowane.asc"

red = Reducer(src, dst)
red.reduce_by_2()
