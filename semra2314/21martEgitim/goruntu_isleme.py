import cv2

# 2.görüntüyü yükledik
image = cv2.imread(r"C:\Users\semra\Desktop\jarvis\21martEgitim\Lena.png")

# 2.görüntüyü ekrana gösterelim
cv2.imshow("Lena", image)
cv2.waitKey(0) #süresiz olarak ekranda gözükmesini sağlıyor

# 3.görüntüde matrix işlemleri
B =image[:,:,0]
G =image[:,:,1]
R =image[:,:,2]

print(image.shape)

merged_image=cv2.hconcat([B,G,R])
cv2.imshow("merge",merged_image)
cv2.imshow("normal_image",image)
cv2.waitKey(0)

# 4.görüntüyü gri tonlamaya çevirelim
gray_image =cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gri",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5.görüntüyü bulanıklaştıralım
blurred_image=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blurred image",blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6.görüntü üzerinde kenar tespiti yapalım


