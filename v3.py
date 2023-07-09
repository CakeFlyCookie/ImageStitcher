from PIL import Image, ImageDraw, ImageFont
import os
from tqdm import tqdm
import pillow_avif

# Получаем список всех поддерживаемых расширений файлов
supported_formats = [f.lower() for f in Image.registered_extensions()]

# Собираем список всех файлов с поддерживаемыми расширениями в текущей директории
images = [f for f in os.listdir('.') if f.lower().endswith(tuple(supported_formats))]

# Если изображений нет, выводим сообщение об ошибке и завершаем скрипт
if not images:
    print('Нет изображений в текущей директории!')
    exit()

# Определяем размер наименьшего изображения
min_size = float('inf')
min_size_img = None
for image in images:
    with Image.open(image) as img:
        width, height = img.size
        curr_size = width * height
        if curr_size < min_size:
            min_size = curr_size
            min_size_img = img

# Рассчитываем количество рядов и столбцов изображений
num_rows = (len(images) - 1) // 5 + 1
num_cols = min(5, len(images))

# Создаем пустую картинку, на которой будем рисовать склеенные изображения
result_width = num_cols * min_size_img.width
result_height = num_rows * min_size_img.height
result = Image.new('RGB', (result_width, result_height), color='white')

# Рисуем каждое изображение на нужном месте на результирующей картинке
font_size = int(min(min_size_img.width, min_size_img.height) * 0.05)
font = ImageFont.truetype('arial.ttf', size=font_size)
draw = ImageDraw.Draw(result)
for i, image in enumerate(tqdm(images)):
    with Image.open(image) as img:
        img = img.resize((min_size_img.width, min_size_img.height))
        row = i // 5
        col = i % 5
        x = col * min_size_img.width
        y = row * min_size_img.height
        result.paste(img, (x, y))

        # Подписываем изображение своим названием
        name = os.path.splitext(image)[0]
        text_width, text_height = draw.textsize(name, font=font)
        text_x = x + (min_size_img.width - text_width) // 2
        text_y = y + min_size_img.height - text_height - 15
        outline_width = max(1, int(font_size * 0.15))
        draw.text((text_x, text_y), name, font=font, fill='black', stroke_width=outline_width, stroke_fill='white')

        # Обновляем прогресс-бар
        tqdm.write(f"Обработано {i+1}/{len(images)} изображений")

# Сохраняем склеенное изображение в файл
result.save('result.png', compress_level=9)

# Удаляем скрипт
os.remove(__file__)
