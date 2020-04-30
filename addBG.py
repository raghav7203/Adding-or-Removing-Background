import cv2
import matplotlib.pyplot as plt

img_path = "3.png"

#saving image into a white bg
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
plt.imshow(img)
plt.show()
b,g,r, a = cv2.split(img)
print(img.shape)

new_img  = cv2.merge((b, g, r))
not_a = cv2.bitwise_not(a)
not_a = cv2.cvtColor(not_a, cv2.COLOR_GRAY2BGR)
plt.imshow(not_a)
cv2.imwrite('added1.png', not_a)
plt.show()
new_img = cv2.bitwise_and(new_img,new_img,mask = a)
new_img = cv2.add(new_img, not_a)

cv2.imwrite('added.png', new_img)
plt.imshow(new_img)
print(new_img.shape)
plt.show()
