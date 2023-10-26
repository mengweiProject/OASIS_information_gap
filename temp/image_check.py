

from PIL import Image, ImageFilter

file_path = r"C:\Users\13395\Pictures\Camera Roll\small_cute1.jpg"

#
# # 打开图像
# image = Image.open(r"C:\Users\13395\Pictures\Camera Roll\small_cute1.jpg")
#
# # 应用锐化滤镜
# sharpened_image = image.filter(ImageFilter.SHARPEN)
#
# # 保存处理后的图像
# sharpened_image.save(r"C:\Users\13395\Pictures\Camera Roll\output_image.jpg")

import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# 定义SRCNN模型
class SRCNN(nn.Module):
    def __init__(self):
        super(SRCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=9, padding=4)
        self.conv2 = nn.Conv2d(64, 32, kernel_size=1, padding=0)
        self.conv3 = nn.Conv2d(32, 3, kernel_size=5, padding=2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.conv3(x)
        return x

# 加载SRCNN模型权重
model = SRCNN()
model.load_state_dict(torch.load('srcnn_model.pt', map_location=torch.device('cpu')))
model.eval()

# 加载图像并进行预处理
image = Image.open('input_image.jpg')
preprocess = transforms.ToTensor()
input_tensor = preprocess(image).unsqueeze(0)

# 使用SRCNN模型进行超分辨率重建
with torch.no_grad():
    output_tensor = model(input_tensor)

# 将输出张量转换回图像
output_image = output_tensor.squeeze(0).clamp(0, 1).numpy()
output_image = transforms.ToPILImage()(output_image)

# 显示原始图像和超分辨率重建图像
image.show()
output_image.show()