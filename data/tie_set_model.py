import numpy as np


class TieSetData:
    def __init__(self, b, zb, eb, ib):
        self.B = np.array(b)
        self.Zb = np.array(zb)
        self.Eb = np.array(eb)
        self.Ib = np.array(ib)
        self.Btrans = np.transpose(self.B)
