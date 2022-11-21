from models import Post, LinkPost, TextPost, ImagePost, User


if __name__ == '__main__':
    ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

    post1 = TextPost(title='Fun with MongoEngine', author=ross)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save()

    steve = User(email='steve@example.com', first_name='Steve', last_name='Buscemi').save()

    post1 = ImagePost(title='Node.js the best', author=steve)
    post1.image_path = 'https://web-creator.ru/uploads/Page/22/nodejs.svg'
    post1.tags = ['node', 'js']
    post1.save()
