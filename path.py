import numpy as np
import heap as hp
import graphics
import math



def desire(A): #a matrix (2d array) of Squares as input
    dests = [] #nodes to visit
    for row in A: #get the list of goal nodes from the map matrix
        for square in row:
            if square.isDestination:
                dests += [square]
    for start in range(len(dests)): #find shortest path from each node to each node            
        prev = [[0 for col in range(len(A[0]))] for row in range(len(A))] #shows what node nodess are visited from
        heap = hp.pHeap() #priority queue of nodes to visit w shortest distance at top
        prevpathdist = [[0 for col in range(len(A[0]))] for row in range(len(A))] #shows min previous distance travelled to get to node
        for goal in range(start+1, len(dests)):
            at = dests[start] 
            heap.push(at, 0)
            mindist = 0
            while(not (heap.isEmpty() or (mindist!=0 and prevpathdist[q.inspect()]>mindist))):
                at = heap.pop(); #visit node at top of heap
                for adj in range(len(at.getAdjacent())): #check adjacent nodes
                    cost = at.cost+at.getAdjacent()[adj].cost
                    if adj % 2 != 0:
                        cost = math.sqrt(2) * cost   
                    minadj = (at.getAdjacent()[adj], cost)
                    if(prevpathdist[minadj[0].x][minadj[0].y]==0 or prevpathdist[at.x][at.y]+minadj[1]<prevpathdist[minadj[0].x][minadj[0].y]):
                        prevpathdist[minadj[0].x][minadj[0].y] = prevpathdist[at.x][at.y]+cost
                        #update dist traveled to get to node
                        prev[minadj[0].x][minadj[0].y]=at #update how got to node
                        heap.push(minadj[0], minadj[1]) #add node and distance to heal
                        if adj==dests[goal]: mindist = prevpathdist[minadj[0].x][minadj[0].y] 
                        #update minimum distance to goal
            c=dests[goal]
            while(c!=dests[start]):
                c=prev[c.x][c.y]
                if(c!=dests[start]):
                    c.color=(0,0,0)



desire(graphics.squarelist)
graphics.main()

