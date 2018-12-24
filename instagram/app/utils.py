from .graph_models import User


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
