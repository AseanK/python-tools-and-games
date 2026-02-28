import os

from utils import package_installer
package_installer.install_dependencies()

from PIL import Image


def reduce_image_size(image_path, quality=85):
    fileName, ext = os.path.splitext(image_path)
    ext = ext.lower()

    img = Image.open(image_path)
    output_path = f"{fileName}_resize{ext}"

    if ext in ['.jpg', '.jpeg']:
        img.save(output_path, "JPEG", quality=quality)
    elif ext == '.png':
        img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
        img.save(output_path, "PNG", optimize=True)
    elif ext == '.webp':
        if getattr(img, "is_animated", False):  # Is file Animate?
            frames = []
            for frame in range(img.n_frames):
                img.seek(frame)
                frames.append(img.copy())
            frames[0].save(
                output_path,
                format="WEBP",
                save_all=True,
                append_images=frames[1:],
                quality=quality,
                duration=img.info.get("duration", 100),
                loop=img.info.get("loop", 0)
            )
        else:
            img.save(output_path, "WEBP", quality=quality)
    else:
        print("We can't resize this extension.")
        return

    print(f"{output_path} resize complete!")

image_path = input("Input image path: ")
reduce_image_size(image_path, quality=70)
