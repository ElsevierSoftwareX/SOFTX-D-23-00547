# Base class for metaheuristics

class MetaheuristicBase(object):

    def __init__(self, n_iter: int, iter_tolerance: int, epsilon_tolerance: float,
                 pop_size: int, pop_dim: int):
        self.n_iter = n_iter
        self.iter_tolerance = iter_tolerance
        self.epsilon_tolerance = epsilon_tolerance
        self.pop_size = pop_size
        self.pop_dim = pop_dim

    def execute(self):
        raise NotImplementedError

    def obj_fn(self):
        raise NotImplementedError

    def pop_fix(self):
        raise NotImplementedError
