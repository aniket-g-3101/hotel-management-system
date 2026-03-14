from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True, help_text="Unsplash image URL for city")

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def __str__(self):
        return self.name


class Hotel(models.Model):
    STAR_CHOICES = [(i, f'{i} Star') for i in range(1, 6)]

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=300)
    stars = models.IntegerField(choices=STAR_CHOICES, default=3)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    amenities = models.CharField(max_length=500, help_text="Comma separated: WiFi, Pool, Gym")
    is_available = models.BooleanField(default=True)
    image_url_1 = models.URLField(blank=True)
    image_url_2 = models.URLField(blank=True)
    image_url_3 = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    def get_amenities_list(self):
        return [a.strip() for a in self.amenities.split(',') if a.strip()]

    def get_images(self):
        images = []
        for url in [self.image_url_1, self.image_url_2, self.image_url_3]:
            if url:
                images.append(url)
        return images


class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
        ('penthouse', 'Penthouse'),
    ]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    room_number = models.CharField(max_length=10)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField(default=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.hotel.name}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room} ({self.check_in})"
