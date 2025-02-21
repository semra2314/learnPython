# Example pytorch usage for python
import torch as tc
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms
import torchvision
import os
from dotenv import load_dotenv


load_dotenv()  # .env dosyasındaki değişkenleri yükler

device = "cuda:0" if tc.cuda.is_available() else "cpu" # Çalışacak cihazı belirleme. GPU yada CPU

kernel = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
        ] # Sobel operatörünü temsil eden bir kenar bulma maskesi

transform = transforms.ToTensor() # Tensor a dönüştürme fonksiyonu oluşturma
to_pil = transforms.ToPILImage() # PIL formatına dönüştürme fonksiyonu oluşturma

img = Image.open(os.getenv("Image_file")) # Resim dosyasını alma
img = img.convert("L") # Grayscale formatına dönüştürme
img.show() # İlk resmi görüntüleme
img_tensor = transform(img).unsqueeze(0).to(device) # Resmi tensor a dönüştürme. Format: [Height, Width, Channel] --> [Batch_size, Channel, Height, Width]

kernel = tc.tensor(kernel, dtype=tc.float32).to(device) # Kerneli tensora dönüştürme ve işlemleri GPU'ya atama
kernel = kernel.unsqueeze(0).unsqueeze(0) # [3, 3] Formatındaki maskeyi 4 boyutlu hale getirme [1, 1, 3, 3]
out = F.conv2d(img_tensor, kernel, padding=1) # Konvolüsyonu oluşturma ve kenarına bir adet pixel ekleme (padding işlemi)
out = out.squeeze(0).cpu().detach().numpy() # Resmin kendisini [Batch_size, Channel, Height, Width] şeklinden [Channel, Height, Width] haline dönüştürme (sıkıştırma işlemi yapma) gpu dan çıkarma kopyalama ve numpy öğesine dönüştürme
print(type(out)) # Çıkan öğenin tipini yazdırma
out_image = out.transpose(1, 2, 0) # Resmin formatını değiştirme [Channel, Height, Width] --> [Height, Width, Channel] Not: Resimler [H, W, C] şeklinde işlenir tensorlar [B, C, H, W] şeklinde işlenir

to_pil(out_image).show() # Son çıkan resmi görüntüleme

