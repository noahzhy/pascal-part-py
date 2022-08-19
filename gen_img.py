import os
import glob
from shutil import copyfile

import numpy as np
from PIL import Image

from anno import ImageAnnotation

# TODO RGBA
# pick what you need in part2ind.py -> # [person]
pick_parts = {
    '': 0,

    'head': 1,
    'neck': 2,
    'torso': 2,

    'luleg': 3,               	    # left upper leg
    'ruleg': 4,               	    # right upper leg

    'llleg': 5,               	    # left lower leg
    'rlleg': 6,               	    # right lower leg

    'lfoot': 7,               	    # left foot
    'rfoot': 8,               	    # right foot

    'luarm': 9,                     # left upper arm
    'ruarm': 10,                    # right upper arm

    'llarm': 11,                    # left lower arm
    'rlarm': 12,                    # right lower arm

    'lhand': 13,                    # left hand
    'rhand': 14,                    # right hand
}


if __name__ == '__main__':
    file_path = r'D:\dataset/pascal_person_part_revision_14\seg_anno'
    for matrix_file in glob.glob(os.path.join(file_path, '*.mat')):
        file_name = os.path.basename(matrix_file).split('.')[0]
        image_file = os.path.join(file_path, "{}.jpg".format(file_name))
        
        # image_file = r'D:\pascal_person_part_24\seg_anno\2008_001366.jpg'
        # matrix_file = r'D:\pascal_person_part_24\seg_anno\2008_001366.mat'

        an = ImageAnnotation(image_file, matrix_file)

        h, w = Image.open(image_file).size
        img = np.full((w, h), fill_value=0)

        for p in pick_parts.keys():
            for _object in an.objects:
                if _object.class_name == 'person':
                    for parts in _object.parts:
                        if parts.part_name == p:
                            idx_part = pick_parts[parts.part_name]
                            img = np.where(parts.mask, idx_part, img)

        im = Image.fromarray(img)
        print(np.max(im), file_name)
        im.save(os.path.join(file_path, "{}.png".format(file_name)))
        # im.show()
        # quit()
