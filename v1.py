from PIL import Image
import os

images = []
total_width = 0
max_height = 0

# проходим по всем файлам в текущей директории
for filename in os.listdir():
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # открываем изображение
        img = Image.open(filename)
        # добавляем изображение в список
        images.append(img)
        # считаем общую ширину и максимальную высоту
        total_width += img.size[0]
        max_height = max(max_height, img.size[1])

# создаем новое изображение, суммируя ширину и высоту входных изображений
result = Image.new('RGB', (total_width, max_height))

# рисуем входные изображения на новом изображении
x_offset = 0
for img in images:
    result.paste(im=img, box=(x_offset, 0))
    x_offset += img.size[0]

# сохраняем получившееся изображение
result.save('result.png')
