from django.contrib import admin

from .models import Graph, GraphWithUser
# Register your models here.

class GraphAdmin(admin.ModelAdmin):
# To get the read-only fields to show up in the interface: 
    readonly_fields = ('created_at', 'last_modified')

admin.site.register(Graph, GraphAdmin)
admin.site.register(GraphWithUser)