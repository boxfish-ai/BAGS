#!/usr/bin/env bash

# download the data set for detecting outer contour
mkdir out_contour
cd out_contour

url_prefix=http://web-page-open.oss-cn-beijing.aliyuncs.com/out_contour/
for index in {0..8499}
    do
        index_formatted=`printf "%06d" ${index}`
        url=${url_prefix}${index_formatted}.png
        wget ${url}
        url=${url_prefix}${index_formatted}_outcontour.png
        wget ${url}
    done


# download the data set for detecting underlines
cd ../
mkdir lines
cd lines

url_prefix=http://web-page-open.oss-cn-beijing.aliyuncs.com/lines/
for index in {0..7999}
    do
        index_formatted=`printf "%06d" ${index}`
        url=${url_prefix}${index_formatted}.png
        wget ${url}
        url=${url_prefix}${index_formatted}_lines.png
        wget ${url}
    done
