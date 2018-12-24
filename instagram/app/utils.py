from django.contrib.auth import authenticate

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


def are_passwords_matching(form) -> bool:
    """
    Checks whether password field and password confirm field have same value
    :param form: filled Django form instance
    :return: true if fields have same value, false otherwise
    """
    return form.cleaned_data['password'] == form.cleaned_data['password_confirm']


def create_and_authenticate_user(form):
    """
    Creates user object with cleaned data from django form.
    Then user is authenticated with credentials provided in form
    :param form: filled Django form instance
    :return: user object if everything is correct, None otherwise
    """
    user_object = form.save(commit=False)
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user_object.email = username
    user_object.set_password(password)
    user_object.save()
    user = authenticate(username=username, password=password)
    return user
