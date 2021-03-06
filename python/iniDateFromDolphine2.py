#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8

#从网络中的每个社区分别选取一定数量的节点用来训练
#此网络为海豚网


from igraph import *
from numpy import *

karate = Graph.Read_GML("dolphins.gml")
fp=open("dolphinsCon.dat")
fpto1=open("dolphins1.scale","w") #训练数据
fpto2=open("dolphins2.scale","w") #测试数据

lineTexts=fp.readlines()
numberOfLines=len(lineTexts)
community=zeros(numberOfLines)
index=0
##社区数为k
k=2

communityElemNum=zeros(k)  #每个社区所含有的样本数


for line in lineTexts:
	listFromLine=line.strip().split(' ')
	community[index]=listFromLine[1]
	communityElemNum[community[index]-1]+=1
	index+=1
degree=zeros(62)
index=0
for deg in karate.degree():
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
	i=karate.vs.find(_degree = degree[numberOfLines-1-maxDegree]).index
	if sign[community[i]-1]==0:
		maxCommunityPoint[community[i]-1]=i
		sign[community[i]-1]=1
for go in range(61,-1,-1):
	if communityElemNum[community[go]-1]!=0:
		fpto1.write('+'+str(int(community[go]))+' ')
		for j in range(0,k):
			fpto1.write(str(j+1)+":"+str(float(1)/(karate.shortest_paths(go,int(maxCommunityPoint[j]))[0][0]+1))+' ')
		fpto1.write('\n')
		communityElemNum[community[go]-1]-=1
	else:
		fpto2.write('+'+str(int(community[go]))+' ')
		for j in range(0,k):
			fpto2.write(str(j+1)+":"+str(float(1)/(karate.shortest_paths(go,int(maxCommunityPoint[j]))[0][0]+1))+' ')
		fpto2.write('\n')



