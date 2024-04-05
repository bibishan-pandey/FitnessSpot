import uuid


def upload_image_location(instance, filename, upload_type="avatar"):
    """
    Upload location for the user profile avatar, cover image, and user post images.
    """

    # check if the file is an image and has an extension
    if not filename.endswith('.jpg') and not filename.endswith('.png') and not filename.endswith('.jpeg'):
        raise Exception("File is not supported. Please upload an image (jpg, png, jpeg) file.")

    extension = filename.split('.')[-1]
    filename = f"{instance.user.profile.pid}_{uuid.uuid4()}.{extension}"
    file_path = f'profiles/{instance.user.username}/{upload_type}/{filename}'
    return file_path


def upload_video_location(instance, filename, upload_type="video"):
    """
    Upload location for the user video post.
    """

    # check if the file is a video and has an extension
    if not filename.endswith('.mp4') and not filename.endswith('.avi') and not filename.endswith('.mov'):
        raise Exception("File is not supported. Please upload a video (mp4, avi, mov) file.")

    extension = filename.split('.')[-1]
    filename = f"{instance.user.profile.pid}_{uuid.uuid4()}.{extension}"
    file_path = f'profiles/{instance.user.username}/{upload_type}/{filename}'
    return file_path


def upload_avatar_location(instance, filename):
    """
    Upload location for the user profile avatar.
    """
    return upload_image_location(instance, filename, "avatar")


def upload_cover_location(instance, filename):
    """
    Upload location for the user profile cover image.
    """
    return upload_image_location(instance, filename, "cover")


def upload_post_image_location(instance, filename):
    """
    Upload location for the user post image.
    """
    return upload_image_location(instance, filename, "post/image")


def upload_post_video_location(instance, filename):
    """
    Upload location for the user post video.
    """
    return upload_video_location(instance, filename, "post/video")
