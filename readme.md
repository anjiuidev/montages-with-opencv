# Creating montages with openCV
In this we’ll learn how to use create a simple Python + OpenCV script to Creating montages.  

**The build_montages  function requires three arguments:**
- **image_list** : This parameter is a list of images loaded via OpenCV. In our case, we supply the images  list.
- **image_shape** : A tuple containing the width and height of each image in the montage. Here we indicate that all images in the montage will be resized to 129 x 196. Resizing every image in the montage to a fixed size is a requirement so we can properly allocate memory in the resulting NumPy array. Note: Empty space in the montage will be filled with black pixels.
- **montage_shape** : A second tuple, this one specifying the number of columns and rows in the montage. Here we indicate that our montage will have 7 columns (7 images wide) and 3 rows (3 images tall).

**commands to run**
- python montages.py -i images
- python montages.py -i images -s 30