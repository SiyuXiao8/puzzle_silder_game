'''
    CS 5001
    FALL 2021
    Final Project - Puzzle Game
    Siyu Xiao
    Puzzle Game Program - a combination puzzle game, a player slides the puzzle
        to form a complete puzzle
'''
import turtle
import os
import time
import math
import random
import glob
X_POSITION = -280
Y_POSITION = 250
TURN_RIGHT_ANGLE = 90

def splash_screen():
    '''
    Function -- splash_screen
        display the splash_screen image for 3 seconds
    No Parameter
    Returns none
    '''
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    turtle.Screen().addshape('splash_screen.gif')
    turtle.shape('splash_screen.gif')
    time.sleep(3)
    turtle.clearscreen()
    os.chdir(current_directory)

def input_name():
    '''
    Function -- input_name
        ask user for their name
    No Parameter
    Returns name as a string
    '''
    name = turtle.textinput('CS5001 Puzzle Slide', 'Your Name:')
    return str(name)

def input_moves():
    '''
    Function -- input_moves
        ask user for the number of moves they want
    No Parameter
    Returns moves as int
    '''
    moves = turtle.numinput('CS5001 Puzzle Slide', \
                       'Enter the number of move (chances) you want (5-200)', \
                            minval=5, maxval=200)
    return int(moves)

def gameboard_rectangle(x, y, length, width, color="black", pensize=8):
    '''
    Function -- gameboard_rectangle
        draws the play area, leaderboard, and status borad's rectangle
    Parameters:
        x -- x axis posistion
        y -- y axis posistion
        length -- length of the rectangle
        width -- width of the rectangle
        color -- color of turtle default is black
        pensize -- pensize of turtle default is size 8
    Returns none
    '''
    gameboard = turtle.Turtle()
    gameboard.speed(0)
    gameboard.pencolor(color)
    gameboard.pensize(pensize)
    gameboard.up()
    gameboard.ht()
    gameboard.goto(x, y)
    gameboard.down()
    gameboard.st()
    for i in range(2):
        gameboard.forward(width)
        gameboard.right(TURN_RIGHT_ANGLE)
        gameboard.forward(length)
        gameboard.right(TURN_RIGHT_ANGLE)
    gameboard.up()
    gameboard.ht()
    
def exit_program(x,y):
    '''
    Function -- exit_program
        display the quitmsg image and quit the program
    Returns none
    '''
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    wn = turtle.Screen()
    turtle.up()
    turtle.ht()
    turtle.goto(0,0)
    turtle.down()
    turtle.st()
    wn.addshape('quitmsg.gif')
    turtle.shape('quitmsg.gif')
    time.sleep(3)
    os.chdir(current_directory)
    turtle.clearscreen()
    turtle.bye()

def quit_button():
    '''
    Function -- quit__button
        display the quit button and calls exit_program when user clicks on quit
    No Parameter
    Returns none
    '''
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    quits = turtle.Turtle()
    wn = turtle.Screen()
    quits.up()
    quits.ht()
    wn.addshape('quitbutton.gif')
    quits.goto(280, -275)
    quits.down()
    quits.st()
    quits.shape('quitbutton.gif')
    os.chdir(current_directory)
    quits.onclick(exit_program)

def load_puz(turtles, tile_location, pic, move_list):
    '''
    Function -- load_puz
        load the puzzle pieces that user picked
    Parameters:
        turtles -- the turtles objects that attach the puzzle pieces
        tile_location -- contains the image of the puzzle pieces
        pic -- the turtle object that attached thumbnail
        move_list -- a list that contains players move
    Returns none
    '''
    puz_list = []
    current_directory = os.getcwd()
    # add files ends with .puz to puz_list
    for name in glob.glob(current_directory + '/*.puz'):
        puz_list.append(name.split('/')[-1])
    # if there are more than 10 files show the warning
    if len(puz_list) > 10:
        os.chdir(current_directory + '/Resources')
        turtle.up()
        turtle.ht()
        turtle.goto(0,0)
        turtle.down()
        turtle.st()
        turtle.Screen().addshape('file_warning.gif')
        turtle.shape('file_warning.gif')
        time.sleep(3)
    puz_of_choice = turtle.textinput('Load Puzzle', \
                                     'Enter the name of puzzle of choice: ' \
                                     + '\n' +'\n'.join(puz_list))
    os.chdir(current_directory)
    # hide the previous thumbnail gif
    pic.ht()
    turtle.clear()
    # hide the previous puzzle pieces
    for each in turtles:
        each.ht()
    # reinitialize player move to 0
    move_list[0] = 0
    puz, info, turtle_name, tile_location, size, resize =\
         directive_info(puz_of_choice)
    pic = attach_thumbnail(info[3][1])
    turtles = shuffled_tiles(tile_location, turtle_name, size, resize,\
                             move_list)
    load = load_button_image()
    load_button(turtles, tile_location, load, pic, move_list)
    reset = reset_button_image()
    reset_button(turtles, tile_location, reset)
    
