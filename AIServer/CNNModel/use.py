import os
import torch
from torchvision import models
from torchvision import transforms
from PIL import Image

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定义模型结构（确保与保存时一致）
model = models.resnet18(num_classes=102)  # 假设任务有 102 个类别
model = model.to(device)
MODEL_PATH = os.path.join(os.path.dirname(__file__),'102flowers_model.pth')
# 加载权重
checkpoint = torch.load(MODEL_PATH, map_location=device,weights_only=True)
model.load_state_dict(checkpoint['model_state_dict'])
model.eval()  # 设置为评估模式

# 定义图像预处理
data_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# 预测函数
def predict(image_path, model=model, transform=data_transforms, device=device):
    model.eval()
    with torch.no_grad():
        # 加载图像并预处理
        image = Image.open(image_path).convert('RGB')
        image = transform(image).unsqueeze(0).to(device)  # 添加批次维度并移动到设备
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        return predicted.item()

# 使用模型进行预测