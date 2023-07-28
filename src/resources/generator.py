# Extends the BaseResource class to provide a generator resource

import numpy as np

from src.resources.base_resource import BaseResource


class Generator(BaseResource):
    def __init__(self,
                 name: str,
                 value: np.array,
                 lower_bound: np.array,
                 upper_bound: np.array,
                 cost: np.array,
                 cost_nde: np.array,
                 is_renewable: np.array):
        super().__init__(name, value, lower_bound, upper_bound, cost)

        self.is_renewable = is_renewable
        self.is_active = np.zeros(self.value.shape)

        self.gen_nde = np.zeros(self.value.shape)
        self.cost_nde = cost_nde
