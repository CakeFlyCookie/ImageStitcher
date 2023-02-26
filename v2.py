import os
from PIL import Image, ImageDraw, ImageFont

# Открываем папку, в которой находится скрипт
dir_path = os.path.dirname(os.path.realpath(__file__))

# Создаем список файлов с расширением .jpg или .png
files = [f for f in os.listdir(dir_path) if f.endswith('.jpg') or f.endswith('.png')]

# Определяем размер самого маленького изображения
sizes = [Image.open(f).size for f in files]
min_size = min(sizes)

# Создаем новое изображение, на котором будем склеивать оригинальные изображения
rows = []
current_row = []
max_width = min_size[0] * 5  # Максимальная ширина ряда - 5 минимальных изображений
total_height = 0
for f in files:
    # Открываем изображение и изменяем его размер до минимального
    img = Image.open(f)
    img = img.resize(min_size)

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(img)

    # Определяем размер шрифта для текста с именем файла
    font_size = int(min_size[1] * 0.05)
    font = ImageFont.truetype('arial.ttf', font_size)

    # Рисуем текст с именем файла снизу посередине
    name = os.path.splitext(os.path.basename(f))[0]  # Имя файла без расширения
    text_width, text_height = draw.textsize(name, font=font)
    text_x = (min_size[0] - text_width) // 2
    text_y = min_size[1] - text_height - font_size
    draw.text((text_x - 1, text_y - 1), name, font=font, fill='white', stroke_width=2, stroke_fill='white')
    draw.text((text_x + 1, text_y - 1), name, font=font, fill='white', stroke_width=2, stroke_fill='white')
    draw.text((text_x + 1, text_y + 1), name, font=font, fill='white', stroke_width=2, stroke_fill='white')
    draw.text((text_x - 1, text_y + 1), name, font=font, fill='white', stroke_width=2, stroke_fill='white')
    draw.text((text_x, text_y), name, font=font, fill='black')

    # Добавляем изображение в текущий ряд
    current_row.append(img)
    total_height = max(total_height, img.size[1])

    # Если текущий ряд достиг максимальной ширины, начинаем новый ряд
    if sum([img.size[0] for img in current_row]) >= max_width:
        rows.append(current_row)
        current_row = []

# Добавляем последний ряд, если он не пустой
if current_row:
    rows.append(current_row)

# Определяем общую высоту изображения
total_height = sum([max([img.size[1] for img in row]) for row in rows])

# Создаем новое изображение, на котором будем склеивать все изображения
result_img = Image.new('RGB', (max_width, total_height), (255, 255, 255))

#Координаты текущего изображения на результирующем изображении
x = 0
y = 0

# Склеиваем изображения
result = Image.new('RGB', (max_width, total_height), color='white')
y_offset = 0
for row in rows:
    x_offset = 0
    row_height = max([img.size[1] for img in row])
    for img in row:
        result.paste(img, (x_offset, y_offset))
        x_offset += img.size[0]
    y_offset += row_height

# Сохраняем результат
result.save('result.png', optimize=True, compression=9)

