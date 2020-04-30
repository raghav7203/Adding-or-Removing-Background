import os
import cv2
import matplotlib.pyplot as plt


def get_images(path):
    data = os.listdir(path)
    return data


images = get_images('./images/0/')

for i in range(0,len(images)):
  img = cv2.imread('./images/0/'+ images[i], cv2.IMREAD_UNCHANGED)

  b,g,r, a = cv2.split(img)

  new_img  = cv2.merge((b, g, r))
  not_a = cv2.bitwise_not(a)
  not_a = cv2.cvtColor(not_a, cv2.COLOR_GRAY2BGR)

  cv2.imwrite('./generated/zero_'+str(i)+'.png', not_a)
