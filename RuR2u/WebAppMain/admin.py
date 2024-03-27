from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Elements


class ElementsAdmin(admin.ModelAdmin):
    def get_photo(self, object):
        return mark_safe(f"'<img src='{object.ElementPhoto.url}'")

admin.site.register(Category)

admin.site.register(Elements, ElementsAdmin)
