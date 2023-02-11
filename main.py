import PIL.Image

img = PIL.Image.open("originale.png")


def get_brightness(c: tuple) -> int:
    s = 0
    for i in c[:3]:
        s += i

    return int(s/3)


def void() -> PIL.Image.Image:
    return PIL.Image.new("RGBA", img.size)


def recolorize(new_color=(29, 40, 50)) -> PIL.Image.Image:
    result = img.copy()

    w, h = result.size

    for x in range(w):
        for y in range(h):

            value = img.getpixel((x, y))

            if value[3] > 100 and get_brightness(value) < 50:
                result.putpixel((x, y), (*new_color, value[3]))

    return result


def main():
    void_img = void()
    recolor_img = recolorize()

    new = void_img

    new.show()
    new.save("result.png")


if __name__ == '__main__':
    main()
