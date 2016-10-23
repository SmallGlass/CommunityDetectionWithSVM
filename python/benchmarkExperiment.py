from svmutil import *


testNum=int(1000*2/3)
y, x = svm_read_problem('benchmark0_1_1.scale')
m = svm_train(y[:testNum], x[:testNum], '-c 4')
p_label, p_acc, p_val = svm_predict(y[testNum:], x[testNum:], m)
