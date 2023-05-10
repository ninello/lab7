def num1():
    from PIL import Image
    photo = 'book1.jpg'
    with Image.open(photo) as img:
        img.load()

    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode

    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def num2():
    from PIL import Image
    photo = 'book2.jpg'
    with Image.open(photo) as img:
        img.load()

    photo2 = img.resize((img.width // 2, img.height // 2  ))
    photo2.save("resized_book2.jpg")
    img.show()

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("image_flipbook2_top.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("image_flipbook2.jpg")

def num3():
    from PIL import Image, ImageFilter

    filenames = ['book2.jpg', 'book3.jpg','book4.jpg', 'book5.jpg']
    for file in filenames:
        with Image.open(file) as img:
            img.load()
            img.show()
            f_img = img.filter(ImageFilter.CONTOUR)
            f_img.save("f_img" + file)
def num4():
    from PIL import Image
    mark = 'watermark.png'
    with Image.open(mark) as img_water:
        img_water.load()

    img_water = Image.open(mark)
    img_water = img_water.resize((img_water.width // 2, img_water.height // 2))

    filename = "book4.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (200, 15), img_water)
    img.save("water_book4.jpg")