from datetime import datetime
import pytz

from neomodel import config
from neomodel import StructuredNode, StructuredRel
from neomodel import StringProperty, UniqueIdProperty, DateTimeProperty, RelationshipTo, RelationshipFrom
from neomodel.cardinality import One

config.DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687'


class Follow(StructuredRel):
    since = DateTimeProperty(
        default=lambda: datetime.now(pytz.utc)
    )


class Like(StructuredRel):
    date = DateTimeProperty(
        default=lambda: datetime.now(pytz.utc)
    )


class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    following = RelationshipFrom('User', 'FOLLOWS', model=Follow)
    followers = RelationshipTo('User', 'FOLLOWED BY', model=Follow)
    likes = RelationshipTo('Photo', 'LIKES', model=Like)
    posts = RelationshipTo('Post', 'ADDED')


class Photo(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()


class HashTag(StructuredNode):
    uid = UniqueIdProperty()
    name_ = StringProperty()

    @property
    def name(self):
        return self.name_.lower() if self.name_ else None

    @name.setter
    def name(self, value):
        if value.startswith('#'):
            self.name_ = value
        else:
            self.name_ = "#" + value


class Comment(StructuredNode):
    uid = UniqueIdProperty()
    author = RelationshipFrom('User', 'AUTHOR', cardinality=One)
    text = StringProperty()
    date = DateTimeProperty(
        default=lambda: datetime.now(pytz.utc)
    )
    post = RelationshipTo('Post', "COMMENT")
    liked_by = RelationshipFrom('User', 'LIKED BY', model=Like)
    commented_by = RelationshipFrom('Comment', 'COMMENTED BY')

    @property
    def name(self):
        return f"{self.author.name}'s comment" if self.author else None


class Post(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    author = RelationshipFrom('User', 'AUTHOR', cardinality=One)
    photo = RelationshipTo('Photo', 'PHOTO', cardinality=One)
    hashtags = RelationshipTo('HashTag', 'TAG')
    description = StringProperty()
    comments = RelationshipTo('Comment', 'COMMENT')
    liked_by = RelationshipFrom('User', 'LIKED BY', model=Like)

    @property
    def likes_number(self):
        return len(self.liked_by.all())
# TODO on create - fetching hashtags from comments and creating HashTag model

