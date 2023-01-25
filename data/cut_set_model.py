import numpy as np


class CutSetData:
    def __init__(self, c, yb, eb, ib):
        self.C = np.array(c)
        self.Yb = np.array(yb)
        self.Eb = np.array(eb)
        self.Ib = np.array(ib)
        self.Ctrans = np.transpose(self.C)
