#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8

from svmutil import *

#从网络中的每个社区分别选取一定数量的节点用来测试
#此网络为海豚网


yTrain, xTrain = svm_read_problem('benchmark0_1_1.scale')
yTest, xTest = svm_read_problem('benchmark0_1_2.scale')
m = svm_train(yTrain, xTrain, '-c 4')
p_label, p_acc, p_val = svm_predict(yTest, xTest, m)
