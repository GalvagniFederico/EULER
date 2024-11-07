import PIL.Image
from pynput.keyboard import Key, Controller
import time
import pyscreenshot
import cv2
import pytesseract
import numpy as np
def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                    for c in cols))
        if r in 'CF':
            print(line)
    print

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) 
            for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
            for s in squares)


def assign(values, s, d):
    #"""Eliminate all the other values (except d) from values[s] and propagate.
    #Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    #"""Eliminate d from values[s]; propagate when values or places <= 2.
    #Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')

    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

def parse_grid(grid):
    values = dict((s,digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values

def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def search(values):
    #"Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
        for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

def solve_grid(grid): 
    p = parse_grid(grid)
    return search(p)

def Solve():
    s = 0
    f = open("096_Sudoku\sudoku.txt")
    f = f.readlines()
    for i in range(0,len(f),10):
        grid_s = "".join("" + x[:9] for x in f[i+1:i+10])
        
        parse_grid((grid_s))
        solved_grid = solve_grid(grid_s)
        s+=int(solved_grid["A1"] + solved_grid["A2"] + solved_grid["A3"])
    
    print(s)

#Solve()7

keyboard = Controller()


def GetGrid():
    dim = 85
    ox = 1050
    oy = 402
    xbound = 8
    ybound = 8

    # Capture the screen with the given bounding box using pyscreenshot
    import pyscreenshot as ImageGrab
    img = ImageGrab.grab(bbox=[ox, oy, 1816, 1160])
    img.save("awd.png")

    # Load the saved image using OpenCV
    img = cv2.imread("awd.png")

    # Convert to grayscale
    

    # Configure tesseract path
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    config = '--psm 6 -c tessedit_char_whitelist=0123456789'
    grid = ''
    for y in range(9):
        for x in range(9):
            # Define the crop box coordinates
            x_start = x * dim +  4
            y_start = y * dim + ybound
            x_end = x_start + dim - xbound*3
            y_end = y_start + dim - ybound*2

            # Crop the image using numpy slicing
            img_cropped = img[y_start:y_end, x_start:x_end]

            # Show the cropped image (for debugging purposes)
            cv2.imshow(f'Cell {x},{y}', img_cropped)
            cv2.waitKey(50)
            # Perform OCR on the cropped image
            cell_text = pytesseract.image_to_string(img_cropped, config = config)
            # Remove newline characters and check if the text is numeric
            cell_text = cell_text.replace('\n', '').replace('\r', '')

            if str(cell_text).isnumeric() and len(cell_text) == 1:
                grid+= cell_text
            else:
                grid+= "0"

    return grid
            

    cv2.destroyAllWindows()

def TestGetGrid():
    rightGreed = '000500008200900004509300070010020080056000000700060001000000000900040007100200300'
    assert len(rightGreed) == 81

    testGrid = GetGrid()
    assert len(testGrid) == 81
    assert testGrid == rightGreed 

import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def Solve2():
    
    grid = GetGrid()
    display(parse_grid(grid))
    grid = '001005800280003070004200000010000000000050'
    grid = solve_grid(grid)
    display(grid)
    click(1070,250)
    for i in range(0,9):
        for j in range(0,9):
            keyboard.press(grid[squares[(i*9)+j]])
            time.sleep(0.02)
            keyboard.press(Key.right)
            time.sleep(0.02)
            if j == 8:
                keyboard.press(Key.down)
                time.sleep(0.01)
                for i in range(9): 
                    keyboard.press(Key.left)
                    time.sleep(0.01)




