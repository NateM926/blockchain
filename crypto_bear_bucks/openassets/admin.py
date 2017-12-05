from django.contrib import admin
from openassets.models import Asset_Definition_File, Output

class OpenAssetsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Asset_Definition_File, OpenAssetsAdmin)
admin.site.register(Output, OpenAssetsAdmin)