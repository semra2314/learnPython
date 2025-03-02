import torch as tc
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms, datasets
from torch import optim
import torchvision.models as mo
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
import os
from dotenv import load_dotenv
from torch import nn
from matplotlib import pyplot as plt
from math import sqrt

# Model Manupilasyonu

load_dotenv()

device = "cuda" if tc.cuda.is_available() else "cpu"
batch = 64

model = mo.alexnet()
model2 = mo.resnet101()
model3 = mo.efficientnet_b0()

print(model, model2, model3)

criterion = nn.CrossEntropyLoss().to(device)

optimizer = optim.Adam(model.parameters(), lr = .001)

transform = transforms.Compose([
    transforms.ToTensor(),
])
transform_to_pil = transforms.Compose([
    transforms.ToPILImage()
])


training_images = datasets.CIFAR10(root="./data", train=True, download=True, transform=transform)

training_data = DataLoader(training_images, batch_size=batch, shuffle=True)



dataiter = iter(training_data)
images, labels = next(dataiter)
num = int(sqrt(batch))

grid = make_grid(images, nrow=num)
topil = grid.permute(1, 2, 0)


plt.figure(figsize=(num, num))
plt.imshow(topil)
plt.axis("off")

plt.show()


