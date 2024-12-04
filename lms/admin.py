from django.contrib import admin

from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'preview')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'description', 'preview', 'video')
    search_fields = ('title', 'description', 'course')
    list_filter = ('title', 'description', 'course')