def load_button_image():
    '''
    Function -- load_button_image
        attach the loadbutton.gif to the screen
    No Parameter
    Returns turtle object called load
    '''
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    load = turtle.Turtle()
    wn = turtle.Screen()
    load.up()
    load.ht()
    wn.addshape('loadbutton.gif')
    load.goto(180, -275)
    load.down()
    load.st()
    load.shape('loadbutton.gif')
    os.chdir(current_directory)
    return load

def load_button(turtles, tile_location, load, pic, move_list):
    '''
    Function -- load_button
        activates onlick when user click on the load button
    Parameters:
        turtles -- the objects that attach the puzzle pieces
        tile_location -- contains the image of the puzzle pieces
        load -- a turtle object called load
        pic -- the turtle object that attached thumbnail
        move_list -- the list that contains player moves
    Returns none
    '''
    load.onclick(lambda x,y: load_puz(turtles, tile_location, pic, move_list))

def resets(turtles, tile_location):
    '''
    Function -- resets
        a cheat button that reset the puzzle pieces
    Parameters:
        turtles -- the turtle objects that attach the puzzle pieces
        tile_location -- contains the image of the puzzle pieces
    Returns none
    '''
    i = 0
    # attach the image in a ordered pattern
    for each in turtles:
        each.shape(tile_location[i])
        i += 1
    
def reset_button_image():
    '''
    Function -- reset_button_image
        attach the reset gif on the screen
    No Parameter
    Returns the turtle object called reset
    '''
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    reset = turtle.Turtle()
    wn = turtle.Screen()
    reset.up()
    reset.ht()
    wn.addshape('resetbutton.gif')
    reset.goto(75, -275)
    reset.down()
    reset.st()
    reset.shape('resetbutton.gif')
    os.chdir(current_directory)
    return reset

def reset_button(turtles, tile_location, reset):
    '''
    Function -- reset_button
        activates the reset button when user clicks on it
    Parameters:
        turtles -- the turtle objects that attach the puzzle pieces
        tile_location -- contains the image of the puzzle peices
        reset -- the turtle object called reset
    Returns none
    '''
    reset.onclick(lambda x,y: resets(turtles, tile_location)) 
    
def write(x, y, string, pen_color, font_size):
    '''
    Function -- write
        writes the string passed in by the user
    Parameters:
        x -- x axis position
        y -- y axis position
        string -- str input from user
    Returns none
    '''
    writes = turtle.Turtle()
    writes.color(pen_color)
    writes.up()
    writes.ht()
    writes.goto(x, y)
    writes.down()
    writes.st()
    writes.write(string, font= ('Arial',font_size,'normal'))
    writes.up()
    writes.ht()
    
def write_move(x, y, string, pen_color, font_size, write_turtle):
    '''
    Function -- write_move
        responsible for writing the player moves section
    '''
    write_turtle.color(pen_color)
    write_turtle.up()
    write_turtle.ht()
    write_turtle.goto(x, y)
    write_turtle.down()
    write_turtle.st()
    write_turtle.write(string, font= ('Arial',font_size,'normal'))
    write_turtle.up()
    write_turtle.ht()
    
def setup_gameboard(name):
    '''
    Function -- setup_gameboard
        draws the play area, status, and leaderboard area. Also writes leader
    Parameters:
        name -- name input from user
    Returns none
    '''
    turtle.setup(800, 800)
    turtle.title("CS5001 Silding Puzzle Game - Siyu Xiao")
    gameboard_rectangle(-350, 320, 500, 450) # play area
    gameboard_rectangle(120, 320, 500, 230, 'blue', 6) # leader board
    gameboard_rectangle(-350, -230, 100, 700) # Status area
    write(130, 280, 'Leaders:', 'blue', 18) # Leader: on the leader board
    write(130, 250, name, 'blue', 18)
    
