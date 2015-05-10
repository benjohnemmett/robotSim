import numpy as np
import math

class statMap(object):
    
    def __init__(self,rows,cols,rOrig,cOrig):
        self.mapArray = np.zeros((rows,cols))
        self.rOrig = rOrig
        self.cOrig = cOrig
        
    def __str__(self):
        return str(self.mapArray)
        
    def setValue(self,row,col,value):
        r = round(row + self.rOrig)
        c = round(col + self.cOrig)
        
        mapRows, mapCols = np.shape(self.mapArray)
        #print "r = " + str(r) + ", c = " + str(c)
        #print "mapRows = " + str(mapRows) + ", mapCols = " + str(mapCols)
        # Expand map if necessary
        if(r < 0):
            #print "r < 0"
            self.expandMap(-r,0,0,0)
        if(r >= mapRows):
            #print "r >= mapRows"
            self.expandMap(0,(r-mapRows + 1),0,0)
        if(c < 0):
            #print "c < 0"
            self.expandMap(0,0,-c,0)
        if(c >= mapCols):
            #print "c >= mapCols"
            self.expandMap(0,0,0,(c-mapCols + 1))            
        
        self.mapArray[r][c] = value
        
    def bumpUp(self,row,col,val=0.5):
        r = round(row + self.rOrig)
        c = round(col + self.cOrig)
        
        mapRows, mapCols = np.shape(self.mapArray)
        
        # Expand map if necessary
        if(r < 0):
            #print "r < 0"
            self.expandMap(-r,0,0,0)
        if(r >= mapRows):
            #print "r >= mapRows"
            self.expandMap(0,(r-mapRows + 1),0,0)
        if(c < 0):
            #print "c < 0"
            self.expandMap(0,0,-c,0)
        if(c >= mapCols):
            #print "c >= mapCols"
            self.expandMap(0,0,0,(c-mapCols + 1))          
        
        prior = self.mapArray[r][c]    
        
        self.mapArray[r][c] = val + (1-val)*prior

    def knockDown(self,row,col,val=0.9):
        r = round(row + self.rOrig)
        c = round(col + self.cOrig)
        
        mapRows, mapCols = np.shape(self.mapArray)
        
        # Expand map if necessary
        if(r < 0):
            #print "r < 0"
            self.expandMap(-r,0,0,0)
        if(r >= mapRows):
            #print "r >= mapRows"
            self.expandMap(0,(r-mapRows + 1),0,0)
        if(c < 0):
            #print "c < 0"
            self.expandMap(0,0,-c,0)
        if(c >= mapCols):
            #print "c >= mapCols"
            self.expandMap(0,0,0,(c-mapCols + 1))          
        
        prior = self.mapArray[r][c]    
        
        self.mapArray[r][c] = val*prior
                     
        
        
    def expandMap(self,rU, rD, cL, cR):
        tmpMap = self.mapArray
        
        #Add above
        r,c = np.shape(tmpMap)
        tmp = np.zeros((rU,c))
        tmpMap = np.vstack((tmp,tmpMap))
        self.rOrig += rU
        
        #Add below
        r,c = np.shape(tmpMap)
        tmp = np.zeros((rD,c))
        tmpMap = np.vstack((tmpMap,tmp))
        
        #Add to Left side
        r,c = np.shape(tmpMap)
        tmp = np.zeros((r,cL))
        tmpMap = np.hstack((tmp,tmpMap))
        self.cOrig += cL
        
        #Add to Right side
        r,c = np.shape(tmpMap)
        tmp = np.zeros((r,cR))
        tmpMap = np.hstack((tmpMap,tmp))
        
        self.mapArray = tmpMap
        
    def mapWithMarker(self,row,col,marker):
        r = round(row + self.rOrig)
        c = round(col + self.cOrig)
        
        tmp = np.copy(self.mapArray) + 0.5
        tmp = tmp.astype(int)
        tmp[r][c] = marker
        
        return tmp
        
    def gradientMapToGoal(self,row,col):
        # Returns a 2d array the same size as the current map. Each array element contains the navigable distance to the goal from that point.
        navThresh = 0.5
        d = [[0,1],[-1,0],[0,-1],[1,0]]        
        
        r = round(row + self.rOrig) #Convert to array indecies
        c = round(col + self.cOrig)
        
        grad = np.zeros_like(self.mapArray,dtype=np.int)
        mapRows, mapCols = np.shape(grad)
        
        openList = [(r,c)]
        
        while (len(openList) > 0):
            maxCost = 999
            r0,c0 = openList.pop(0)
            cost = grad[r0][c0]
            
            for i in range(len(d)):
                rt = r0 + d[i][0]
                ct = c0 + d[i][1]
                
                if((rt >= 0) & (rt <= (mapRows-1)) & (ct >= 0) & (ct <= (mapCols-1))): #On the map
                    if(grad[rt][ct] == 0) & ((rt != r) | (ct != c)): #Not set yet
                        if(self.mapArray[rt][ct] < navThresh): # Navigable
                            grad[rt][ct] = cost + 1
                            openList.append((rt,ct))
                        else:
                            grad[rt][ct] = maxCost # Max cost means that this space is not navigable
        return grad
    
    def planRouteToGoal(self,startY, startX, endY, endX):
        sr = round(startY + self.rOrig) #Convert to array indecies
        sc = round(startX + self.cOrig)
        er = round(endY + self.rOrig)
        ec = round(endX + self.cOrig)
        
        ###########################
        ### !!!! This appears to have a bug where it does not completely fill in the map, leaving some areas zeros where it should not be
        ############################
        grad = self.gradientMapToGoal(endY, endX)
        
        #Create a list of waypoints leading to the goal
        dList = [[0,1],[0,-1],[1,0],[-1,0]]
        
        waypoints = []
        
        cr = sr
        cc = sc
        while((cr != er) or (cc != ec)):
            cost = 999
            
            #Find lowest cost next move. 
            for i in range(len(dList)):
                dr = dList[i][0]
                dc = dList[i][1]
                if(grad[cr+dr][cc+dc] < cost):
                   nextRow = cr + dr
                   nextCol = cc + dc
                   cost = grad[cr+dr][cc+dc]
            waypoints.append((round(nextRow - self.rOrig), round(nextCol - self.cOrig))) # This coordinate transform is not correct going from map back to robot coordinates
            cr = nextRow
            cc = nextCol
            
        #waypoints.append((endY,endX))
        return waypoints
                    
            
            
                
                
            
        
        
        
        
        
            
            
        
        
        
