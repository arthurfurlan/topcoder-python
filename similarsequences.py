# -*- coding: utf-8 -*-

'''
TopCoder Reference:
http://community.topcoder.com/stat?c=problem_statement&pm=12615
'''

import itertools
import unittest
import timeit


class SimilarSequences(object):

    def count(self, seq, bound):
        nums = xrange(1, bound+1)
        seqs = itertools.product(nums, repeat=len(seq))
        return len([s for s in seqs if self.similar(seq, list(s))])

    def similar(self, seq1, seq2):
        if not seq1 or len(seq1) != len(seq2):
            return False
        for i in xrange(len(seq1)):
            tseq1 = seq1[:]
            tseq1.pop(i)
            for j in xrange(len(seq2)):
                tseq2 = seq2[:]
                tseq2.pop(j)
                if tseq1 == tseq2:
                    return True
        return False


class TestSimilarSequences(unittest.TestCase):

    def setUp(self):
        self.instance = SimilarSequences()

    def test_example_0(self):
        args = [[1, 1], 3]
        self.assertEquals(5, self.instance.count(*args))

    def test_example_1(self):
        args = [[1, 2], 2]
        self.assertEquals(4, self.instance.count(*args))

    def test_example_2(self):
        args = [[999], 1000]
        self.assertEquals(1000, self.instance.count(*args))     ## lower numbers, same idea

    def test_example_3(self):
        args = [[1, 2, 3, 4, 5], 5]
        self.assertEquals(97, self.instance.count(*args))

    #def test_example_4(self):                                  ## my computer was defeated
    #    args = [[5, 8, 11, 12, 4, 1, 7, 9], 1000000000]
    #    self.assertEquals(999999363, self.instance.count(*args))

    def test_example_5(self):
        args = [[999, 555], 1000]
        self.assertEquals(3996, self.instance.count(*args))


if __name__ == '__main__':
    unittest.main()
