from django.contrib import admin
from .models import SesiUjian, Jawaban


class JawabanInline(admin.TabularInline):
    model = Jawaban
    extra = 0
    readonly_fields = ['soal', 'teks_jawaban', 'nilai', 'alasan_nilai', 'grading_status', 'graded_at']
    can_delete = False


@admin.register(SesiUjian)
class SesiUjianAdmin(admin.ModelAdmin):
    list_display = ['mahasiswa', 'ujian', 'status', 'total_nilai', 'waktu_mulai', 'waktu_selesai']
    list_filter = ['status', 'ujian']
    search_fields = ['mahasiswa__nama_lengkap', 'mahasiswa__nim']
    readonly_fields = ['waktu_mulai', 'ip_address', 'last_heartbeat']
    inlines = [JawabanInline]


@admin.register(Jawaban)
class JawabanAdmin(admin.ModelAdmin):
    list_display = ['sesi', 'soal', 'nilai', 'grading_status', 'graded_at']
    list_filter = ['grading_status', 'nilai']
    readonly_fields = ['submitted_at', 'graded_at']
