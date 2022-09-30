from .linker import link
import concurrent.futures as futures
import pygame
from conts import WIDTH, HEIGHT
import sys


def _get_text():
    text = input("What would you like to write? ")
    return text

def get_text(win):
    place_holder = "... write here ..."
    text = place_holder
    font = pygame.font.SysFont(None, 50)
    while True:
        pygame.display.flip()
        win.fill((255,255,255))
        if text == place_holder:
            render_text = font.render(text, True, (200,200,200,200))
        else:
            render_text = font.render(text, True, (0,0,0))
        x_pos = (WIDTH - render_text.get_size()[0])/2
        y_pos = (HEIGHT -render_text.get_size()[1])/2
        win.blit(render_text, (x_pos, y_pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Bye!")
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text

                elif event.key ==  pygame.K_BACKSPACE:
                    text = text[:-1]
                    if text == "":
                        text = place_holder
                elif event.key == pygame.K_SPACE:
                    text += " "
                else:
                    if text == place_holder:
                        text = ""
                    try:
                        if (char := event.unicode).isalpha():
                            if event.mod and event.mod == pygame.K_LSHIFT:
                                text += char.upper()
                            else:
                                text += char
                    except ValueError: ## invaild key
                        pass



def get(win, input_text=None):
    # get size of win -- in order to limit size of text
    size = win.get_size()

    # check for defult text
    if not input_text:
        input_text= get_text(win)

    # load letter vals
    import json

    with open("D:/Fourier/text/letters.json", "r") as file:
        letters = json.load(file)

    # divide into word and link to prevent words spliting over lines
    words = input_text.split()
    text = []
    for word in words:
        text.append(link([letters[i] for i in word], size)[-1])
        text.append(letters[" "])
    # finaly link words
    return link(text, size)


# import json
# with open("D:/Fourier/text/letters.json", "r") as file:
#     letters = json.load(file)

# for i in letters:
#     max_x = max(letters[i], key=lambda x: x["x"])["x"]
#     min_x = min(letters[i], key=lambda x: x["x"])["x"]

#     print(f"{i}, {max_x=}, {min_x=}, diff = {max_x-min_x}")
