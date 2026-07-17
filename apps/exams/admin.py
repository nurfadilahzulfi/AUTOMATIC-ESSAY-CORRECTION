from django.contrib import admin
from .models import MataPelajaran, Ujian, Soal


@admin.register(MataPelajaran)
class MataPelajaranAdmin(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'dosen']
    search_fields = ['kode', 'nama']


class SoalInline(admin.TabularInline):
    model = Soal
    extra = 0
    fields = ['nomor_urut', 'pertanyaan', 'referensi_jawaban', 'kata_kunci']


@admin.register(Ujian)
class UjianAdmin(admin.ModelAdmin):
    list_display = ['judul', 'mata_pelajaran', 'kelas_target', 'status', 'durasi_menit', 'tanggal_ujian']
    list_filter = ['status', 'mata_pelajaran']
    search_fields = ['judul']
    inlines = [SoalInline]


@admin.register(Soal)
class SoalAdmin(admin.ModelAdmin):
    list_display = ['ujian', 'nomor_urut', 'pertanyaan']
    list_filter = ['ujian']
