import random
import time
import numpy as np
import sys
import pygame


class GameOfLife:

    def __init__(self):
        pygame.init()

        self.height = 1280
        self.width = 960
        self.size = (self.height, self.width)
        self.screen = pygame.display.set_mode(self.size)

        self.cellHeight = 64
        self.cellWidth = 48

        self.deadCell = 0, 0, 0
        self.aliveCell = 255, 255, 255

        self.grid = self.init_grid()
        self.draw_from_grid(self.grid)

    def init_grid(self):
        return np.random.randint(0, 2, (int(self.height / self.cellHeight), int(self.width / self.cellWidth)))

    def draw_from_grid(self, grid):
        rowIndex = 0
        for row in grid:
            colIndex = 0
            for col in row:
                if col == 0:
                    pygame.draw.rect(self.screen, self.deadCell,
                                     (rowIndex * self.cellHeight, colIndex * self.cellWidth, self.cellHeight,
                                      self.cellWidth))
                else:
                    pygame.draw.rect(self.screen, self.aliveCell,
                                     (rowIndex * self.cellHeight, colIndex * self.cellWidth, self.cellHeight,
                                      self.cellWidth))
                colIndex = colIndex + 1
            rowIndex = rowIndex + 1

    def count_alive_neighbors(self, rowIndex, colIndex, grid):
        numberOfAliveNeighbors = 0
        if rowIndex == 0:
            if colIndex == 0:
                if grid[rowIndex][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
            elif colIndex == int(self.height/self.cellHeight) - 1:
                if grid[rowIndex][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex] == 1:
                    numberOfAliveNeighbors += 1
            else :
                if grid[rowIndex][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex + 1][colIndex] == 1:
                    numberOfAliveNeighbors += 1
        elif rowIndex == int(self.height/self.cellHeight) - 1:
            if colIndex == 0 :
                if grid[rowIndex - 1][colIndex] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex - 1][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
            elif colIndex == int(self.height/self.cellHeight) - 1:
                if grid[rowIndex - 1][colIndex] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex - 1][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
            else:
                if grid[rowIndex][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex - 1][colIndex - 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex - 1][colIndex + 1] == 1:
                    numberOfAliveNeighbors += 1
                if grid[rowIndex - 1][colIndex] == 1:
                    numberOfAliveNeighbors += 1
        elif colIndex == 0:
            if grid[rowIndex - 1][colIndex] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex - 1][colIndex + 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex][colIndex + 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex + 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex] == 1:
                numberOfAliveNeighbors += 1
        elif colIndex == int(self.height/self.cellHeight) - 1:
            if grid[rowIndex - 1][colIndex] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex - 1][colIndex - 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex][colIndex - 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex - 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex] == 1:
                numberOfAliveNeighbors += 1
        else:
            if grid[rowIndex - 1][colIndex - 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex - 1][colIndex] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex - 1][colIndex + 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex][colIndex - 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex][colIndex + 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex - 1] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex] == 1:
                numberOfAliveNeighbors += 1
            if grid[rowIndex + 1][colIndex + 1] == 1:
                numberOfAliveNeighbors += 1
        return numberOfAliveNeighbors

    def update_grid(self, grid):
        newGrid = grid
        rowIndex = 0
        for row in newGrid:
            colIndex = 0
            for col in row:
                if col == 1 and (
                        self.count_alive_neighbors(rowIndex, colIndex, grid) < 2 or self.count_alive_neighbors(rowIndex,
                                                                                                               colIndex,
                                                                                                               grid) > 3):
                    newGrid[rowIndex][colIndex] = 0
                elif col == 0 and self.count_alive_neighbors(rowIndex, colIndex, grid) == 3:
                    newGrid[rowIndex][colIndex] = 1
                elif col == 1 and (
                        self.count_alive_neighbors(rowIndex, colIndex, grid) == 2 or self.count_alive_neighbors(
                        rowIndex, colIndex, grid) == 3):
                    newGrid[rowIndex][colIndex] = 1
                else:
                    newGrid[rowIndex][colIndex] = 0
                colIndex = colIndex + 1
            rowIndex = rowIndex + 1
        return newGrid

    def run(self):
        while 1:
            time.sleep(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.grid = self.update_grid(self.grid)
            self.draw_from_grid(self.grid)
            pygame.display.flip()


if __name__ == '__main__':
    game = GameOfLife()
    game.run()
