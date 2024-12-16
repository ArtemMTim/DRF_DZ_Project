from django.contrib import admin

from .models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "preview", "owner")
    search_fields = ("title", "description", "owner")
    list_filter = ("title", "description", "owner")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course", "description", "preview", "video", "owner")
    search_fields = ("title", "description", "course", "owner")
    list_filter = ("title", "description", "course", "owner")

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user', 'course')
    list_filter = ('user', 'course')