import os
from PIL import Image
print("Current directory:", os.getcwd())
try:
    image = Image.open("photo.jpg")
    print("Image loaded successfully!")
    resized = image.resize((200, 200))
    resized.show()
    resized.save("resized_photo.jpg")
    print("✅ Image resized and saved!")
except Exception as e:
    print(f"❌ Error: {e}")
