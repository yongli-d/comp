from django.contrib import admin

# Register your models here.
from .models import Article
admin.site.register(Article)

from .models import Image
admin.site.register(Image)

from .models import Contributor 
admin.site.register(Contributor)
