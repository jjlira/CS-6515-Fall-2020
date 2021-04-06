# -*- coding: utf-8 -*-
#argparse allows the parsing of command line arguments
import argparse
#utility functions for cs 6515 projects
import GA_ProjectUtils as util


"""
    mst.py       Intro to Graduate Algorithms
    
    Union find object for kruskal algorithm using adjacency matrix
    Also known as a Disjoint-set data structure
    See the text (Dasgupta)
"""
class unionFind:
    def __init__(self, n):
        self.pi = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def areConnected(self, p, q):
        """
            return true if 2 nodes are connected or false if they are
            not by comparing their roots
        """
        #Your Code Goes Here
        return self.find(p) == self.find(q)
        #return None

    def union(self, u, v):
        """
            build union of 2 components
            Be sure to maintain self.rank as needed to
            make sure your algorithm is optimal.
        """
        #Your Code Goes Here (remove pass)
        #pass
        u_root = self.find(u)
        v_root = self.find(v)
        print("root is : " + str(u_root)+ "  and " + str(v_root))
        print("rank  is : " + str(self.rank[u_root])+ "  and " + str(self.rank[v_root]))
        if u_root == v_root:
            return
        if self.rank[u_root] > self.rank[v_root]:
            self.pi[v_root] = u_root
            self.rank[u_root] += self.rank[v_root]
        else:
            self.pi[u_root] = v_root
            self.rank[v_root] +=  self.rank[u_root]
            print(self.rank[u_root] ,self.rank[v_root])

    def find(self, p):
        """
            find the root of the set containing the
            passed vertex p - Must use path compression!
        """
        #Your Code Goes Here
        if self.pi[p] == p:
            return p
        self.pi[p] = self.find(self.pi[p])
        return self.pi[p]

def kruskal(G):
    """
        Kruskal algorithm
        G : graph object
    """
    #Build unionFind Object
    uf = unionFind(G.numVerts)
    #Make MST as a set
    MST = set()    
    #Get list of edges sorted by increasing weight
    sortedEdges = G.sortedEdges()   
    #Go through edges in sorted order smallest, to largest
    print(sortedEdges)
    print(len(sortedEdges))
    for e in sortedEdges:
        # Your Code Goes Here (remove comments if you wish)
        u, v = e
        if uf.areConnected(u,v) is False:
            uf.union(u,v)
        else:
            continue
        #for each edge e you should do :
        #   e is a tuple of vertices; get vertices u and v from edge e
        #   find if u and v are already connected in MST via unionFind object
        #   if they are connected,  ignore this edge and move on to next one
        #   if they are not, connect them and add the edge to the MST via:
        MST.add(util.buildMSTEdge(G,e))   # do not modify this line

    return MST, uf

"""
main
"""
def main():	
    #DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Minimum Spanning Tree Coding Quiz')
    #use this flag, or change the default here to be small.txt, medium.txt or large.txt, to use different graph description files
    parser.add_argument('-g', '--graphFile',  help='File holding graph data in specified format', default='medium.txt', dest='graphDataFileName')
    #use this flag to print the graph and resulting MST
    parser.add_argument('-p', '--print', help='Print the MSTs?', default=False, dest='printMST')

    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-n', '--sName',  help='Student name, used for autograder', default='GT', dest='studentName')	
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')	
    args = parser.parse_args()
    
    #DO NOT MODIFY ANY OF THE FOLLOWING CODE
    #Build graph object
    graph = util.build_MSTBaseGraph(args)
    #you may print the configuration of the graph -- only effective for graphs with up to 10 vertex
    #graph.printMe()

    #Calculate kruskal's alg for MST
    MST_Kruskal, uf = kruskal(graph)
        
    #verify against provided prim's algorithm results
    util.verify_MSTKruskalResults(args, MST_Kruskal, args.printMST)
    
if __name__ == '__main__':
    main()