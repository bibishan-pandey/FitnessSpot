import os
import shutil


def copy_images_to_media_folder():
    """
    Script file used to copy images from the static folder to the media folder.

    ONLY USE THIS SCRIPT IF YOU WANT TO LOAD DATA FROM FIXTURES FOR POST.
    """

    # Define paths
    static_images_dir = 'static/images'
    media_images_dir = 'media/post/image'

    # Create media directory if it doesn't exist
    os.makedirs(media_images_dir, exist_ok=True)

    # Copy images from static folder to media folder
    for filename in os.listdir(static_images_dir):
        if filename.endswith('.jpg'):
            src_path = os.path.join(static_images_dir, filename)
            dst_path = os.path.join(media_images_dir, filename)
            shutil.copyfile(src_path, dst_path)


if __name__ == "__main__":
    copy_images_to_media_folder()
