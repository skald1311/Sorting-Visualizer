"""
Sorting Visualizer
#2#
Author: Duong
When: April 7, 2023
"""
import pygame
import random
import math
from bubblesort import bubble_sort

pygame.init()

class Information: # Class for the information of the game
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    YELLOW = 255, 255, 51
    BACKGROUND_COLOR = 0, 0, 51
    SIDE_PAD = 100
    TOP_PAD = 150
    GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
    FONT = pygame.font.SysFont('calibri', 30)
    BIG_FONT = pygame.font.SysFont('calibri', 40, bold = True)
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.lst = lst
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption('Sorting Visualizer')
        self.set_list(lst)
    
    def set_list(self, lst):
        """
        A function that gets called in init to further set properties
        Did this to make it more readable
        And if we reset, we just have to call this function, not initialize new info object
        """
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.tower_width = round((self.width - self.SIDE_PAD) / len(lst))  # Width of a tower that is dynamic with the width of the screen
        self.height_per_px = math.floor((self.height - self.TOP_PAD) / (self.max_val))  # height / max, which gives height per 1px 
        self.start_x = self.SIDE_PAD // 2

def generate_random_list(n, max_val):
    """
    Generating a list with random numbers
    n: length of the list
    Return: the random list
    """
    lst = []
    for i in range(n):
        random_numb = random.randint(1, max_val)
        lst.append(random_numb)
    return lst

def draw(info, algo_name):
    info.screen.fill(info.BACKGROUND_COLOR)

    title = info.BIG_FONT.render(f"{algo_name}", 1, info.YELLOW)  # surface object
    info.screen.blit(title, ((info.width/2) - (title.get_width()/2) , 10))

    controls1 = info.FONT.render("R - Reset | SPACE - Start Sorting", 1, info.WHITE)  # surface object
    info.screen.blit(controls1, ((info.width/2) - (controls1.get_width()/2) , 45))

    speed_control = info.FONT.render("Speed: J - Slow | K - Fast", 1, info.WHITE)
    info.screen.blit(speed_control, ((info.width/2) - (speed_control.get_width()/2) , 75))

    controls2 = info.FONT.render("A - Bubble | S - Selection | D - Insertion | F - Merge | G - Quick", 1, info.WHITE)
    info.screen.blit(controls2, ((info.width/2) - (controls2.get_width()/2) , 105))



    draw_list(info)
    pygame.display.update()

def draw_list(info, color_pos = {}, clear_bg = False):
    """
    Draw the towers
    """
    lst = info.lst
    
    if clear_bg:
        clear_rect = (info.SIDE_PAD // 2, info.TOP_PAD, info.width - info.SIDE_PAD, info.height - info.TOP_PAD)
        pygame.draw.rect(info.screen, info.BACKGROUND_COLOR, clear_rect)

    
    for i in range(len(lst)):
        x = info.start_x + i * info.tower_width  # Left point rule
        y = info.height - (lst[i] * info.height_per_px)  # The height of the screen minus the height of the tower = the height of the space that is not the tower. But coordinate is up down in pygame
        color = info.GRADIENTS[i % 3]   # element beside each other has different remainder

        if i in color_pos:
            color = color_pos[i]

        pygame.draw.rect(info.screen, color, (x, y, info.tower_width, info.height))

    if clear_bg:
        pygame.display.update()

def main():
    """
    Main function
    """
    n = 50
    max_val = 100

    random_list = generate_random_list(n, max_val)
    info = Information(800, 600, random_list)
    running = True
    sorting = False
    clock = pygame.time.Clock()
    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None

    speed_slow = False
    
    while running:
        if speed_slow:
            clock.tick(30)  # fps: 30
        else:
            clock.tick(60)
        
        if sorting:
            try:
                next(sorting_algo_generator)  
            except Exception:  # if we call next on a generator and it doesn't have the next yield, it will raise an Exception
                sorting = False
        else:
            draw(info, sorting_algo_name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User pressed X / closed the program
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:  # R key = RESET
                random_list = generate_random_list(n, max_val) 
                info.set_list(random_list)
                sorting = False
            elif event.key == pygame.K_j: # Slow speed
                speed_slow = True
            elif event.key == pygame.K_k: # Slow speed
                speed_slow = False
            elif (event.key == pygame.K_SPACE) and (sorting == False) :  # Space = start sorting
                sorting = True
                sorting_algo_generator = sorting_algo(info)
            

    
    pygame.quit()

if __name__ == "__main__":
    main()

