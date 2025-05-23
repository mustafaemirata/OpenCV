import cv2 as cv
import os

# Tam görüntü yolu
image_name = "/home/emir/PycharmProjects/OpenCV/01_Temel_Islemler/02_Gray_Image/opencv.png"

# Tam kayıt yolu
save_path = "/home/emir/PycharmProjects/OpenCV/01_Temel_Islemler/02_Gray_Image/"

# Görüntüyü oku
img = cv.imread(image_name)

if img is None:
    print("Hata: Görüntü yüklenemedi. Lütfen dosya yolunu kontrol edin.")
    print(f"Denenen yol: {image_name}")
    exit()

# Griye çevir
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Göster
cv.imshow("gray", gray)
cv.waitKey(0)

if not os.path.exists(save_path):
    os.makedirs(save_path)

output_file = os.path.join(save_path, "yeni.png")
success = cv.imwrite(output_file, gray)

if success:
    print("Gri resim başarıyla kaydedildi:", output_file)
else:
    print("Kaydetme başarısız!")

cv.destroyAllWindows()
