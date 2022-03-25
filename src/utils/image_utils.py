from PIL import Image, ImageChops, ImageOps
from werkzeug.datastructures import FileStorage


def get_image(image_file: FileStorage):
    img = Image.open(image_file)
    img = img.convert('L')
    img = img.point(lambda x: 0 if x < 200 else 255, 'L')

    if has_transparency(img):
        img = set_background_white(img)

    if img.size != (28, 28):
        img = resize(img, (28, 28))

    return img


def resize(img: Image, size: (int, int)):
    return img.resize(size, Image.ANTIALIAS)


def set_background_white(img: Image):
    new_image = Image.new('RGBA', img.size, 'WHITE')
    new_image.paste(img, mask=img)
    return new_image.convert('RGB')


def trim(img: Image):
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)

    bbox = diff.getbbox()

    if bbox:
        return img.crop(bbox)


def has_transparency(img: Image):
    if img.info.get('transparency', None) is not None:
        return True
    if img.mode == 'P':
        transparent = img.info.get('transparency', -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == 'RGBA':
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False
