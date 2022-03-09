import torch as T
import torch.nn as nn
import torch.nn.functional as F

# original img dim = 3 x 100 x 100

class Conv_test(nn.Module):
   def __init__(self):
   	super(Conv_test, self).__init__()
   	self.conv1 = nn.conv2D(3, 64, 7, 1)
   	self.pool = nn.maxPool2D(3, 2)
   	self.conv2 = nn.conv2D(64, 128, 7, 1)
   	
   	self.fc1 = nn.Linear(40 * 40 * 128, some_num)
   	self.out = nn.Linear(some_num, 10)
   
   def forward(self, x):
	x = F.relu(self.conv1(x))
	x = self.pool(x)
	x = F.relu(self.conv2(x))
	
	x = x.view(x.shape[0], -1)
	
	x = F.relu(self.fc1(x))
	x = self.out(x)
	

epochs = 100

model = Conv_test()
criterion = nn.CrossEntropyLoss()
optim = T.optim.Adam(model.parameters(), lr=3e-5)

for e in epochs:
   
   for imgs, labels in iter(trainloader):
	
	optim.zero_grad()
	
	out = model(imgs)
	
	loss = criterion(out, labels)
	
	loss.backward()
	
	optim.step()
	
   	
   	
   	
   	



