from django.contrib import admin
from blog.models import Feedback
from .models import *


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Feedback)
