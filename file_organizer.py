import os
import shutil

folder = "MyFiles"

categories = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if os.path.isfile(path):

        extension = os.path.splitext(filename)[1].lower()

        for category, extensions in categories.items():

            if extension in extensions:

                destination = os.path.join(folder, category)

                os.makedirs(destination, exist_ok=True)

                shutil.move(
                    path,
                    os.path.join(destination, filename)
                )

                break

print("Files organized successfully!")
input("Press Enter to exit...")