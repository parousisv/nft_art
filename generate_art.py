from turtle import width
from PIL import Image
from PIL import ImageDraw
import random

def generate_lines():
    print("Hello World!")
    image_size_x = 512
    image_size_y = 512

    padding_x = 30
    padding_y = 30

    # numer of images
    for j in range (10):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        image = Image.new("RGB", size=(image_size_x, image_size_y), color=(red, green, blue))

        file_name = "C:\\Workspaces\\python_workspaces\\nft_art\images\\lines\\" + "image_" + str(j) + ".png"

        draw = ImageDraw.Draw(image)

        # number of lines
        for i in range(300):
            random_point_0 = (
                random.randint(padding_x, image_size_x - padding_x),
                random.randint(padding_y, image_size_y - padding_y)
            )

            random_point_1 = (
                random.randint(padding_x, image_size_x- padding_x),
                random.randint(padding_y, image_size_y- padding_y)
            )

            line_red = random.randint(0, 255)
            line_green = random.randint(0, 255)
            line_blue = random.randint(0, 255)

            line = (random_point_0, random_point_1)
            line_color = (line_red, line_green, line_blue)
            thickness = random.randint(0, 3)

            draw.line(line, fill=line_color, width=thickness)

            
        image.save(file_name)

if __name__ == "__main__":
    generate_lines()