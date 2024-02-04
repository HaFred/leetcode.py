import torch
import torch.nn.functional as F

N = 1
C = 3 # n_classses
H = 2
W = 2
dev = torch.device('cpu')
# one weight per class
weights = torch.ones(C, device=dev)

pred = torch.randn(N, C, H, W, device=dev).uniform_(0, 1)
print("input pred: \n", pred)

# label must stay in [0, C-1]
label = torch.zeros(N, H, W, device=dev).long()
label[0][0][0] = 0
label[0][0][1] = 1
label[0][1][0] = 1
label[0][1][1] = 2
print("target label: \n", label)
loss = F.cross_entropy(input=pred, target=label, weight=weights, reduction="none")
print("round-0: cross_entropy: \n", loss)

softmax = torch.nn.LogSoftmax(dim=1)
nllloss = torch.nn.NLLLoss(weight=weights, reduction="none")
pred_softmax = softmax(pred)
# print("pred_LogSoftmax: \n", pred_softmax)
loss = nllloss(pred_softmax, label)
print("round-1: cross_entropy: \n", loss)


"""implementing softmax`"""
pred_exp = torch.exp(pred)
pred_sum = torch.sum(pred_exp, dim=(1), keepdim=False)
pred_div = torch.div(pred_exp, pred_sum)
pred_log = torch.log(pred_div)
# print("pred_log: \n", pred_log)

loss = torch.zeros(N, H, W, device=dev)
for dim0 in range(N):
    for dim1 in range(H):
        for dim2 in range(W):
            cls = label[dim0][dim1][dim2]
            loss[dim0][dim1][dim2] = -1 * weights[cls] * pred_log[dim0][cls][dim1][dim2]
print("round-2: cross_entropy: \n", loss)
