from PIL import Image
import os

def reduce_image_size(image_path, quality=85):
    fileName, ext = os.path.splitext(image_path)
    ext = ext.lower()

    img = Image.open(image_path)
    output_path = f"{fileName}_resize{ext}"

    if ext in ['.jpg', '.jpeg']:
        img.save(output_path, "JPEG", quality=quality)
    elif ext == '.png':
        # 1. 색상 수 줄이기 (8비트 PNG로 변환)
        img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
        img.save(output_path, "PNG", optimize=True)
    else:
        print("We can't resize this extension.")
        return

    print(f"{output_path} resize complete!")


image_path = input("Input image path: ")
reduce_image_size(image_path, quality=70)
