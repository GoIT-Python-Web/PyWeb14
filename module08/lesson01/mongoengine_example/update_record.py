from models import Post

if __name__ == '__main__':

    post = Post.objects(title='MongoEngine Documentation')

    post.update(link_url='http://docs.mongoengine.org/')

    for p in post:
        print(p.to_mongo().to_dict())

