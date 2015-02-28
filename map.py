import numpy as np
import math

class map(object):
    
    def __init__(self,rows,cols,rOrig,cOrig):
        self.mapArray = np.zeros((rows,cols),dtype=int)
        self.rOrig = rOrig
        self.cOrig = cOrig
    def __str__(self):
        return str(self.mapArray)
        
    def setValue(self,row,col,value):
        r = math.floor(row + self.rOrig)
        c = math.floor(col + self.cOrig)
        
        
        
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
        
    
    
