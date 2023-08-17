from . import api
from app import db
from app.models import Post


@api.route('/posts')
def get_posts():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [post.to_dict() for post in posts]
