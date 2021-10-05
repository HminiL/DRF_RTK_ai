import pandas as pd
from django.db import models

# Create your models here.
from dataclasses import dataclass


@dataclass
class DFrameGenerater(object):

    train: object
    test: object
    id: str
    label: str
    dframe: object

    @property
    def dframe(self)-> object: return self._dframe
    @dframe.setter
    def dframe(self, dframe) : self._dframe = pd.read_csv(f'admin/')

    @property
    def train(self) -> object: return self._train
    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test
    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label
    @label.setter
    def label(self, label): self._label = label