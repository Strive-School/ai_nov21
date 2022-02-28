import torch as T
import torch.nn as nn
import torch.nn.functional as F

# original 75 x 75 x 3

class ConvClf(nn.Module):

    def __init__(self):
        super(ConvClf, self).__init__()

        self.conv1 = nn.Conv2d(3, 16, 3, 2, 1) # (75 - 3 + 2*1)//2 + 1 = 74//2 + 1 = 37 + 1 = 38
        self.pool1 = nn.MaxPool2d(3, 2) # (38 - 3 +2*0)//2 + 1 = 35//2 + 1 = 17 +1 = 18
        self.conv2 = nn.Conv2d(16, 32, 5, 2, 2) # (18 - 5 + 2*2)//2 + 1 = 17//2 + 1 = 8 + 1 = 9
        self.pool2 = nn.MaxPool2d(5, 2) # (9 - 5)//2 + 1 = 3
        self.conv3 = nn.Conv2d(32, 64, 3, 1, 1) # (3 - 3 + 2*2)//2 + 1 = 3

        # to calculate input feat.
        # I use the foolowing formula:
        # (S - K + 2P) / str + 1

        # final img dim after the conv is 3 x 3 x 64

        self.fc1 = nn.Linear(3 * 3 * 64, 256)
        self.fc2 = nn.Linear(256, 128)
        self.out = nn.Linear(128, 10)
    
    def forward(self, x):

        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = F.relu(self.conv3(x))

        x = x.view(3 * 3 * 64,)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.out(x)

fake_img = T.rand((1, 3, 75 ,75))

model = ConvClf()

logits = model.forward(fake_img)

probs = F.softmax(logits)

pred = T.argmax(probs)

print(pred)
       


