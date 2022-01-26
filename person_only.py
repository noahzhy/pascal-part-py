import os
import glob
from shutil import copyfile

from anno import ImageAnnotation


if __name__ == '__main__':
    save_path = r'D:\pascal_person_part_24\seg_anno'
    image_path = r'D:\pascal_person_part_24\JPEGImages'
    annotation_matrix_path = r'D:\pascal_person_part_24\Annotations_Part'
    for matrix_file in glob.glob(os.path.join(annotation_matrix_path, '*.mat')):
        # print(matrix_file)
        file_name = os.path.basename(matrix_file).split('.')[0]
        image_file = os.path.join(image_path, "{}.jpg".format(file_name))
        an = ImageAnnotation(image_file, matrix_file)
        class_list = [_object.class_name for _object in an.objects]
        print(class_list)
        if 'person' in class_list:
            copyfile(matrix_file, os.path.join(save_path, os.path.basename(matrix_file)))
            copyfile(image_file, os.path.join(save_path, "{}.jpg".format(file_name)))
