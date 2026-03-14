from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from .models import City, Hotel, Room, Booking
from datetime import date


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'hotel_app/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text())
    return render(request, 'hotel_app/register.html')


def logout_view(request):
    logout(request)
    return redirect('user_login')


@login_required
def home_view(request):
    cities = City.objects.all()
    featured_hotels = Hotel.objects.filter(is_available=True, stars__gte=4)[:6]
    query = request.GET.get('city', '')
    if query:
        return redirect('hotels_by_city_name', city_name=query)
    return render(request, 'hotel_app/home.html', {
        'cities': cities,
        'featured_hotels': featured_hotels,
        'today': date.today(),
    })


@login_required
def cities_view(request):
    cities = City.objects.all()
    return render(request, 'hotel_app/cities.html', {'cities': cities})


@login_required
def hotels_by_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    hotels = Hotel.objects.filter(city=city, is_available=True)

    stars = request.GET.get('stars')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if stars:
        hotels = hotels.filter(stars=stars)
    if min_price:
        hotels = hotels.filter(price_per_night__gte=min_price)
    if max_price:
        hotels = hotels.filter(price_per_night__lte=max_price)

    return render(request, 'hotel_app/hotels_list.html', {
        'city': city,
        'hotels': hotels,
        'stars_filter': stars,
        'min_price': min_price,
        'max_price': max_price,
    })


@login_required
def hotels_by_city_name(request, city_name):
    city = get_object_or_404(City, name__iexact=city_name)
    return redirect('hotels_by_city', city_id=city.id)


@login_required
def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = hotel.rooms.filter(is_available=True)
    images = hotel.get_images()
    return render(request, 'hotel_app/hotel_detail.html', {
        'hotel': hotel,
        'rooms': rooms,
        'images': images,
        'today': date.today(),
    })


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = int(request.POST.get('guests', 1))

        from datetime import datetime
        ci = datetime.strptime(check_in, '%Y-%m-%d').date()
        co = datetime.strptime(check_out, '%Y-%m-%d').date()
        nights = (co - ci).days

        if nights <= 0:
            messages.error(request, 'Check-out must be after check-in.')
            return redirect('hotel_detail', hotel_id=room.hotel.id)

        total = room.price_per_night * nights
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            check_in=ci,
            check_out=co,
            guests=guests,
            total_price=total,
            status='confirmed'
        )
        room.is_available = False
        room.save()
        messages.success(request, f'Room booked successfully! Total: ₹{total}')
        return redirect('my_bookings')

    return render(request, 'hotel_app/book_room.html', {'room': room, 'today': date.today()})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('room__hotel').order_by('-created_at')
    return render(request, 'hotel_app/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'confirmed':
        booking.status = 'cancelled'
        booking.save()
        booking.room.is_available = True
        booking.room.save()
        messages.success(request, 'Booking cancelled successfully.')
    return redirect('my_bookings')
