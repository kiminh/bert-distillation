from catalyst.contrib.dl.callbacks.wandb import WandbLogger
from catalyst.dl import registry
from torch.nn import CosineEmbeddingLoss
from torch_optimizer import Ranger

from .callbacks import CosineLossCallback
from .experiment import Experiment  # noqa: F401
from .models import BertForMLM, DistilbertStudentModel
from .runners import DistilMLMRunner as Runner  # noqa: F401

registry.Model(BertForMLM)
registry.Model(DistilbertStudentModel)

registry.Optimizer(Ranger)

registry.Callback(WandbLogger)

registry.Criterion(CosineEmbeddingLoss)

registry.Callback(CosineLossCallback)
