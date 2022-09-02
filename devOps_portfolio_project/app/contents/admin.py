from django.contrib import admin
from contents.models import HostedContent, UploadedContent, CheckedContent

# Register your models here.
admin.site.register(HostedContent)
admin.site.register(UploadedContent)
admin.site.register(CheckedContent)
