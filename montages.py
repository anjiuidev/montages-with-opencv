# import the packages
import cv2
import random
import argparse
from imutils import paths
from imutils import build_montages

# argument parser construction
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="Path to input directory of images")
ap.add_argument("-s", "--sample", type=int, default=21, help="# of images to sample")
args = vars(ap.parse_args())

# grab the paths to the images, then randomly select a sample of them
imagePaths = list(paths.list_images(args["images"]))
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

# initializing images
images = []

# loop over imagePaths and read the each image and append it to images list.
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)

# use imutils helper function to build the montages
montages = build_montages(images, (128,196), (7,3))

# loop over the montages and display each of them
for montage in montages:
	cv2.imshow("Montage", montage)
	cv2.waitKey(0)