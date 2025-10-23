import pygame
from pygame.locals import *
import sys # provide system related functions ( exit/font etc. ) 
import random


pygame.init()


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("ASL Trainer") # caption 


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def text(surface, msg, x, y, color, size, center=False):
    fontobj = pygame.font.SysFont("arial", size, bold=True)
    msgobj = fontobj.render(msg, True, color)
    rect = msgobj.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(msgobj, rect)


def draw_button(surface, rect, label, border_color=WHITE, fill=None, label_color=WHITE):
    if fill:
        pygame.draw.rect(surface, fill, rect, border_radius=15)
    pygame.draw.rect(surface, border_color, rect, width=3, border_radius=15)
    text(surface, label, rect.centerx, rect.centery, label_color, 26, center=True)


def draw_vertical_gradient(surface, top_color, bottom_color): ##HELP EXPLAINING THIS 
    h = surface.get_height()
    w = surface.get_width()
    y = 0
    while y < h:
        ratio = y / float(h - 1)
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (w, y))
        y += 1


def load_scaled(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, size) # blits the image to the true size ( scales it)


def scale_to_fit(img, max_w, max_h):
    r = img.get_rect()
    w = r.width
    h = r.height
    s = min(max_w / float(w), max_h / float(h))
    nw = int(w * s)
    nh = int(h * s)
    return pygame.transform.smoothscale(img, (nw, nh))


logo_img = load_scaled('/Users/dhanyashankar/Downloads/ASL_logo.png', (240, 110)) # loading the logo image 
logo_rect = logo_img.get_rect(center=(300, 72)) # keeping the image in the center


learn_img = load_scaled('/Users/dhanyashankar/Downloads/ChatGPT Image Aug 1, 2025, 05_02_09 PM.png', (200, 100))
exit_img  = load_scaled('/Users/dhanyashankar/Downloads/OFFICIAL EXIT SIGN.png', (200, 100))


def asl(path):
    return load_scaled(path, (340, 470))


signs = []
signs.append(('A', asl('/Users/dhanyashankar/Downloads/ASL_a.png')))
signs.append(('B', asl('/Users/dhanyashankar/Downloads/ASL_b (1).png')))
signs.append(('C', asl('/Users/dhanyashankar/Downloads/ASL_c (1).png')))
signs.append(('D', asl('/Users/dhanyashankar/Downloads/ASL_d (1).png')))
signs.append(('E', asl('/Users/dhanyashankar/Downloads/ASL_e (1).png')))
signs.append(('F', asl('/Users/dhanyashankar/Downloads/ASL_f (1).png')))
signs.append(('G', asl('/Users/dhanyashankar/Downloads/ASL_g (1).png')))
signs.append(('H', asl('/Users/dhanyashankar/Downloads/ASL_h (1).png')))
signs.append(('I', asl('/Users/dhanyashankar/Downloads/ASL_i (2).png')))
signs.append(('J', asl('/Users/dhanyashankar/Downloads/ASL_j.png')))
signs.append(('K', asl('/Users/dhanyashankar/Downloads/ASL_k.png')))
signs.append(('L', asl('/Users/dhanyashankar/Downloads/ASL_l.png')))
signs.append(('M', asl('/Users/dhanyashankar/Downloads/ASL_m.png')))
signs.append(('N', asl('/Users/dhanyashankar/Downloads/ASL_n.png')))
signs.append(('O', asl('/Users/dhanyashankar/Downloads/ASL_o.png')))
signs.append(('P', asl('/Users/dhanyashankar/Downloads/ASL_p.png')))
signs.append(('Q', asl('/Users/dhanyashankar/Downloads/ASL_q.png')))
signs.append(('R', asl('/Users/dhanyashankar/Downloads/ASL_r.png')))
signs.append(('S', asl('/Users/dhanyashankar/Downloads/ASL_s.png')))
signs.append(('T', asl('/Users/dhanyashankar/Downloads/ASL_t.png')))
signs.append(('U', asl('/Users/dhanyashankar/Downloads/ASL_u.png')))
signs.append(('V', asl('/Users/dhanyashankar/Downloads/ASL_v.png')))
signs.append(('W', asl('/Users/dhanyashankar/Downloads/ASL_w.png')))
signs.append(('X', asl('/Users/dhanyashankar/Downloads/ASL_x.png')))
signs.append(('Y', asl('/Users/dhanyashankar/Downloads/ASL_y.png')))
signs.append(('Z', asl('/Users/dhanyashankar/Downloads/ASL_z.png')))


