from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

def upload_image(file):
    response = upload(file)
    url, options = cloudinary_url(
        response['public_id'],
        format="jpg",
        crop="fill",
        width=100,
        height=100
    )
    return url
