from .linker import link
import concurrent.futures as futures


def get_text():
    text = input("What would you like to write? ")
    return text


def get(win, input_text=None):
    # get size of win -- in order to limit size of text
    size = win.get_size()

    # check for defult text
    if not input_text:
        # limit time for user to answer
        with futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(get_text)
            try:
                input_text = future.result(100)
            except futures.TimeoutError:
                print("\ntook to long to answer text set to 'testing'")
                input_text = "testing"

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
