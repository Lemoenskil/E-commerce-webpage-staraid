from django.contrib import admin
from .models import NewsUser
class NewsletterAdmin(admin.ModelAdmin):
	list_display =('email','date_added',)
admin.site.register(NewsUser, NewsletterAdmin)
