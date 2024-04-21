# This is an example of how 4 esri grid squares of equal size could be combined together

from lib.terrain_model_helper import Combiner4

# replace below paths with yours
base_dir = "/home/marcin/model_terenu/jaxa_data/tatry/"
src_NW = f"{base_dir}tatry_gorny_lewy_ALPSMLC30_N049E019_DSM.asc"
src_SW = f"{base_dir}tatry_dolny_lewy_ALPSMLC30_N048E019_DSM.asc"
src_NE = f"{base_dir}tatry_gorny_prawy_ALPSMLC30_N049E020_DSM.asc"
src_SE = f"{base_dir}tatry_dolny_prawy_ALPSMLC30_N048E020_DSM.asc"
dst = f"{base_dir}tatry_zlozone_z_4.asc"

c4 = Combiner4(src_NW, src_SW, src_NE, src_SE, dst)
c4.combine4()
