from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .base_trainer import BaseTrainer

class ConvGNNTrainer(BaseTrainer):
    def __init__(self, opt, model, optimizer=None):
        super(ConvGNNTrainer, self).__init__(opt, model, optimizer=optimizer)