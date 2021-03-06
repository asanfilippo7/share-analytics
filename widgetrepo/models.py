from django.db.models import Model
from django.db.models import IntegerField
from django.db.models import ForeignKey
from django.db.models import CharField
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.db.models import PROTECT
from django.db.models import CASCADE

from django.contrib.auth.models import User

class Widget(Model):

    name = CharField(
        max_length = 32,
        default='Unnamed Widget'
    )
    author = ForeignKey(
        User,
        on_delete=PROTECT
    )
    width = IntegerField(default=2)
    height = IntegerField(default=2)
    query = JSONField()
    settings = JSONField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        super(Widget, self).save(*args, **kwargs)


