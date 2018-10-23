'''
Conway's game of Life. 
- The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970
- The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, 
  (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally 
  adjacent. At each step in time, the following transitions occur:

    Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by overpopulation.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

- The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births 
  and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. 
  The rules continue to be applied repeatedly to create further generations. 

Script developed by Diego Alonso San Alberto under GNU/GPL License
'''

import pygame as pg
import numpy  as np
import time
import sys
import cgol_config as cfg


# #-- Classes --
# class ConwayLifeGame:
#     #Create the board and with the cells
#     def __init__(self, board):
#         self.boardMap=[]    #Control array for the map
#         self.totalCells=0
#         # Create the window (width, height)
#         #self.board = pg.display.set_mode((cfg.surface_sz, cfg.surface_sz))
#         self.board= board

#         #Create a tile board to be used in the board
#         tile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
        
#         #Draw the ful board
#         for row in range(cfg.N):
#             mapRow=[]
#             for col in range(cfg.N):
#                 #set the content of the tile (0= empty/white tile 1= cell in tile/black tile)
#                 tileValue= np.random.randint(0,2)
#                 if tileValue == 1:  self.totalCells+=1
#                 tile.fill(cfg.colors[tileValue])
#                 self.board.blit(tile, (col*cfg.tile_sz, row*cfg.tile_sz)) 
#                 mapRow.append(tileValue)    #Add a 0 in the x position of the current tile  
#             self.boardMap.append(mapRow)
        
#         print('total cells: %s'%self.totalCells)

#     def print_boardMap(self):
#         print('boardMap values')
#         for row in range(cfg.N-1):
#             print(self.boardMap[row])


#     def check_health(self, x, y):
#         totalNeighbors=0
#         for i in range(x-1, x+1):
#             if i >= 0 and i < (len(self.boardMap)):
#                 for j in range(y-1, y+1):
#                     if j >= 0 and j < (len(self.boardMap)):
#                         if i!=x and j!=y:
#                             #We must count the surronding neighborgs only (not the cell in (x,y) itself)
#                             if self.boardMap[i][j] == 1:
#                                 totalNeighbors+=1
#         return totalNeighbors

#     def new_generation(self):
#         #black and white tiles to use in the board
#         blackTile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
#         blackTile.fill(cfg.colors[1])
#         whiteTile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
#         whiteTile.fill(cfg.colors[0])        

#         for i in range(len(self.boardMap)-1):
#             for j in range(len(self.boardMap)-1):
#                 neighbors= self.check_health(i,j)
            
#                 if ((self.boardMap[i][j] == 0) and neighbors == 3):
#                     #if there are exactly 3 neighbors next to a empty tile, a new cell appear by reproduction 
                        
#                     print ('self.boardMap[i][j] == 0 and neighbors == 3 -- self.boardMap[i][j]: %s'%self.boardMap[i][j])
                        
#                     #Update the color in the tile where the cell was
#                     self.board.blit(blackTile, (i*cfg.tile_sz, j*cfg.tile_sz))    
#                     self.boardMap[i][j]=1

#                 elif ((self.boardMap[i][j] == 1) and (neighbors<2 or neighbors>3)):
#                     #if less than 2 neighbors (=underpopulation) or more than 3 neighbors(overpopulation), the cell dies                        
                        
#                     #print ('self.boardMap[i][j] == 1 and (neighbors<2 or neighbors>3 -- self.boardMap[i][j]: %s'%self.boardMap[i][j])
                        
#                     #Update the color in the tile where the cell was
#                     self.board.blit(whiteTile, (i*cfg.tile_sz, j*cfg.tile_sz))
                        
#                     self.boardMap[i][j]=0

#         #update board
#         pg.display.flip()


#Create the board and with the cells
def ConwayLifeGame (board):
    boardMap=[]    #Control array for the map
    totalCells=0
    # Create the window (width, height)
    #self.board = pg.display.set_mode((cfg.surface_sz, cfg.surface_sz))
    board= board

    #Create a tile board to be used in the board
    tile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    
    #Draw the ful board
    for row in range(cfg.N):
        mapRow=[]
        for col in range(cfg.N):
            #set the content of the tile (0= empty/white tile 1= cell in tile/black tile)
            tileValue= np.random.randint(0,2)
            if tileValue == 1:  totalCells+=1
            tile.fill(cfg.colors[tileValue])
            board.blit(tile, (col*cfg.tile_sz, row*cfg.tile_sz)) 
            mapRow.append(tileValue)    #Add a 0 in the x position of the current tile  
        boardMap.append(mapRow)
    
    print('total cells: %s'%totalCells)
    return boardMap, board


#Create the board and with the cells
def ConwayLifeGame_reduced (board):
    boardMap=[]    #Control array for the map
    totalCells=0

    minBoundary= (cfg.N/2)-(cfg.N/6)
    maxBoundary= (cfg.N/2)+(cfg.N/6)
    # Create the window (width, height)
    #self.board = pg.display.set_mode((cfg.surface_sz, cfg.surface_sz))
    board= board

    #Create a tile board to be used in the board
    tile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    
    #Draw the ful board
    for row in range(cfg.N):
        mapRow=[]
        for col in range(cfg.N):
            #set the content of the tile (0= empty/white tile 1= cell in tile/black tile)
            if (row >= minBoundary or row <= maxBoundary) and (col >= minBoundary or col <= maxBoundary):
                tileValue= np.random.randint(0,2)
                if tileValue == 1:  totalCells+=1
            else: 
                tileValue= 0
            tile.fill(cfg.colors[tileValue])
            board.blit(tile, (col*cfg.tile_sz, row*cfg.tile_sz)) 
            mapRow.append(tileValue)    #Add a 0 in the x position of the current tile  
        boardMap.append(mapRow)
    print('total cells: %s'%totalCells)
    return boardMap, board


