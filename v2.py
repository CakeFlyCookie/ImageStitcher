import os
from PIL import Image, ImageDraw, ImageFont

# Получаем список всех файлов в текущей директории
files = os.listdir()

# Фильтруем только файлы с расширениями .jpg и .png
image_files = [file for file in files if file.endswith('.jpg') or file.endswith('.png')]

# Если нет изображений, то завершаем программу
if not image_files:
    print("No image files found.")
    exit()

# Определяем размер самого маленького изображения
min_size = float('inf')
for file in image_files:
    with Image.open(file) as img:
        size = min(img.size)
        if size < min_size:
            min_size = size

# Размер текста для названия файла
font_size = int(min_size * 0.05)

# Создаем список изображений и их названий
images = []
names = []
for file in image_files:
    with Image.open(file) as img:
        # Изменяем размер изображения
        img = img.resize((min_size, min_size))

        # Добавляем изображение в список
        images.append(img)

        # Получаем имя файла без расширения
        name = os.path.splitext(file)[0]
        names.append(name)

# Определяем ширину и высоту выходного изображения
num_images = len(images)
num_cols = min(num_images, 5)
num_rows = (num_images - 1) // num_cols + 1
out_width = num_cols * min_size
out_height = num_rows * (min_size + font_size)

# Создаем выходное изображение
output = Image.new('RGB', (out_width, out_height), color='white')

# Создаем объект для рисования на выходном изображении
draw = ImageDraw.Draw(output)

# Координаты текущей позиции на выходном изображении
x = 0
y = 0

# Рисуем изображения на выходном изображении
for i, img in enumerate(images):
    # Если текущий столбец заполнен, переходим на следующую строку
    if i % num_cols == 0 and i > 0:
        x = 0
        y += min_size + font_size

    # Вставляем изображение на выходное изображение
    output.paste(img, (x, y))

    # Рисуем название файла под изображением
    name = names[i]
    text_width, text_height = draw.textsize(name)
    text_x = x + min_size // 2 - text_width // 2
    text_y = y + min_size + font_size // 2 - text_height // 2
    draw.text((text_x, text_y), name, font=ImageFont.truetype("arial.ttf", font_size), fill='black', stroke_width=2, stroke_fill='white')

    # Переходим к следующему столбцу
    x += min_size

# Сохраняем выходное изображение
output.save('output.png', optimize=True, compress_level=9)
