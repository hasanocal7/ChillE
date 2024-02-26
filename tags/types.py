from strawberry import auto
import strawberry_django
from .models import Tag

@strawberry_django.type(Tag)
class TagType:
    name: auto