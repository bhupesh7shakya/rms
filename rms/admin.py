from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    list_per_page=10
    search_fields=('name',)
    ordering=('id','name',)


admin.site.register(models.Food)
admin.site.register(models.Table)
admin.site.register(models.Profile)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)