def print_boardMap(boardMap, text):
    print(text)
    for row in range(cfg.N):
        print(boardMap[row])

def blink_tiles(boardMap, map):
    #black and white tiles to use in the board
    blackTile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    blackTile.fill(cfg.colors[1])
    whiteTile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    whiteTile.fill(cfg.colors[0])    
    
    for i in range(len(boardMap)):
        for j in range(len(boardMap)):
            if boardMap[i][j] == 1:
                boardMap[i][j]= 0
                #Update the color in the tile where the cell was
                board.blit(whiteTile, (i*cfg.tile_sz, j*cfg.tile_sz))  
            else:
                boardMap[i][j]= 1
                #Update the color in the tile where the cell was
                board.blit(blackTile, (i*cfg.tile_sz, j*cfg.tile_sz))  
                #update board
                pg.display.flip()
    return boardMap, board


def check_health(boardMap, x, y):
    totalNeighbors=0
    #print('Looking for neighbors next to point [%s][%s]'%(x,y))

    for i in range(x-1, x+2):
        if i >= 0 and i < (len(boardMap)):
            for j in range(y-1, y+2):
                if j >= 0 and j < (len(boardMap)):
                        if boardMap[i][j] == 1:
                            #print('  - boardMap[%s][%s]:%s '%(i,j,boardMap[i][j]))
                            totalNeighbors+=1
    if boardMap[x][y] == 1:
        #If the current position contained already a cell, erase from the total neighborg count
        totalNeighbors-= 1
    #print('  - total neighbors for boardMap[%s][%s]: %s '%(x,y,totalNeighbors))
    return totalNeighbors

def new_generation(boardMap, board):
    #black and white tiles to use in the board
    blackTile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    blackTile.fill(cfg.colors[1])
    whiteTile= pg.Surface((cfg.tile_sz, cfg.tile_sz))
    whiteTile.fill(cfg.colors[0])

    tempMap=[]
    neighMap=[]        

    for i in range(len(boardMap)):
        neighRow=[]
        tempRow= []
        for j in range(len(boardMap)):
            neighbors= check_health(boardMap,i,j)
            neighRow.append(neighbors)
            if ((boardMap[i][j] == 0) and neighbors == 3):
                #if there are exactly 3 neighbors next to a empty tile, a new cell appear by reproduction 
                                       
                #Update the color in the tile where the cell was
                board.blit(blackTile, (i*cfg.tile_sz, j*cfg.tile_sz))    
                tempRow.append(1)

            elif ((boardMap[i][j] == 1) and (neighbors<2 or neighbors>3)):
                #if less than 2 neighbors (=underpopulation) or more than 3 neighbors(overpopulation), the cell dies                        
                    
                #print ('self.boardMap[i][j] == 1 and (neighbors<2 or neighbors>3 -- self.boardMap[i][j]: %s'%self.boardMap[i][j])
                    
                #Update the color in the tile where the cell was
                board.blit(whiteTile, (i*cfg.tile_sz, j*cfg.tile_sz))
                    
                tempRow.append(0)
            
            else:
                #No changes in for this cell
                tempRow.append(boardMap[i][j]) 

        neighMap.append(neighRow)
        tempMap.append(tempRow)
    #update board
    pg.display.flip()

    #print_boardMap(neighMap, '-- mapa de vecinos -- ')
    #print_boardMap(tempMap, ' -- nueva generacion --')
    return tempMap, board


# Quita el ultimo caracter de una lista.
def erase_last_char(map):
    for i in range(len(map)):
        map[i] = map[i][:-1]
    return map

# Read a map from a file and convert it as a list.
def load_board(file):
    boardMap = open(file, "r")
    boardMap = boardMap.readlines()
    boardMap = erase_last_char(mapa)
    for i in range(len(boardMap)):
        boardMap[i] = listarCadena(mapa[i])
    return boardMap
                  

# #--- MAIN SCRIPT ---
# pg.init()
# # Create the window (width, height)
# board = pg.display.set_mode((cfg.surface_sz, cfg.surface_sz))

# testito= ConwayLifeGame(board)
# i=0
# testito.print_boardMap()
# #time.sleep(10)
# while i<10: 
#     #Look for an event from keyboard, mouse, etc.
#     ev = pg.event.poll()
#     if ev.type == pg.QUIT:
#         break
#     else:
#         testito.new_generation()
#     i+=1

# print('boardMap last situation')
# testito.print_boardMap()


#--- MAIN SCRIPT ---
pg.init()
# Create the window (width, height)
board = pg.display.set_mode((cfg.surface_sz, cfg.surface_sz))

#boardMap, board= ConwayLifeGame(board)
boardMap, board= ConwayLifeGame_reduced(board)
i=0
#print_boardMap(boardMap, 'INIT')
#time.sleep(10)
while i<100000: 
    #Look for an event from keyboard, mouse, etc.
    ev = pg.event.poll()
    if ev.type == pg.QUIT:
        break
    else:
        boardMap, board= new_generation(boardMap, board)
        #boardMap, board= blink_tiles(boardMap, board)
        #print('-- iteration: %s'%i)
        #print_boardMap(boardMap, 'generation in iteration: '+str(i))
        time.sleep(0.1)
    i+=1

#print_boardMap(boardMap, 'boardMap last situation' )