import os
import numpy as np
import cv2
import argparse
from tqdm import tqdm

image_list = os.listdir(os.getcwd() + "/images")

if os.path.exists("result") is False:
    os.mkdir('./result')

result_dir = os.getcwd() + "/result"


def args():
    parser = argparse.ArgumentParser()
    #parser.add_argument("--pdf_dir", type = str, help = "PDF dir not file name")
    parser.add_argument("--w", type = int, help = "number of images will be in width")
    parser.add_argument("--h", type = int, help = "number of images will be in height")
    parser.add_argument("--resize", type = str, default = False, help = "print resize options")
    return parser.parse_args()

def concat(image_list, w, h, big_image, resize_mode):
    image = cv2.imread('./images/' + image_list[0])
    w_size = image.shape[1]
    h_size = image.shape[0]
    ww = 0
    hh = 0
    for i in tqdm(image_list):
        image = cv2.imread('./images/' + i)
        big_image[h_size*hh : h_size*(hh + 1), w_size*ww : w_size*(ww + 1), :] = image

        ww += 1
        if ww == w:
            ww = 0
            hh += 1
        
    cv2.imwrite("./result/concatenated.png", cv2.cvtColor(big_image.astype('uint8'), cv2.COLOR_BGR2RGB))
    cv2.imwrite("./result/concatenated_resized2.png", cv2.cvtColor(cv2.resize(big_image, dsize=(int(w_size*w/2), int(h_size*h/2)), interpolation=resize_mode).astype('uint8'), cv2.COLOR_BGR2RGB))
    cv2.imwrite("./result/concatenated_resized4.png", cv2.cvtColor(cv2.resize(big_image, dsize=(int(w_size*w/4), int(h_size*h/4)), interpolation=resize_mode).astype('uint8'), cv2.COLOR_BGR2RGB))
    cv2.imwrite("./result/concatenated_resized6.png", cv2.cvtColor(cv2.resize(big_image, dsize=(int(w_size*w/6), int(h_size*h/6)), interpolation=resize_mode).astype('uint8'), cv2.COLOR_BGR2RGB))
    cv2.imwrite("./result/concatenated_resized10.png", cv2.cvtColor(cv2.resize(big_image, dsize=(int(w_size*w/8), int(h_size*h/8)), interpolation=resize_mode).astype('uint8'), cv2.COLOR_BGR2RGB))

def big_image(image_list, w, h):
    
    image = cv2.imread('./images/' + image_list[0])
    print(image.shape)
    height = image.shape[0]*h
    width = image.shape[1]*w

    return np.zeros([ height, width, 3 ])  # If gray chagne here 3 -> 1!


if __name__=="__main__":
    args = args()
    w = args.w
    h = args.h
    mode_list= ["cv2.INTER_NEAREST", "cv2.INTER_LINEAR", "cv2.INTER_AREA", "cv2.INTER_CUBIC", "cv2.INTER_LANCZOS4"]
    mode_list_= [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_AREA, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]
    resize_mode = 3
    if args.resize == "True":
        for n, i in enumerate(mode_list):
            print(n, i)
        print("Enter number of interpolation")
        resize_mode = int(input())
    resize_mode = mode_list_[resize_mode]
    print("wait!!!!!!!!!!!!!!!!!!!")
    big_image = big_image(image_list, w, h)
    concat(image_list, w, h, big_image, resize_mode)
    print("Done!!!!!!!!!!!!!!!!!!")