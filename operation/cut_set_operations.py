import numpy as np

from data import cut_set_model as csm


class CutSetOperations:
    cutSetData = csm.CutSetData

    def __init__(self, cut_set_model):
        self.cutSetData = cut_set_model

    def get_en(self):
        c_yb = np.dot(self.cutSetData.C, self.cutSetData.Yb)
        left_side = np.dot(c_yb, self.cutSetData.Ctrans)
        yb_eb = np.dot(self.cutSetData.Yb, self.cutSetData.Eb)
        sub_right = np.subtract(self.cutSetData.Ib, yb_eb)
        right_side = np.dot(self.cutSetData.C, sub_right)
        inv_left = np.linalg.inv(left_side)
        return np.dot(inv_left, right_side)

    def get_vb(self):
        return np.dot(self.cutSetData.Ctrans, self.get_en())

    def get_jb(self):
        yb_vb = np.dot(self.cutSetData.Yb, self.get_vb())
        yb_eb = np.dot(self.cutSetData.Yb, self.cutSetData.Eb)
        sub_right = np.add(yb_vb, yb_eb)
        return np.subtract(sub_right, self.cutSetData.Ib)
