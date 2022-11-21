from models import Post, User


if __name__ == '__main__':
    posts = Post.objects()
    print('------ Posts -------')
    for post in posts:
        print(post.to_mongo().to_dict())
    print('------ Users -------')
    users = User.objects()
    for user in users:
        print(user.to_mongo().to_dict())

    post = User.objects(first_name='Steve')
    print(post.delete())  # Повертає кількість видалених елементів

    posts = Post.objects()
    print('------ Posts -------')
    for post in posts:
        print(post.to_mongo().to_dict())
    print('------ Users -------')
    users = User.objects()
    for user in users:
        print(user.to_mongo().to_dict())