from PIL import Image
import os

def concat_images(image_list):
    """
    Concatenates images horizontally (side-by-side).
    """
    widths, heights = zip(*(i.size for i in image_list))
    total_width = sum(widths)
    max_height = max(heights)

    new_img = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for img in image_list:
        new_img.paste(img, (x_offset,0))
        x_offset += img.width

    return new_img

def generate_image_names(n):
    """
    Generates image names based on the given pattern.
    """
    for i in range(1, n+1):
        yield f"{i}"
        for j in range(1, n+1):
            yield f"{i}_{j}"
            for k in range(1, n+1):
                yield f"{i}_{j}_{k}"

def generate_images():
    """
    Generates new images based on the given pattern.
    """
    for name in generate_image_names(12):
        images = [Image.open(f"{i}.jpg") for i in name.split('_')]
        result = concat_images(images)
        result.save(f"{name}.jpg")

if __name__ == "__main__":
    generate_images()