def bfs(graph,start):
    visited=[start]
    vist_check=set([start])
    queue=[start]
    while(len(queue)):
        ele=queue.pop(0)
        
        for i in graph[ele]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                vist_check.add(i)
    print(*visited)
def dfs(graph, start, visited = None):
    if visited == None:
        visited = []
    visited.append(start)
    print(start,end=" ")
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs(graph, i, visited)

            
    #20 10 40 50 30
grap={
    10:[20,40,50],
    20:[10,40],
    30:[40,50],
    40:[10,20,30,50],
    50:[10,30,40]
}
bfs(grap,20)
dfs(grap,20)