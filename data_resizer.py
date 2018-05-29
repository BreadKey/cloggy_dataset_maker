import glob
import imageProcessor
import os
import cv2

root_path = './results'
dirs = next(os.walk(root_path))[1]
wanted_size = (120, 120)

for dir in dirs:
    path = os.path.join(root_path, dir)
    final_dirs = next(os.walk(path))[1]
    for final_dir in final_dirs:
        data_dir_path = os.path.join(path, final_dir)
        for data_path in glob.glob(os.path.join(data_dir_path, '*.png')):
            data = cv2.imread(data_path, 0)
            height, width = data.shape[:2]
            rect = (0, 0, width, height)
            resized_data = imageProcessor.resizeImage(data, wanted_size, rect, True)
            cv2.imwrite(data_path, resized_data)