index = 0 
menu_learn_rect = pygame.Rect(200, 300, 200, 100)
menu_exit_rect = pygame.Rect(200, 430, 200, 100)
next_rect = pygame.Rect(430, 530, 140, 50)
back_rect = pygame.Rect(30, 530, 140, 50)
yes_rect = pygame.Rect(120, 360, 150, 60)
no_rect = pygame.Rect(330, 360, 150, 60)



window = "menu"
quiz_images = []
quiz_layout = []
quiz_ready = False

# For multiple choice quiz
mc_signs = []  # [(letter, img), ...]
mc_options = []  # [[option1, option2, option3], ...]
mc_selected = [None, None]  # User's selected option index for each sign
mc_rects = []  # Rects for each option box
mc_feedback = [None, None]  # True/False for correct/incorrect
mc_next_rect = pygame.Rect(230, 520, 140, 50)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if window == "menu": # like multiple slides ( bliting learn and exit options) ( Menu is the mains screen)
                if menu_learn_rect.collidepoint(x, y):
                    window = "learn" 
                elif menu_exit_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()
            elif window == "learn": # Goes to the next sign ( if there is more) 
                if next_rect.collidepoint(x, y):
                    if index + 1 < len(signs):
                        index = index + 1
                    else:
                        window = "prompt" # Quiz screen
                elif back_rect.collidepoint(x, y):
                    index = 0
                    window = "menu"
            elif window == "prompt": 
                if yes_rect.collidepoint(x, y):
                    quiz_images = []
                    used = set() # set makes sure there is no duplicates or repeated items 
                    while len(quiz_images) < 6:
                        pick = random.choice(signs)
                        key = pick[0] 
                        if key not in used:
                            used.add(key)
                            quiz_images.append(pick[1])
                    quiz_layout = []
                    r1 = pygame.Rect(45, 210, 160, 170)
                    r2 = pygame.Rect(220, 210, 160, 170)
                    r3 = pygame.Rect(395, 210, 160, 170)
                    r4 = pygame.Rect(45, 395, 160, 170)
                    r5 = pygame.Rect(220, 395, 160, 170)
                    r6 = pygame.Rect(395, 395, 160, 170)
                    quiz_layout.append(r1)
                    quiz_layout.append(r2)
                    quiz_layout.append(r3)
                    quiz_layout.append(r4)
                    quiz_layout.append(r5)
                    quiz_layout.append(r6)
                    quiz_ready = True # making it available after the user goes through all the signs 
                    window = "quiz"
                elif no_rect.collidepoint(x, y):# a rect method used to check if a point/thing is inside the rectangle area 
                    index = 0
                    window = "menu"

            elif window == "quiz":
                if back_rect.collidepoint(x, y):
                    index = 0
                    window = "menu"
                # After quiz, go to multiple choice quiz
                elif next_rect.collidepoint(x, y):
                    # Prepare 2 random signs and 3 options for each
                    mc_signs.clear()
                    mc_options.clear()
                    mc_selected[:] = [None, None] # stores what option is clicked by the user. Initially its none because its empty 
                    mc_feedback[:] = [None, None] # stores if the answer is correct or wrong
                    used_letters = set() # keep tracks of alr used signs 
                    while len(mc_signs) < 2: # Radonmly pickes 2 unique signs ( tuple)- not changable 
                        pick = random.choice(signs)
                        if pick[0] not in used_letters:
                            mc_signs.append(pick)
                            used_letters.add(pick[0])
                    # For each sign, create 3 options (1 correct, 2 random incorrect)
                    for sign in mc_signs:
                        correct = sign[0]
                        options = [correct]
                        while len(options) < 3:
                            l = random.choice(signs)[0]
                            if l not in options:
                                options.append(l)
                        random.shuffle(options)
                        mc_options.append(options)
                    # Prepare rects for option boxes
                    mc_rects.clear() # clearing the rectangles 
                    # For each sign, 3 boxes horizontally next to the sign
                    y_positions = [220, 370]
                    for i in range(2): # makes sure we just have 2 signs ( yes and no)- repeated/ non-repeated 
                        row = []
                        for j in range(3): # options for the answers
                            rect = pygame.Rect(320 + j*80, y_positions[i], 70, 60)
                            row.append(rect)
                        mc_rects.append(row)
                    window = "mc_quiz" # move to the quiz screen

            elif window == "mc_quiz":
                # Check if user clicked an option box
                for i in range(2): 
                    for j in range(3):
                        if mc_rects[i][j].collidepoint(x, y):
                            mc_selected[i] = j # when someone clicks somewhere, it stores the options
                            # Check correctness
                            if mc_options[i][j] == mc_signs[i][0]:
                                mc_feedback[i] = True # checks if the answer is correct
                            else:
                                mc_feedback[i] = False # checks if the answer is wrong 
                # Next button
                if mc_next_rect.collidepoint(x, y):
                    # Reset and go back to menu or restart quiz
                    index = 0
                    window = "menu"


    if window == "menu":
        draw_vertical_gradient(screen, (255, 180, 100), (255, 100, 60))
        screen.blit(logo_img, logo_rect.topleft)
        draw_button(screen, menu_learn_rect, "LEARN", border_color=WHITE, label_color=WHITE)
        draw_button(screen, menu_exit_rect, "EXIT", border_color=WHITE, label_color=WHITE)
        screen.blit(learn_img, (menu_learn_rect.x, menu_learn_rect.y))
        screen.blit(exit_img, (menu_exit_rect.x, menu_exit_rect.y))
        text(screen, "ASL Trainer", 300, 185, WHITE, 50, center=True)


    elif window == "learn":
        draw_vertical_gradient(screen, (80, 140, 255), (20, 60, 180))
        screen.blit(logo_img, logo_rect.topleft)
        pair = signs[index]
        letter = pair[0]
        img = pair[1]
        img_rect = img.get_rect()
        img_rect.center = (230, 320)
        screen.blit(img, img_rect.topleft)
        font = pygame.font.SysFont("arial", 150, bold=True)
        letter_surface = font.render(letter, True, WHITE)
        letter_rect = letter_surface.get_rect()
        letter_rect.midleft = (img_rect.right + 40, img_rect.centery)
        screen.blit(letter_surface, letter_rect.topleft)
        draw_button(screen, next_rect, "NEXT", border_color=WHITE, label_color=WHITE)
        draw_button(screen, back_rect, "BACK", border_color=WHITE, label_color=WHITE)


    elif window == "prompt":
        draw_vertical_gradient(screen, (80, 140, 255), (20, 60, 180))
        screen.blit(logo_img, logo_rect.topleft)
        text(screen, "Do you want to test your knowledge?", 300, 240, WHITE, 32, center=True)
        draw_button(screen, yes_rect, "YES", border_color=WHITE, label_color=WHITE)
        draw_button(screen, no_rect, "NO", border_color=WHITE, label_color=WHITE)



    elif window == "quiz": # blitting it 
        draw_vertical_gradient(screen, (30, 35, 60), (10, 10, 20)) # scaling the image
        screen.blit(logo_img, logo_rect.topleft)
        text(screen, "Identify these signs", 300, 170, WHITE, 36, center=True)
        if quiz_ready:
            i = 0
            while i < len(quiz_images):
                thumb = scale_to_fit(quiz_images[i], 150, 160)
                rect = quiz_layout[i]
                trect = thumb.get_rect(center=rect.center) # centering the image in that window 
                screen.blit(thumb, trect.topleft)
                i += 1
        draw_button(screen, back_rect, "BACK", border_color=WHITE, label_color=WHITE)
        draw_button(screen, next_rect, "NEXT", border_color=WHITE, label_color=WHITE)

    elif window == "mc_quiz":
        draw_vertical_gradient(screen, (60, 60, 120), (20, 20, 40))
        screen.blit(logo_img, logo_rect.topleft)
        text(screen, "Multiple Choice Quiz", 300, 120, WHITE, 36, center=True)
        # Draw 2 signs and 3 option boxes for each
        for i in range(2):
            sign_img = scale_to_fit(mc_signs[i][1], 120, 120)
            img_rect = sign_img.get_rect()
            img_rect.topleft = (120, 200 + i*150)
            screen.blit(sign_img, img_rect.topleft)
            # Draw option boxes
            for j in range(3):
                rect = mc_rects[i][j]
                # Highlight if selected
                fill = (80, 200, 80) if mc_selected[i] == j and mc_feedback[i] == True else (200, 80, 80) if mc_selected[i] == j and mc_feedback[i] == False else (40, 40, 60)
                draw_button(screen, rect, mc_options[i][j], border_color=WHITE, fill=fill, label_color=WHITE)
            
    pygame.display.flip()
    pygame.time.Clock().tick(60)
