list=[1,3,1,3,4,5]
newlist=[]
[newlist.append(x) for x in list if x not in newlist]
