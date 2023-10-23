from PIL import Image

# Function to save and display a 2D pixel array.
def save_and_disp_png(data, filename):
    # Save PNG.
    img = Image.new('RGB', (len(data[0]), len(data)))
    for y, row in enumerate(data):
        for x, pixel in enumerate(row):
            img.putpixel((x, y), pixel)
    img.save(filename, format='PNG')
    # Display PNG.
    with Image.open(filename) as img:
        img.show()
