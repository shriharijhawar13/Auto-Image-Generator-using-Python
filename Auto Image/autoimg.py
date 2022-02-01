from PIL import Image, ImageDraw, ImageFont
 
img = Image.new('RGB', (100, 50), color = (73, 109, 137))
 
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
d = ImageDraw.Draw(img)

name= "Hello World"

if " " not in name:
    initials = name[0]
else:
    for i in range(0,len(name)):
        if name[i] == ' ':
            break

    initials = name[0] + name[i+1]


print(initials)
d.text((10,10), initials, font=fnt, fill=(255, 255, 0))
 
img.save('pil_text_font.png')



'''
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1000, 300), color = (73, 109, 137))


d = ImageDraw.Draw(img)


name= "Hello World"

print(len(name))
for i in range(0,len(name)):
    if name[i] == ' ':
        break

initials = name[0] + name[i+1]

font = ImageFont.truetype("arial.ttf", 15)


print(initials)
d.text((500,150), initials, font=font , fill=(255, 255, 0))

img.save('pil_text_font.png')'''


# Aashman Foundation is a non for profit organisation working resolutely 
# towards promoting the cause of women, empowering single income families 
# and promoting child education, through its various livelihood programs. 
# Through our various endevours our aim is to protect and promote the well 
# being of underprivileged sections of the society and create a positive impact 
# as responsible stakeholders of society.


# RESQ Charitable Trust is a not-for-profit organisation founded in 2007 with an
# aim to minimise animal suffering and reduce human-animal conflict by providing
# emergency animal rescue, rehabilitation, medical aid and conducting education
# and awareness programs to promote peaceful coexistence between humans and animals. 
# We run two divisions, one for domestic animals and the other for wildlife and
# have provided free medical aid, rescue and rehabilitation to over 80,000+ animals since inception.



# The Akshaya Patra Foundation is a not-for-profit organisation headquartered in Bengaluru, India. The
# Foundation strives to eliminate classroom hunger by implementing the Mid-Day Meal Programme. It prov
# ides nutritious meals to children studying in Government schools and Government-aided schools. Akshaya
# Patra also aims to counter malnutrition and support right to education of children hailing from
# socio-economically challenging backgrounds.


# Started in 1988 with a magazine for children from the underserved communities, Katha’s work spans the
#  literacy to literature continuum. By seamlessly connecting grassroots work in education and urban resurgence,
#   Katha brings children living in poverty into reading and quality education. Over the past three decades,
#    through its many programmes, Katha has helped over one million children help themselves out of poverty.


# CHILDLINE 1098 is a phone number that spells hope for millions of children across India. It is a 24-hour a day,
# 365 days a year, free, emergency phone service for children in need of aid and assistance. We not only respond
# to the emergency needs of children but also link them to relevant services for their long-term care and rehabilitation.
# We have, till date, connected to three million children across the nation offering them care and protection.



