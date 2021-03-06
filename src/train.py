import numpy as np
import torch 
from data_loader import DatasetCreate
from torch.utils.data import DataLoader
from modelClass import Model
import torch.optim as opt
data = DatasetCreate()
train_data = DataLoader(data,   batch_size=8, shuffle=True , sampler=None, num_workers = 4)


# """ model """
model = Model()
    



# """ optimizer """
optimizer = opt.Adam(model.parameters(), lr=.07)

# """ loss function """
loss_fun = torch.nn.CrossEntropyLoss(size_average=True)

for i in range(2):
    for batch_no, batch_data in enumerate(train_data):
        print("batch_no = ", batch_no)
        input, labels = batch_data
        train_x = torch.tensor(input, requires_grad=False, dtype = torch.float)
        train_y = torch.tensor(labels, requires_grad=False, dtype = torch.long)
        model.zero_grad() 
        out = model(train_x)
        print(out)
        i, pred =  out.max(1)
        print("predic = ", pred)
        print("out = ", train_y.view(-1,))
        loss = loss_fun(out, train_y.view(-1,))
        print(loss.item())
        loss.backward()
        for param in model.parameters():
            print("parameter grad sum = ", param.grad.data.sum())
        optimizer.step()

torch.save(model, 'model/model.pt')