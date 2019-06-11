# BAGS
Boxfish Automatic Grading System ("BAGS: An automatic homework grading system using the pictures taken by smart phones", ICDAR 2019)

### [Paper on arXiv](https://arxiv.org/abs/1906.03767)

## Framework
![framework](./images/framework.png?raw=true "framework")
## Datasets
DatasetA and DatasetB are publicly available. 

### Introduction to the Datasets
Dataset A is used for rectangular borderlines segmentation, which consists of 8500 images.

Dataset B is used for answer area underlines(AAU) segmentation, which consists of 8000 images.

### Examples

Each image is in grayscale and has a corresponding mask. 

In dataset A，we add "_outcontour" in the corresponding mask name.
![outcontour](images/out_contour/show.png "outcontour")


In dataset B, we add "_lines" in the corresponding mask name.
![lines](images/lines/show.png "lines")


### How to Download the Datasets
All the images（about 26.1GB） are stored in aliyun, which can be downloaded using following script:
```sh
sh dataset/download_dataset.sh
```
or
```sh
python dataset/download_dataset.py
```

## Citation 
If you use the datasets in your research, please cite:
```bibtex
@article{li2019BAGS,
  title={BAGS: An automatic homework grading system using the pictures taken by smart phones},
  author={Xiaoshuo Li and Tiezhu Yue and Xuanping Huang and Zhe Yang and Gang Xu},
  journal={arXiv preprint arXiv:1906.03767},
  year={2019}
}
```
