import numpy as np
import math

class aiMap(object):
    
    def __init__(self,rows,cols,rOrig,cOrig):
        self.mapArray = np.zeros((rows,cols),dtype=int)
        self.rOrig = rOrig
        self.cOrig = cOrig
        
    def __str__(self):
        return str(self.mapArray)
        
    def setValue(self,row,col,value):
        r = math.floor(row + self.rOrig)
        c = math.floor(col + self.cOrig)
        
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
        
    def expandMap(self,rU, rD, cL, cR):
        tmpMap = self.mapArray
        
        #Add above
        r,c = np.shape(tmpMap)
        tmp = np.zeros((rU,c),dtype=int)
        tmpMap = np.vstack((tmp,tmpMap))
        self.rOrig += rU
        
        #Add below
        r,c = np.shape(tmpMap)
        tmp = np.zeros((rD,c),dtype=int)
        tmpMap = np.vstack((tmpMap,tmp))
        
        #Add to Left side
        r,c = np.shape(tmpMap)
        tmp = np.zeros((r,cL),dtype=int)
        tmpMap = np.hstack((tmp,tmpMap))
        self.cOrig += cL
        
        #Add to Right side
        r,c = np.shape(tmpMap)
        tmp = np.zeros((r,cR),dtype=int)
        tmpMap = np.hstack((tmpMap,tmp))
        
        self.mapArray = tmpMap
        
    def mapWithMarker(self,row,col,marker):
        r = math.floor(row + self.rOrig)
        c = math.floor(col + self.cOrig)
        
        tmp = np.copy(self.mapArray)
        tmp[r][c] = marker
        
        return tmp
        
