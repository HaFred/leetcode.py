import torch
import torch.nn.functional as F

input = torch.randn(3, 2, requires_grad=False)  # N C
# target_class = torch.randint(2, (3,), requires_grad=False)  # N, required by the cross entropy function
target = torch.randn(3, 2).softmax(1)  # class prob
target_class = target.max(1)[1]

# sinput = torch.sigmoid(input)
# loss = F.binary_cross_entropy(sinput, target)

# input = torch.randn(3, 5, requires_grad=True)
# target = torch.randn(3, 5).softmax(dim=1)

loss = F.cross_entropy(input, target_class, reduction='none')  # with reduction just takes mean
print('with reduction, torch loss is {}, which is {}'.format(F.cross_entropy(input, target_class), loss))


# target = torch.randint(5, (3,), dtype=torch.int64)

def CE_Loss(target, act):
    """Input is softmax-ed, thus CE is doing softmax+log+NLLLoss for the input logit"""
    # out = torch.sum((-target * torch.log(act) - (1 - target) * torch.log(1 - act)))
    loss = torch.zeros(target.shape)
    for dim_label in range(target.shape[0]):
        cls = target[dim_label]
        loss[dim_label] = - 1 * torch.log(act[dim_label][cls])  # the gt cls index the log(pred) in the cross entropy
    return loss


input_soft = F.softmax(input)
my_loss = CE_Loss(target_class, input_soft)
print('[my func: target as class label] loss is {} from {}'.format(my_loss, torch.mean(my_loss)))

""" Or the target can be passed in as each class prob instead of class label"""


def CE_loss_takes_targetprob(target, soft_input):
    loss = - target * torch.log(soft_input)
    loss_sum = loss.sum(1)
    loss = loss_sum.mean()
    return loss, loss_sum


my_prob_loss, loss_sum = CE_loss_takes_targetprob(target, input_soft)
print('[my func: target as class prob] loss is {} from {}'.format(my_prob_loss, torch.mean(loss_sum)))
# will be the same as following
print('directly with target prob in ce loss: {}'.format(F.cross_entropy(input, target_class)))

""" Output:
with reduction, torch loss is 1.286257028579712, which is tensor([1.2287, 1.3038, 1.3262])
[my func: target as class label] loss is tensor([1.2287, 1.3038, 1.3262]) from 1.2862569093704224
[my func: target as class prob] loss is 1.0002144575119019 from 1.0002144575119019
directly with target prob in ce loss: 1.286257028579712
"""

