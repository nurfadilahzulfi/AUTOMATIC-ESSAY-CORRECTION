from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'nama_lengkap', 'nim', 'kelas', 'role', 'is_exam_locked', 'is_active']
    list_filter = ['role', 'kelas', 'is_exam_locked', 'is_active']
    search_fields = ['username', 'nama_lengkap', 'nim']
    ordering = ['kelas', 'nama_lengkap']

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informasi Akademik', {
            'fields': ('role', 'nama_lengkap', 'nim', 'kelas', 'plain_password'),
        }),
        ('Status Ujian', {
            'fields': ('is_exam_locked', 'lock_reason', 'locked_at'),
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informasi Akademik', {
            'fields': ('role', 'nama_lengkap', 'nim', 'kelas'),
        }),
    )
