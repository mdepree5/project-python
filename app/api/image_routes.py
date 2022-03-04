from flask import Blueprint, request
from app.models import db, Image
from flask_login import current_user, login_required
from app.s3_helpers import (upload_file_to_s3, allowed_file, get_unique_filename)

image_routes = Blueprint("images", __name__)


@image_routes.route("", methods=["POST"])
@login_required
def upload_image():
    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)
    print('@@@@@', image.filename)

    upload = upload_file_to_s3(image)
    print('&&&&&&&&&&&&&&&&&&&',upload)

    if "url" not in upload:
        # if the dictionary doesn't have a filename key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload["url"]
  
    new_image = Image(user=current_user, url=url)
    db.session.add(new_image)
    db.session.commit()

    return {"url": url}


@image_routes.route("")
def get_all_images():
    images = Image.query.order_by(Image.id.desc()).all()
    return {"images": [image.to_dict() for image in images]}
