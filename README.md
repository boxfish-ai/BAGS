# BAGS
Boxfish Automatic Grading System("BAGS: An automatic homework grading system using the pictures taken by smart phones")

## Framework
![framework](./images/framework.png?raw=true "framework")
## Datasets
DatasetA and DatasetB are publicy available. 

### Introduction to the Datasets
Dataset A is used for rectangular borderlines segmentation, which consists of 8500 images.
Dataset B is used for answer area underlines(AAU) segmentation, which consists of 8000 images.

### Examples

Each image is in grayscale and has a corresponding mask. 

In dataset A. We add "_outcontour" in the corresponding mask name.
![outcontour](images/out_contour/show.png "outcontour")


In dataset B. We add "_lines" in the corresponding mask name.
![lines](images/lines/show.png "lines")


### How to Download the Datasets
All the images（about 26.1GB） are stored in aliyun. You can download them using following script:
```sh
sh dataset/download_dataset.sh
```
or
```sh
python dataset/download_dataset.py
```

## Lisence
...
