
'''
A----B---E
|    ///
C----D---F
'''

G = {
    'A':['B','C'],
    'B':['A','E'],
    'C':['A','D'],
    'D':['C','E','F'],
    'E':['B','D'],
    'F':['D']    
}

visited = set()
taskList=[]
time = 0

def DFS(graph,s):  
    visited.add(s)
    global time 
    time = time +1
    print(s, time)
    for adj in graph[s]:
       if adj not in visited:
           DFS(graph,adj)
    
    time = time +1
    print(s, time)
    taskList.append(s)




DFS(G,'A')
print(taskList)