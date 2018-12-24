from .graph_models import User, Post


def create_user_node(username: str):
    """
    Function safely creates user node in GraphDatabase.
    It prevent from creating duplicated nodes.
    :param username: username to create
    """
    try:
        User.nodes.get(name=username)
    except User.DoesNotExist:
        User(name=username).save()


def delete_all_nodes(node_set):
    for node in node_set:
        node.delete()


def create_post(name: str, description: str, author, photo):
    post = Post(name=name, description=description).save()
    post.author.connect(author)
    post.photo.connect(photo)
    post.save()
