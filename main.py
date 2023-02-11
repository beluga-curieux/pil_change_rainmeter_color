import PIL.Image


def main():

    img = PIL.Image.open("Background.png")
    result = img.copy()

    w, h = result.size

    target_color = 0, 0, 0
    new_color = 29, 40, 50

    for x in range(w):
        for y in range(h):

            value = img.getpixel((x, y))

            if value[:3] == target_color and value[3] > 100:
                result.putpixel((x, y), (*new_color, value[3]))

    result.show()


if __name__ == '__main__':
    main()
