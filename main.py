import time

import PIL.Image


def get_luminosite(c: tuple) -> int:
    s = 0
    for i in c[:3]:
        s += i

    return int(s/3)


def main():

    img = PIL.Image.open("Background.png")
    result = img.copy()

    w, h = result.size

    target_color = 0, 0, 0
    new_color = 29, 40, 50

    for x in range(w):
        for y in range(h):

            value = img.getpixel((x, y))

            if value[3] > 100 and get_luminosite(value) < 50:

                result.putpixel((x, y), (*new_color, value[3]))

    result.show()

    result.save("result.png")


if __name__ == '__main__':
    main()
