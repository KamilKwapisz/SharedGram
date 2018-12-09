from datetime import datetime
import pytz

from neomodel import config
from neomodel import StructuredNode, RelationshipTo, RelationshipFrom, StructuredRel
from neomodel import StringProperty, IntegerProperty, UniqueIdProperty, DateTimeProperty
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
    name = StringProperty
    following = RelationshipTo('User', 'FOLLOWS', model=Follow)
    followers = RelationshipFrom('User', 'FOLLOWED BY', model=Follow)
    likes = RelationshipTo('Photo', 'LIKES', model=Like)


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


class Post(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    photo = RelationshipTo('Photo', 'PHOTO', cardinality=One)
    hashtags = RelationshipTo('HashTag', 'TAG')
    description = StringProperty()
    liked_by = RelationshipFrom('User', 'LIKED BY', model=Like)

    @property
    def likes_number(self):
        return len(self.liked_by.all())
