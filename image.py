from PIL import Image, ImageDraw, ImageFont


font = ImageFont.truetype('tnr.ttf', 32)


def make_spanchbob(text: str) -> Image:
    img = Image.open('./images/001.jpg')
    draw = ImageDraw.Draw(img)

    draw.text((0, 0), text, font=font)

    return img
