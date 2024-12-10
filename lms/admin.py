from django.contrib import admin

from .models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "preview", "owner")
    search_fields = ("title", "description", "owner")
    list_filter = ("title", "description", "owner")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "description", "preview", "video", "owner")
    search_fields = ("title", "description", "course", "owner")
    list_filter = ("title", "description", "course", "owner")