def display_file_error():
    '''
    Function -- display_file_error
        display the file error gif to the user
    '''
    current_directory = os.getcwd() 
    os.chdir(current_directory + '/Resources')
    error = turtle.Turtle()
    wn = turtle.Screen()
    error.up()
    error.ht()
    error.goto(0,0)
    error.down()
    error.st()
    wn.addshape('file_error.gif')
    error.shape('file_error.gif')
    time.sleep(3)
    error.ht()
    os.chdir(current_directory)
    
def directive_info(filename='mario.puz'):
    '''
    Function -- directive_info
        this function is responsible for processing all the information for the
        program to run
    Parameters:
        filename -- accpets .puz file, with mario.puz as default
    Returns all the info necessary for other functions
    '''
    try:
        with open(filename, mode='r') as file:
            puz_list = []
            info_list = [] 
            list_ = []
            turtle_name = []
            tile_location = []
            for each in file:
                new_list = []
                x = each.split(': ')
                for element in x:
                    new_list.append(element)
                for i in range(len(new_list)):
                    new_list[i] = new_list[i].strip('\n')
                list_.append(new_list)
            for i in range(len(list_)):
                if i <= 3:
                    info_list.append(list_[i])
                else:
                    puz_list.append(list_[i])
            for i in range(len(puz_list)):
                turtle_name.append(puz_list[i][0])
                tile_location.append(puz_list[i][1])
            # the size of the tile
            size = int(info_list[2][1])
            # added 2 to show the little gaps between each tiles
            resize = size + 2
            number = int(info_list[1][1])
            number_of_images = math.sqrt(number)
            # checks if the number of images is 16, 9, or 4
            if int(number_of_images + 0.5) ** 2 != number:
                display_file_error()
            return puz_list, info_list, turtle_name, tile_location,\
                   size, resize
    except Exception as msg:
        display_file_error()
        f = open("5001_puzzle.err.txt", "a")
        f.write(str(msg)+'\n')
        f.close()

def attach_thumbnail(thumbnail):
    '''
    Function -- attach_thumbnail
        attach the thumbnail gif
    Parameters:
        thumbnail -- the .gif image of thumbnail
    Returns the turtle object called pic
    '''
    thumbnail_location = str(thumbnail)
    pic = turtle.Turtle()
    wn = turtle.Screen()
    pic.up()
    pic.ht()
    wn.addshape(thumbnail_location)
    pic.goto(330, 280)
    pic.down()
    pic.st()
    pic.shape(thumbnail_location)
    return pic
   
def check_blank(current, neighbor, move_list):
    '''
    Function -- check_blank
        checks if the tile's neighbors is blank, if yes then swap places
    Parameters:
        current -- current place of the tile
        neighbor -- the surrounding tiles
        move_list -- list contains player move info
    Returns none
    '''
    # checks if surrouding tiles has blank.gif if yes then swap places
    if "blank.gif" in neighbor.shape():
        target_shape = current.shape()
        current.shape(neighbor.shape())
        neighbor.shape(target_shape)
        move_list[1].clear()
        move_list[0] += 1
        # when swap is successful then add the move by 1
        write_move(-310, -290, f'player moves: {move_list[0]} / '+\
                   f'{move_list[2]}','black', 20, move_list[1])
        
