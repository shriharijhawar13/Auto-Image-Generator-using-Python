from PIL import Image, ImageDraw, ImageFont
 
 # Specify the image dimensions and the RGB value of the background colour.
img = Image.new('RGB', (100, 50), color = (73, 109, 137))
 
 # Specify the path of the font library and specify the text font size
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
d = ImageDraw.Draw(img)


name= "Hello World"

# Used to obtain the initials of the first two words from the text 
if " " not in name:
    initials = name[0]
else:
    for i in range(0,len(name)):
        if name[i] == ' ':
            break

    initials = name[0] + name[i+1]

# Generate the image
print(initials)
d.text((10,10), initials, font=fnt, fill=(255, 255, 0))
 
img.save('pil_text_font.png')








