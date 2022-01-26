import os
import glob
from shutil import copyfile

import numpy as np
from PIL import Image

from anno import ImageAnnotation

# TODO RGBA, keep A for 
pick_parts = {
    '':(),
    # 'hair': (255, 255, 255),
    'head': (255, 255, 255),
    'torso': (255, 255, 255),

    'luleg': (255, 255, 255),               	# left upper leg
    'ruleg': (255, 255, 255),               	# right upper leg

    'llleg': (255, 255, 255),               	# left lower leg
    'rlleg': (255, 255, 255),               	# right lower leg

    'lfoot': (255, 255, 255),               	# left foot
    'rfoot': (255, 255, 255),               	# right foot

    'luarm': (255, 255, 255),                   # left upper arm
    'ruarm': (255, 255, 255),                   # right upper arm

    'llarm': (255, 255, 255),                   # left lower arm
    'rlarm': (255, 255, 255),                   # right lower arm

    'lhand': (255, 255, 255),                   # left hand
    'rhand': (255, 255, 255),                   # right hand
}


if __name__ == '__main__':
    file_path = r'D:\pascal_person_part_24\seg_anno'
    for matrix_file in glob.glob(os.path.join(file_path, '*.mat')):
        file_name = os.path.basename(matrix_file).split('.')[0]
        image_file = os.path.join(file_path, "{}.jpg".format(file_name))
        
        # image_file = r'D:\pascal_person_part_24\seg_anno\2008_001366.jpg'
        # matrix_file = r'D:\pascal_person_part_24\seg_anno\2008_001366.mat'

        an = ImageAnnotation(image_file, matrix_file)

        h, w = Image.open(image_file).size
        img = np.zeros((w, h))

        for p in pick_parts.keys():
            for _object in an.objects:
                if _object.class_name == 'person':
                        for parts in _object.parts:
                            if parts.part_name == p:

                    # if parts.part_name in pick_parts.keys():
                                img = np.where(parts.mask, (list(pick_parts.keys()).index(parts.part_name))*15, img)

        im = Image.fromarray(img).convert('RGBA')
        print(matrix_file)
        im.save(os.path.join(file_path, "{}.png".format(file_name)))
        # im.show()
        # quit()
