#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yuetiezhu on 2019/06/05

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import matplotlib.pyplot as plt
import cv2
import os


def load_im(im):
    return cv2.cvtColor(cv2.imread(im, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)


plt.figure(figsize=(6.4 * 2, 4.8 * 2))
plt.subplot(1, 2, 1)

plt.imshow(load_im('/Users/boxfish/bfprojects/BAGS2/images/out_contour/000000.png'))
plt.title('000000.png', y=-0.05)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(load_im('/Users/boxfish/bfprojects/BAGS2/images/out_contour/000000_outcontour.png'))
plt.axis('off')

plt.title('000000_outcontour.png', y=-0.05)
plt.axis('off')

plt.savefig('/Users/boxfish/bfprojects/BAGS2/images/out_contour/show.png', bbox_inches='tight')
plt.close('all')
print('ok')


plt.figure(figsize=(6.4 * 2, 4.8 * 2))
plt.subplot(1, 2, 1)

plt.imshow(load_im('/Users/boxfish/bfprojects/BAGS2/images/lines/000001.png'))
plt.title('000001.png', y=-0.05)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(load_im('/Users/boxfish/bfprojects/BAGS2/images/lines/000001_lines.png'))
plt.axis('off')

plt.title('000001_lines.png', y=-0.05)
plt.axis('off')

plt.savefig('/Users/boxfish/bfprojects/BAGS2/images/lines/show.png', bbox_inches='tight')
plt.close('all')
print('ok')

