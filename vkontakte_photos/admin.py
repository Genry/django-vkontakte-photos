# -*- coding: utf-8 -*-
from django.contrib import admin
from vkontakte_api.admin import VkontakteModelAdmin
from models import Album, Photo

class PhotoInline(admin.TabularInline):

    def image(self, instance):
        return '<img src="%s" />' % (instance.src_small,)
    image.short_description = 'photo'
    image.allow_tags = True

    model = Photo
    fields = ('created','image','text','owner','group','user','likes','comments','tags')
    readonly_fields = fields
    extra = False
    can_delete = False

class AlbumAdmin(VkontakteModelAdmin):

    def image_preview(self, obj):
        return u'<a href="%s"><img src="%s" height="30" /></a>' % (obj.thumb_src, obj.thumb_src)
    image_preview.short_description = u'Картинка'
    image_preview.allow_tags = True

    list_display = ('image_preview','title','size','vk_link','created','updated')
    list_display_links = ('title',)
    search_fields = ('title','description')
    inlines = [PhotoInline]

class PhotoAdmin(VkontakteModelAdmin):

    def image_preview(self, obj):
        return u'<a href="%s"><img src="%s" height="30" /></a>' % (obj.src_big, obj.src)
    image_preview.short_description = u'Картинка'
    image_preview.allow_tags = True

    list_display = ('image_preview','text','vk_link','likes','created')
    list_display_links = ('text',)
    list_filter = ('album',)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)