import sys, os
from PIL import Image, ImageFilter

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# chech /New exist or not, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through the folder
image_list = os.listdir(image_folder)
for filename in image_list:
    # convert the image
    image = Image.open(f'{image_folder}{filename}')
    # get the filename without extension
    cleanname = os.path.splitext(filename)[0]
    # save the images in new folder
    image.save(f'{output_folder}{cleanname}.png','png')