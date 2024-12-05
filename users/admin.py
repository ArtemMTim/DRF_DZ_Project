from django.contrib import admin

from .models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "city",
        "avatar",
    )
    search_fields = ("email", "first_name", "last_name", "phone_number")
    list_filter = ("email", "first_name", "last_name", "phone_number")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payment_date",
        "course",
        "lesson",
        "amount",
        "payment_method",
    )
    search_fields = ("user", "payment_date", "course", "lesson")
    list_filter = (
        "user",
        "payment_date",
        "course",
        "lesson",
        "amount",
        "payment_method",
    )
