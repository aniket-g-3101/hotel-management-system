from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='user_login'),
    path('register/', views.register_view, name='user_register'),
    path('logout/', views.logout_view, name='user_logout'),
    path('cities/', views.cities_view, name='cities'),
    path('hotels/city/<int:city_id>/', views.hotels_by_city, name='hotels_by_city'),
    path('hotels/city/<str:city_name>/', views.hotels_by_city_name, name='hotels_by_city_name'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
