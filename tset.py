map='''
1 2 100 FLAG{          #
2 3 87 AFQWE
2 4 57 ETKLS
2 5 50 WEIVK            #
2 6 51 AWEIW
3 7 94 QIECJF
3 8 78 QSXKE
3 9 85 QWEIH
4 13 54 WQOJF
4 14 47 KDNVE
4 15 98 QISNV
5 10 43 AEWJV
5 11 32 QWKXF
5 12 44 ASJVL            #
6 16 59 ASJXJ
6 17 92 QJXNV
6 18 39 SCJJF
6 23 99 SJVHF
7 19 99 WJCNF
8 20 96 SKCNG
9 20 86 SJXHF
10 21 60 SJJCH
11 21 57 SJHGG
12 22 47 SJCHF           #
14 10 55 EJFHG
16 17 59 ASJVH
18 12 53 SJFHG
18 24 93 SHFVG
21 22 33 SJFHB
19 25 88 ASHHF
20 25 96 SJVHG
22 25 23 SJVHJ         #
25 26 75 SDEV}        #
'''
mapinit=[i for i in map.split('\n') if i !='']
def fun():
    pass

node_list=[]
mas=[i.split() for i in mapinit]
for i in mas:
    node_list.append((i[0],i[1],int(i[2])))
# print(node_list)
# mas=[list(map(fun,list(i.split()))) for i in mapinit]
# print(mas)
# -*-coding:utf-8 -*-
class DijkstraExtendPath():
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        self.used_node_list = []
        self.collected_node_dict = {}
    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        self.collected_node_dict[self.from_node] = [0, -1]
        for index1, node1 in list(enumerate(self.node_map[self.from_node])):
            if node1:
                self.collected_node_dict[index1] = [node1, self.from_node]
        self._foreach_dijkstra()
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_length - 1:
            return
        for key, val in list(self.collected_node_dict.items()):  # 遍历已有权值节点
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
            for index1, node1 in list(enumerate(self.node_map[key])):  # 对节点进行遍历
                # 如果节点在权值节点中并且权值大于新权值
                if node1 and index1 in self.collected_node_dict and self.collected_node_dict[index1][0] > node1 + val[0]:
                    self.collected_node_dict[index1][0] = node1 + val[0] # 更新权值
                    self.collected_node_dict[index1][1] = key
                elif node1 and index1 not in self.collected_node_dict:
                    self.collected_node_dict[index1] = [node1 + val[0], key]
        self._foreach_dijkstra()
    def _format_path(self):
        node_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        node_list.reverse()
        return node_list
def set_node_map(node_map, node, node_list):
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] =  val
if __name__ == "__main__":
    # node = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # node_list = [('A', 'F', 9), ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
    #              ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
    #              ('E', 'D', 7)]
    node=[str(i) for i in range(1,27)]
    # node_list=[i for map]
    node_map = [[0 for val in range(len(node))] for val in range(len(node))]
    set_node_map(node_map, node, node_list)
    # A -->; D
    from_node = node.index('1')
    to_node = node.index('26')
    dijkstrapath = DijkstraExtendPath(node_map)
    path = dijkstrapath(from_node, to_node)
    print (path)
#     x=[j[0]+1 for j in path]

#     t=0
#     # for i in range(len(x)):
#     #     print()
