import random 
import plotly.express as px
import plotly.figure_factory as ff
list1 =[]
count =[]
for i in range(0,100) :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    add = dice1+dice2
    list1.append(add)
    count.append(i)
graph = ff.create_distplot([list1],['count'])
graph.show()
print(list1)