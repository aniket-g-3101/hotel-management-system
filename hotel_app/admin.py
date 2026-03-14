from django.contrib import admin
from .models import City, Hotel, Room, Booking


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    search_fields = ['name']


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'stars', 'price_per_night', 'is_available']
    list_filter = ['city', 'stars', 'is_available']
    search_fields = ['name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'hotel', 'room_type', 'price_per_night', 'is_available']
    list_filter = ['hotel', 'room_type', 'is_available']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'check_in', 'check_out', 'status', 'total_price']
    list_filter = ['status']
