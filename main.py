import pygame, numpy as np, math as mt, sys, csv
from ast import literal_eval as magic
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
savefile = "map_eg.csv"
file = open(savefile)
Parser = csv.reader(file)
Colours = {}
grid = []
RecordingCol = True
for dat in Parser:
    print(dat)
    if dat[0] == ".":
        RecordingCol = False
    elif RecordingCol:
        Colours[dat[0]] = dat[1]
    elif dat[0] != "=":
        grid.append([dat[0], dat[1], dat[2]])
while True:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
    pygame.draw.rect(screen, magic(Colours["BG"]), [0, 0, width, height])
    for block in grid:
        x = int(block[0])
        y = int(block[1])
        ID = block[2]
        pygame.draw.rect(screen, magic(Colours[ID]), [x/16*width, y/9*height, width/16, height/9])
    pygame.display.flip()
