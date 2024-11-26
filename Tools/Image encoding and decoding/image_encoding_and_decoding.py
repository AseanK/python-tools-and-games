import os
import base64


def encode_image(file_path):
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        output_file = f"{os.path.splitext(os.path.basename(file_path))[0]}_encode.txt"
        with open(output_file, "w", encoding="utf-8") as text_file:
            text_file.write(encoded_string)
        print(f"\n✅ Image encoding successful! Result saved in '{output_file}'.")
    except Exception as e:
        print(f"⚠️ Error during encoding: {e}")


def decode_image(encoded_string, output_path):
    try:
        image_data = base64.b64decode(encoded_string)
        with open(output_path, "wb") as image_file:
            image_file.write(image_data)
        print(f"\n✅ Image decoding successful! Result saved in '{output_path}'.")
    except Exception as e:
        print(f"⚠️ Error during decoding: {e}")


def list_files(current_dir):
    print(f"\n📂 Current directory: {current_dir}")
    print("=" * 40)
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            print(f"[DIR]  {item}")
        else:
            print(f"       {item}")
    print("=" * 40)


def change_directory(current_dir):
    target_dir = input("Enter the directory to move to ('..' for parent directory): ").strip()
    if target_dir == "..":
        return os.path.dirname(current_dir)
    else:
        new_dir = os.path.join(current_dir, target_dir)
        if os.path.isdir(new_dir):
            return new_dir
        else:
            print("⚠️ Directory does not exist.")
            return current_dir


def main():
    current_dir = os.getcwd()
    while True:
        list_files(current_dir)
        print("\n🛠️  Select an action")
        print("[1] Encode an image")
        print("[2] Decode an image from encoded text")
        print("[3] Change directory")
        print("[4] Exit")
        choice = input("Select (1/2/3/4): ").strip()

        if choice == "1":
            file_name = input("🔎 Enter the name of the image file to encode: ").strip()
            file_path = os.path.join(current_dir, file_name)
            if os.path.exists(file_path):
                encode_image(file_path)
            else:
                print("⚠️ File does not exist.")

        elif choice == "2":
            encoded_file = input("🔎 Enter the name of the encoded text file: ").strip()
            encoded_path = os.path.join(current_dir, encoded_file)
            if os.path.exists(encoded_path):
                with open(encoded_path, "r", encoding="utf-8") as text_file:
                    encoded_string = text_file.read()
                output_name = input("💾 Enter the name of the output image file (e.g., output.png): ").strip()
                output_path = os.path.join(current_dir, output_name)
                decode_image(encoded_string, output_path)
            else:
                print("⚠️ Text file does not exist.")

        elif choice == "3":
            current_dir = change_directory(current_dir)

        elif choice == "4":
            print("\nExiting the program. 👋")
            break

        else:
            print("⚠️ Invalid input. Please try again.")


if __name__ == "__main__":
    main()
