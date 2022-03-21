import sys
class Point:
    def __init__(self,street,number,code, vertex, weight=0):
        self.street=street
        self.number=number
        self.code=code
        self.vertex=vertex
        self.weight=weight
    
class Map():
    def __init__(self,directed=True):
        self.vertices={}
        self.directed=directed
    
    def addPoint(self,point):
        self.vertices[point.vertex]=[point]
    
    def addConection(self, a, b, weight=0):
        start=a.vertex
        end=b.vertex
        if start not in self.vertices:
            print(start,' Does not exist!')
            return
        if end not in self.vertices:
            print(end,' Does not exist!')
            return
        self.vertices[start].append(Point(b.street, b.number,b.code, b.vertex, weight))
        if self.directed==False:
            self.vertices[end].append(Point(a.street, a.number,a.code, a.vertex, weight))

    def areConected(self, a, b):
        start=a.vertex
        end=b.vertex
        if start not in self.vertices:
            print(start,' Does not exist!')
        if end not in self.vertices:
            print(end,' Does not exist!')
        for adj in self.vertices[start]:
            if adj.vertex==end:
                if adj.weight!=0:                  
                    return "Distance between "+str(a.vertex)+ " and "+str(b.vertex)+": "+str(adj.weight)
                else:                  
                    return "Distance: "+str(0)
        return str(-1)+" they are not connected"

    def removeConection(self,a,b):
        start=a.vertex
        end=b.vertex
        if start not in self.vertices:
            print(start,' Does not exist!')
            return
        if end not in self.vertices:
            print(end,' Does not exist!')
            return
        for adj in self.vertices[start]:
            if adj.vertex==end:
                self.vertices[start].remove(adj)
        if self.directed==False:
            for adj in self.vertices[end]:
                if adj.vertex==start:
                    self.vertices[end].remove(adj)
  
    def __str__(self):
        result=''
        for v in self.vertices:
            y=self.vertices[v][0]
            result+="Point "+str(y.vertex)+" with direction "
            result+=str(y.street)+" "+str(y.number)+" "+str(y.code)+" has connection with points:"+"\n"
            for x in self.vertices[v][1:]:
                result+=str(x.vertex)+" with distance: "+str(x.weight)+", "
            result+="\n"
        return result

    
    def generateRoute(self): 
        visited={}
        for v in self.vertices.keys():
            visited[v]=False
        route=[]
        for v in  self.vertices.keys():
            if visited[v]==False:
              self._dfs(v, visited, route)
        return route

    def _dfs(self, v, visited, lista): 
        visited[v] = True
        lista.append(v)
        for adj in self.vertices[v]: 
            if visited[adj.vertex] == False: 
                self._dfs(adj.vertex, visited, lista)
    
    def minDistance(self, distances, visited): 
        min = sys.maxsize 

        for vertex in self.vertices.keys(): 
            if distances[vertex] <= min and visited[vertex] == False: 
                min = distances[vertex]
                min_vertex = vertex      
    
        return min_vertex

    def minRoute(self, a, b): 
        origin=a.vertex
        end=b.vertex
        visited={}
        for v in self.vertices.keys():
            visited[v]=False
        #previous will save the previous vertex fot the key
        previous={}
        for v in self.vertices.keys():
            previous[v]=None
        #distances will save accumulative distance from a to vertex(key)    
        distances={}
        for v in self.vertices.keys():
            distances[v]=sys.maxsize

        distances[origin] = 0
        
        for n in range(len(self.vertices)): 
            u = self.minDistance(distances, visited) 
            visited[u] = True
            for adj in self.vertices[u]: 
                i=adj.vertex
                w=adj.weight
                if visited[i]==False and distances[i]>distances[u]+w:
                    distances[i]=distances[u]+w   
                    previous[i]=u       
        minpath=self.getPath(distances,previous,origin,end)
        return minpath and distances[end]
          

    def getPath(self,distances,previous,origin, end): 
        if distances[end]==sys.maxsize:
            print("There is not path from ",origin,' to ',end)
        else: 
            minimum_path=[]
            prev=previous[end]
            while prev!=None:
                minimum_path.insert(0,prev)
                prev=previous[prev]
            minimum_path.append(end)  
        return minimum_path


def test():
    a=Point("street1","14","2221", "A")
    b=Point("street2","34","2222", "B")
    c=Point("street3","65","2223", "C")
    d=Point("street4","13","2224", "D")
    e=Point("street5","27","2225", "E")
    f=Point("street6","33","2226", "F")
    g=Map(False)
    
    #Add points
    g.addPoint(a)
    g.addPoint(b)
    g.addPoint(c)
    g.addPoint(d)
    g.addPoint(e)
    g.addPoint(f)
    
    #Add connections
    g.addConection(a,b,7) 
    g.addConection(a,c,9) 
    g.addConection(a,f,14) 
    g.addConection(b,c,10) 
    g.addConection(b,d,15) 
    g.addConection(c,d,11)  
    g.addConection(c,f,2)
    g.addConection(d,e,13)
    g.addConection(e,f,9)
    
    #Check connections
    print(g.areConected(a,b))
    print(g.areConected(a,d))
    print(g.areConected(c,f))
    print(g.areConected(d,e))
    print(g.areConected(b,e))
    
    #Show connections
    print(g.__str__())
    
    #Create route
    x=g.generateRoute()
    
    #Create minimum path
    y=g.minRoute(a,e)
    
    #Remove connections
    g.removeConection(a, b)
    g.removeConection(c, d)
    g.removeConection(f, e)
    print(g.__str__())

test()
