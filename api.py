import config

def getCellByCoords(x, y):
    row = int(x) // config.CELL_HEIGHT
    col = int(y) // config.CELL_WIDTH

    return (row, col)

def getLineEq(x1,y1,x2,y2):
    A = y1 - y2
    B = x2 - x1
    C = -(A * x1 + B * y1)

    return A, B, C
