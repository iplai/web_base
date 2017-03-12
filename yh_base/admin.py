# Stage 2 Update (Python 3)
from __future__ import unicode_literals
from django.contrib import admin
from yh_base.models import Website, Article, Account


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'website', 'url_',)
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'username', 'password', 'remarks', 'url_',)
    list_display_links = ('title',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Account, AccountAdmin)
