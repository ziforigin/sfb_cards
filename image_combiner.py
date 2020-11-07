from PIL import Image
import os
from os.path import isfile, join

for_printing_folder = "./output/"


def chunks(file_list, length):
    for i in range(0, len(file_list), length):
        yield file_list[i:i + length]


def image_combiner(name: str, images: list, card_size: tuple, margin: int, color=(255, 255, 255)):
    y_offset = 0
    canvas_width = card_size[0] * 3 + margin * 2
    canvas_height = card_size[1] * 3 + margin * 2
    chunk_counter = 0
    images = list(chunks(images, 9))
    for big_chunk in images:
        new_image = Image.new('RGBA', (canvas_width, canvas_height), color)
        cards_row = list(chunks(big_chunk, 3))
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
        output_file = os.path.join(for_printing_folder, new_image_name)
        new_image.save(output_file)


def combine_cards(cards_list: list):
    image_combiner("card", cards_list, (532, 744), 2)


def combine_backs():
    dirname = os.path.dirname(__file__)
    card_path = os.path.join(dirname, '_SFB/sideb.png')
    back_list = [card_path] * 9
    image_combiner("back", back_list, (532, 744), 2)


def combine_characters(chars_list: list, inspired_list: list):
    image_combiner("char_front", chars_list, (532, 744), 2)
    image_combiner("char_back", inspired_list, (532, 744), 2)


def listfile(mypath: str) -> list:
    files = [os.path.join(mypath, file) for file in os.listdir(mypath)]
    files.sort()
    for file in files:
        print(file, end='\n')
    return files


def combine_object_cards(cards_list: list):
    image_combiner("obj", cards_list, (266, 372), 2)


def combine_object_backs():
    dirname = os.path.dirname(__file__)
    card_path = os.path.join(dirname, '_SFB/misc/_BACKSIDE_.png')
    back_list = [card_path] * 9
    image_combiner("obj_back", back_list, (266, 372), 2)


def trap_combiner(cards_list):
    image_combiner("trap_back", cards_list, (146, 146), 2)


def combine_trap_backs():
        dirname = os.path.dirname(__file__)
        card_path = os.path.join(dirname, '_SFB/misc/trap12.png')
        back_list = [card_path] * 12
        image_combiner("trap", back_list, (146, 146), 2)


dirname = os.path.dirname(__file__)
# cards_folder = os.path.join(dirname, '_SFB/cards/')
# chars_folder_front = os.path.join(dirname, '_SFB/chars2/')
# chars_folder_back = os.path.join(dirname, '_SFB/chars3/')
# obj_card_folder = os.path.join(dirname, '_SFB/goals')
trap_folder = os.path.join(dirname, '_SFB/traps')
# combine_cards(listfile(cards_folder))
# combine_backs()
# combine_characters(listfile(chars_folder_front), listfile(chars_folder_back))
# combine_object_backs()
# combine_object_cards(listfile(obj_card_folder))
# combine_trap_backs()
trap_combiner(listfile(trap_folder))

