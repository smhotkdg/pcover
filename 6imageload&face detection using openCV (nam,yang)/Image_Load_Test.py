import glob
from PIL import Image

File_list = glob.glob('C:/PythonImage/*.png')

for i in File_list:
	print(i)
