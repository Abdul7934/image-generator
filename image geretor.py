from PIL import Image
import random

def generate_image(width, height):
    # Create a new image with RGB mode
    image = Image.new("RGB", (width, height))

    # Get the image's pixel access object
    pixels = image.load()

    # Generate random colors for each pixel
    for x in range(width):
        for y in range(height):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            # Set the pixel color
            pixels[x, y] = (red, green, blue)

    return image

def save_image(image, filename):
    # Save the generated image
    image.save(filename)
    print(f"Image saved as {filename}")

if __name__ == "__main__":
    # Set the dimensions of the image
    image_width = 500
    image_height = 500

    # Generate the image
    generated_image = generate_image(image_width, image_height)

    # Save the image
    save_image(generated_image, "generated_image.png")
