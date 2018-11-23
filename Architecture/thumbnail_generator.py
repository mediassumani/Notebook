"""
A sample program from Description:Anand  Pillai's Software Architecture with Python.
The program generates thumnail of an image concurently using pyhton's threading module.
"""


import threading
import urllib.request
from PIL import Image


def thumbnail_image(url, size=(64, 64), format='.png'):
    """ Save thumbnail of an image URL
        @params :
            - url: the online path to the image
            - size: the prefered size of the image
            - format: the prefered fromat of the image
    """
    im = Image.open(urllib.request.urlopen(url))
    # The filename is the last part of the URL minus the extension + '.format'
    pieces = url.split('/')
    filename = ''.join((pieces[-2],'_',pieces[-1].split('.')[0],'_thumb', format))
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(filename)
    print('Saved', filename)

def main():

    # list of images urls
    img_urls = ['https://dummyimage.com/256x256/000/fff.jpg',
               'https://dummyimage.com/320x240/fff/00.jpg',
               'https://dummyimage.com/640x480/ccc/aaa.jpg',
               'https://dummyimage.com/128x128/ddd/eee.jpg',
               'https://dummyimage.com/720x720/111/222.jpg']

    # converting 5 images sequentally...
    for url in img_urls:
        thumbnail_image(url) # 0.4 seconds per url ...total of 1.776 seconds for all urls


    # converting 5 images concurently...
    for url in img_urls:
        thread = threading.Thread(target=thumbnail_image, args=(url,)) # each url gets a thread
        thread.start() # starts the process
        # 0.121 seconds per url ... total of 0.06 seconds for all


if __name__ == '__main__':
    main()
