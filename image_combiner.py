from PIL import Image
from os import listdir
from os.path import isfile, join


def image_combiner(self, name: str, images: list, card_size: tuple, margin: int, color=(255, 255, 255)):
    y_offset = 0
    canvas_width = card_size[0] * 3 + margin * 2
    canvas_height = card_size[1] * 3 + margin * 2
    chunk_counter = 0
    images = list(self.chunks(images, 9))
    for big_chunk in images:
        new_image = Image.new('RGBA', (canvas_width, canvas_height), color)
        cards_row = list(self.chunks(big_chunk, 3))
        for i in range(len(cards_row)):
            for j in range(len(cards_row[i])):
                picture = Image.open(cards_row[i][j], mode="r")
                if not picture.size == card_size:
                    picture = picture.resize(card_size, Image.ANTIALIAS)
                x_offset = j * (card_size[0] + margin)
                new_image.paste(picture, (x_offset, y_offset))
            y_offset = (i + 1) * (card_size[1] + margin)
        y_offset = 0
        chunk_counter += 1
        new_image_name = name + str(chunk_counter) + '.png'
        output_file = os.path.join(self.for_printing_folder, new_image_name)
        new_image.save(output_file)


def combine(cards_list: list):
    image_combiner("card", cards_list, (532, 744), 2)


def listfile(mypath: str) -> list:
    onlyfiles = [file for file in listdir(mypath) if isfile(join(mypath, file))]
    return onlyfiles

dirname = os.path.dirname(__file__)
cards_folder = os.path.join(dirname, './cards/')
combine(listfile(cards_folder))

