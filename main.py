
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def generate_ascii(image_path, width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    image = resize_image(image, width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_img = ""

    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    print(ascii_img)

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    generate_ascii(image_path)