def swap_tile(turtl, resize, turtles, tile_location, move_list):
    '''
    Function -- swap_tile
        checks the neighboring tiles
    Parameters:
        information about the tiles and image of puzzle pieces
    Returns none
    '''
    pair = turtl.pos() #turtl is one turtle that carries the image
    # defines the "neighbors"
    left = (pair[0] - resize, pair[1])
    right = (pair[0] + resize, pair[1])
    top = (pair[0], pair[1] + resize)
    down = (pair[0], pair[1] - resize)
    for each in turtles:
        if each.pos() == right:
            # if the turtles image is to the right of the onclick turtle
            # see if its blank
            check_blank(turtl, each, move_list)
        elif each.pos() == left:
            check_blank(turtl, each, move_list)
        elif each.pos() == top:
            check_blank(turtl, each, move_list)
        elif each.pos() == down:
            check_blank(turtl, each, move_list)
    i = 0    
    for i in range(len(turtles)):
        # compare the pattern to the ordered pattern if not the same break
        if turtles[i].shape() != tile_location[i]:
            break
        # continue otherwise
        else:
            i += 1
    # if puzzle is solved then display winner.gif
    if i == len(turtles):
        current_directory = os.getcwd()
        os.chdir(current_directory + '/Resources')
        turtle.goto(0,0)
        turtle.down()
        turtle.st()
        turtle.Screen().addshape('winner.gif')
        turtle.shape('winner.gif')
        time.sleep(3)
        os.chdir(current_directory)
        turtle.clearscreen()
        turtle.bye()
    # if puzzle is unsolved within the move specified, then display lose.gif
    if move_list[0] == move_list[2]:
        current_directory = os.getcwd()
        os.chdir(current_directory + '/Resources')
        turtle.goto(0,0)
        turtle.down()
        turtle.st()
        turtle.Screen().addshape('Lose.gif')
        turtle.shape('Lose.gif')
        time.sleep(2)
        turtle.Screen().addshape('credits.gif')
        turtle.shape('credits.gif')
        time.sleep(3)
        os.chdir(current_directory)
        turtle.clearscreen()
        turtle.bye()
        
def square(x_pos, y_pos, size):
    '''
    Function -- sqaure
        draws the sqaures around the tiles
    Parameters:
        x_pos -- the x position of the tile
        y_pos -- the y position of the tile
        size -- the size of the tile
    Returns none
    '''
    x = int(size/2)
    y = int(size/2)
    t = turtle
    t.pencolor('black')
    t.speed(0)
    t.pensize(0)
    t.up()
    t.ht()
    t.goto(x_pos-x, y_pos+y)
    t.down()
    t.st()
    # draws the square
    for k in range(4):
                t.forward(size)
                t.right(TURN_RIGHT_ANGLE)
                
def shuffled_tiles(tile_location, turtle_name, size, resize, move_list):
    '''
    Function -- shuffled_tiles
        shuffle the tiles and display the shuffled puzzle pieces for user to
        solve
    Parameters:
        tile_location -- image of puzzle peices
        turtle_name -- the turtle objects that attach the puzzle pieces
        size -- the size of the tile
        resize -- the size of the tile +2 to show the gaps between tiles
        move_list -- contains the player move info
    Returns turtles that is responsible for attaching all the puzzle pieces
    '''
    wn = turtle.Screen()
    turtles = [] # different turtle objects
    shuffled_tile = tile_location.copy() # made a copy, so OG dont get changed
    random.shuffle(shuffled_tile) #shuffle the list
    length = int(math.sqrt(len(shuffled_tile)))
    for each in tile_location:
        wn.addshape(each)
    for each in turtle_name:
        each = turtle.Turtle()
        turtles.append(each)
    x_pos = X_POSITION
    y_pos = Y_POSITION
    a = 0
    # the two for loops gives the layers of the puzzle 4x4 3x3 or 2x2
    for i in range(length):
        turtles[a].up()
        turtles[a].ht()
        turtles[a].goto(0, y_pos)
        turtles[a].down()
        turtles[a].st()
        for j in range(length):
            turtles[a].speed(0)
            turtles[a].up()
            turtles[a].ht()
            turtles[a].goto(x_pos, y_pos)
            turtles[a].down()
            turtles[a].st()
            turtles[a].shape(shuffled_tile[a]) # Attach image
            def click(x, y,  tile=turtles[a]):
                return swap_tile(tile, resize, turtles, tile_location,\
                                 move_list)
            turtles[a].onclick(click)
            # draw broders around the tiles
            square(x_pos, y_pos, size) 
            a += 1
            x_pos += resize
        x_pos = -280
        y_pos -= resize
    turtle.up()
    turtle.ht()
    return turtles

def main():
    splash_screen()
    name = input_name()
    write_turtle = turtle.Turtle()
    moves = input_moves()
    move_list = [0, write_turtle, moves]
    setup_gameboard(name)
    quit_button()
    load = load_button_image()
    reset = reset_button_image()
    puz, info, turtle_name, tile_location, size, resize = directive_info()
    pic = attach_thumbnail(info[3][1]) 
    turtles = shuffled_tiles(tile_location, turtle_name, size, resize,\
                             move_list)
    load_button(turtles, tile_location, load, pic, move_list)
    reset_button(turtles, tile_location, reset)
    
if __name__ == "__main__":
    main()
