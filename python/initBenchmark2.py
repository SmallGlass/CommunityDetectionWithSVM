#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8

#从网络中的每个社区分别选取一定数量的节点用来训练
#此网络为人工生成的网络


from igraph import *
from numpy import *

benchmark = Graph.Read_Edgelist("benchmark_2_2/network0.4.dat") #读的时候是从0开始找节点的，所以后期要处理的
fp=open("benchmark_2_2/community0.4.dat")
fpto1=open("benchmark0_1_1.scale","w") #训练数据
fpto2=open("benchmark0_1_2.scale","w") #测试数据

lineTexts=fp.readlines()
numberOfLines=len(lineTexts)
community=zeros(numberOfLines)
index=0
##社区数为k  ####此处需要修改
k=4

communityElemNum=zeros(k)  #每个社区所含有的样本数


for line in lineTexts:
	listFromLine=line.strip().split('	')
	community[index]=listFromLine[1]
	communityElemNum[community[index]-1]+=1
	index+=1
nodes=200#节点数    ####此处需要修改
degree=zeros(nodes)
index=0
canWrite=0
for deg in benchmark.degree():
	if canWrite==0:
		canWrite=1
		continue
	degree[index]=deg
	index+=1
degree.sort()

for i in range(0,k):
	communityElemNum[i]=int(communityElemNum[i]*2/3)
#此社区是否找过了
sign=zeros(k)
#每个社区最大度的点
maxCommunityPoint=zeros(k)
#找到每个社区的最大度的点
for maxDegree in range(0,numberOfLines):
	i=benchmark.vs.find(_degree = degree[numberOfLines-1-maxDegree]).index
	if sign[community[i-1]-1]==0:
		maxCommunityPoint[community[i-1]-1]=i
		sign[community[i-1]-1]=1
for go in range(0,nodes):
	if communityElemNum[community[go]-1]!=0:
		fpto1.write('+'+str(int(community[go]))+' ')
		for j in range(0,k):
			fpto1.write(str(j+1)+":"+str(float(1)/(benchmark.shortest_paths(go+1,int(maxCommunityPoint[j]))[0][0]+1))+' ')
		fpto1.write('\n')
		communityElemNum[community[go]-1]-=1
	else:
		fpto2.write('+'+str(int(community[go]))+' ')
		for j in range(0,k):
			fpto2.write(str(j+1)+":"+str(float(1)/(benchmark.shortest_paths(go+1,int(maxCommunityPoint[j]))[0][0]+1))+' ')
		fpto2.write('\n')



