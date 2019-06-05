# coding=utf-8
import os
import argparse
try:
    # python 2
    from urllib2 import urlopen
except ImportError:
    # python3
    from urllib.request import urlopen


URL_PREFIX = 'http://web-page-open.oss-cn-beijing.aliyuncs.com'


def load(url, dst):
    print('downloading {0}'.format(url))
    response = urlopen(url)
    data = response.read()

    with open(dst, 'wb') as f:
        f.write(data)


def mk_dir(path):
    dir_name = os.path.dirname(path)
    if not os.path.exists(dir_name):
        mk_dir(dir_name)
        os.mkdir(dir_name)


def load_dataset(dst_folder, dataset='out_contour'):
    if dataset == 'out_contour':
        size = 8500
        key1 = '{0}/out_contour/{1:06d}.png'
        key2 = '{0}/out_contour/{1:06d}_outcontour.png'
    elif dataset == 'lines':
        size = 8000
        key1 = '{0}/lines/{1:06d}.png'
        key2 = '{0}/lines/{1:06d}_lines.png'
    else:
        raise ValueError

    mk_dir(os.path.join(key1.format(dst_folder, 0)))

    for i in range(size):
        oss_key1 = key1.format(URL_PREFIX, i)
        dst_key1 = key1.format(dst_folder, i)
        load(oss_key1, dst_key1)

        oss_key2 = key2.format(URL_PREFIX, i)
        dst_key2 = key2.format(dst_folder, i)
        load(oss_key2, dst_key2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""a script to download the data sets
        """)

    parser.add_argument('folder', help='the destination folder to save the images.')
    args = parser.parse_args()

    load_dataset(args.folder, dataset='out_contour')
    load_dataset(args.folder, dataset='lines')




