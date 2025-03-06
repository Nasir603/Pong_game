from PIL import Image

# Open JPEG file
image = Image.open("background.jpg")

# Convert and save as GIF
image.convert("RGB").save("background.gif")
