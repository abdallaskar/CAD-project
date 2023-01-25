import numpy as np

from data import tie_set_model as tsm


class TieSetOperations:
    tieSetData = tsm.TieSetData

    def __init__(self, tie_set_model):
        self.tieSetData = tie_set_model

    def get_il(self):
        b_zb = np.dot(self.tieSetData.B, self.tieSetData.Zb)
        left_side = np.dot(b_zb, self.tieSetData.Btrans)
        b_eb = np.dot(self.tieSetData.B, self.tieSetData.Eb)
        b_zb_ib = np.dot(b_zb, self.tieSetData.Ib)
        right_side = np.subtract(b_eb, b_zb_ib)
        inverse_left = np.linalg.inv(left_side)
        return np.dot(inverse_left, right_side)

    def get_jb(self):
        il = self.get_il()
        return np.dot(self.tieSetData.Btrans, il)

    def get_vb(self):
        jb = self.get_jb()
        jb_ib = np.add(jb, self.tieSetData.Ib)
        sub_right = np.dot(self.tieSetData.Zb, jb_ib)
        right_side = np.subtract(sub_right, self.tieSetData.Eb)
        return right_side
