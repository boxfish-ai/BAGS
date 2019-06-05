# BAGS
the Boxfish Automatic homework Grading System
## Framework
![framework](./images/framework.png?raw=true "framework")
## Datasets
Two datasets are available in this repo. 

### Introduction to the Datasets
Dataset A is used for rectangular borderlines segmentation, which consists of 8500 pairs of images.
Dataset B is used for answer area underlines(AAU) segmentation, which consists of 8000 pairs of images.

There are one original grayscale image and  one tagged binary image corresponding to the gray image in a pair of images. 
They are named in this way: the original grayscale image is named as "***index***.png", and the tagged binary image is named as "***index***_outcontour.png"(for Dataset A) or "***index***_lines.png"(for Dataset B). 
"***Index***" is an integer type number with a constant length of 6 by adding leading zeros to the left of it.
They have the same formatted ***index*** in each pair.

### Examples
One example pair of dataset A. The original image is named as 'out_contour/000000.png'.
![A_ori](images/out_contour/000000.png "A_ori")
And the tagged image is named as 'out_contour/000000_outcontour.png'.
![A_tagged](images/out_contour/000000_outcontour.png "A_tagged")


One example pair of dataset B. the original image is named as 'lines/000001.png'.
![B_ori](images/lines/000001.png "B_ori")
And the tagged image is named as 'lines/000001_lines.png'.
![B_tagged](images/lines/000001_lines.png "B_tagged")


### How to Download the Datasets
All the images（about 26.1GB） are stored in aliyun. You could download the two datasets as follow:
```sh
sh dataset/download_dataset.sh
```
or
```sh
python dataset/download_dataset.py
```
