from django.contrib import admin
from .models import Konten, Komentar

@admin.register(Konten)
class KontenAdmin(admin.ModelAdmin):
    list_display = ('judul', 'slug', 'kategori', 'penulis', 'terbit', 'status')
    list_filter = ('status', 'dibuat', 'terbit', 'penulis', 'kategori')
    search_fields = ('judul', 'body', 'kategori')
    prepopulated_fields = {'slug' : ('judul',)}
    raw_id_fields = ('penulis',)
    date_hierarchy = 'terbit'
    ordering = ('status', 'terbit', 'judul', 'kategori')

@admin.register(Komentar)
class KomentarAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'konten', 'dibuat', 'aktif')
    list_filter = ('aktif', 'dibuat', 'diperbarui')
    search_fields = ('nama', 'email', 'isi')
