# This is an example of cutting fragment of ESRI file

from lib.terrain_model_helper import Trimmer

# replace example parameters with yours
base_dir = "/home/marcin/model_terenu/jaxa_data/tatry/"
src = f"{base_dir}tatry_zlozone_z_4_redukowane.asc"
dst = f"{base_dir}tatry_zlozone_z_4_redukowane_obciete.asc"
tr = Trimmer(src, dst, 800, 400, 2600-800)
tr.cut()
