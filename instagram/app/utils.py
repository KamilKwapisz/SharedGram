from .graph_models import User


def create_user_node(username: str):
    try:
        User.nodes.get(name=username)
    except User.DoesNotExist:
        User(name=username).save()
