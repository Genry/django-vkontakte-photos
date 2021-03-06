from vkontakte_users.factories import UserFactory
from models import Album, Photo
from datetime import datetime
import factory
import random

class AlbumFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Album

    remote_id = factory.LazyAttributeSequence(lambda o, n: '-%s_%s' % (o.group.remote_id, n))
    thumb_id = factory.Sequence(lambda n: n)

    created = datetime.now()
    updated = datetime.now()
    size = 1

class PhotoFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Photo

    remote_id = factory.LazyAttributeSequence(lambda o, n: '%s_%s' % (o.group.remote_id, n))
    user = factory.SubFactory(UserFactory)

    created = datetime.now()
    width = 10
    height = 10
