from collections import defaultdict, deque
#ponder about how you planned to mark nodes as explored in the second pass
def kosaraju_scc(graph, transposed_graph, n):
    explored=[False]*(n+1)
    finishing_time=[]

    def dfs_first_pass(node):
        explored[node]=True
        stack_2=deque([node])
        while stack_2:
            vertex=stack_2[-1]
            finished=True
            for neighbour in transposed_graph[vertex]:
                if not explored[neighbour]:
                    finished=False
                    explored[neighbour]=True
                    stack_2.append(neighbour)
            if finished:
                finishing_time.append(stack_2.pop())

    for i in range(1, n+1):
        if not explored[i]:
            dfs_first_pass(i)

    explored=[False]*(n+1)
    scc_sizes=[]

    def dfs_second_pass(node):
        size=1
        explored[node]=True
        stack=deque([node])
        while stack:
            v=stack.pop()
            for neighbour in graph[v]:
                if not explored[neighbour]:
                    explored[neighbour]=True
                    stack.append(neighbour)
                    size+=1
        scc_sizes.append(size)

    while finishing_time:
        k=finishing_time.pop()
        if not explored[k]:
            dfs_second_pass(k)
            

    scc_sizes.sort(reverse=True)
    return scc_sizes[:5] + [0]*(5 - len(scc_sizes))

def parse_graph(file_name):
    graph=defaultdict(list)
    transposed_graph=defaultdict(list)
    with open(file_name, 'r') as file:
        for line in file:
            tail, head=map(int,line.split())
            graph[tail].append(head)
            transposed_graph[head].append(tail)
    
    return graph, transposed_graph


n=875714
graph, transposed_graph=parse_graph("input.txt")
ans=kosaraju_scc(graph, transposed_graph, n)
print(",".join(map(str,ans)))