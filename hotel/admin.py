from django.contrib import admin

# Register your models here.

from hotel.models import Room, Hotel


class HabitacionInline(admin.TabularInline):
    model = Room


class HotelAdmin(admin.ModelAdmin):
    inlines = [HabitacionInline]

admin.site.register(Hotel, HotelAdmin)
