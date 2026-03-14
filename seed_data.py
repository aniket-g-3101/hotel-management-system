import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_project.settings')
django.setup()

from django.contrib.auth.models import User
from hotel_app.models import City, Hotel, Room

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@luxstay.com', 'admin123')
    print("✅ Superuser created: admin / admin123")

if not User.objects.filter(username='user1').exists():
    User.objects.create_user('user1', 'user1@example.com', 'user1234')
    print("✅ Test user created: user1 / user1234")

# Cities
cities_data = [
    {"name": "Mumbai", "state": "Maharashtra", "image_url": "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=800&q=80"},
    {"name": "Delhi", "state": "Delhi", "image_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&q=80"},
    {"name": "Bangalore", "state": "Karnataka", "image_url": "https://images.unsplash.com/photo-1595658658481-d53d3f999875?w=800&q=80"},
    {"name": "Goa", "state": "Goa", "image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&q=80"},
    {"name": "Jaipur", "state": "Rajasthan", "image_url": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800&q=80"},
    {"name": "Chennai", "state": "Tamil Nadu", "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800&q=80"},
]

cities = {}
for c in cities_data:
    obj, created = City.objects.get_or_create(name=c['name'], defaults=c)
    cities[c['name']] = obj
    if created:
        print(f"✅ City: {c['name']}")

# Hotels data
hotels_data = [
    # Mumbai
    {
        "city": "Mumbai",
        "name": "The Taj Mahal Palace",
        "description": "An iconic landmark standing tall at the Gateway of India since 1903. This legendary property blends Moorish, Oriental and Florentine architectural styles with impeccable Indian hospitality.",
        "address": "Apollo Bunder, Colaba, Mumbai 400001",
        "stars": 5, "price_per_night": 18500,
        "amenities": "WiFi, Pool, Spa, Gym, Restaurant, Bar, Concierge, Valet Parking",
        "image_url_1": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&q=80",
        "image_url_3": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800&q=80",
    },
    {
        "city": "Mumbai",
        "name": "Marine Drive Boutique Hotel",
        "description": "Nestled along the famous Queen's Necklace, this sleek boutique hotel offers breathtaking views of the Arabian Sea and contemporary luxury in the heart of South Mumbai.",
        "address": "Marine Drive, Nariman Point, Mumbai 400020",
        "stars": 4, "price_per_night": 8500,
        "amenities": "WiFi, Sea View, Restaurant, Bar, Room Service",
        "image_url_1": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&q=80",
        "image_url_3": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&q=80",
    },
    {
        "city": "Mumbai",
        "name": "Bandra Grand",
        "description": "A contemporary urban hotel in the posh Bandra West neighbourhood, surrounded by Mumbai's finest restaurants, cafes, and nightlife. Perfect for the modern business and leisure traveller.",
        "address": "Hill Road, Bandra West, Mumbai 400050",
        "stars": 4, "price_per_night": 6200,
        "amenities": "WiFi, Gym, Rooftop Bar, Restaurant, Business Centre",
        "image_url_1": "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800&q=80",
        "image_url_3": "",
    },

    # Delhi
    {
        "city": "Delhi",
        "name": "Imperial New Delhi",
        "description": "A colonial-era masterpiece on Janpath, The Imperial is Delhi's most prestigious address. With an unrivalled art collection and legendary service, it defines luxury in the capital.",
        "address": "Janpath, New Delhi 110001",
        "stars": 5, "price_per_night": 21000,
        "amenities": "WiFi, Pool, Spa, Multiple Restaurants, Bar, Heritage Art Gallery, Gym",
        "image_url_1": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1596436889106-be35e843f974?w=800&q=80",
        "image_url_3": "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=800&q=80",
    },
    {
        "city": "Delhi",
        "name": "Connaught Residency",
        "description": "Ideally located in central Delhi near Connaught Place, this stylish hotel offers modern comforts with easy access to the city's business district, shopping, and historic monuments.",
        "address": "Connaught Place, New Delhi 110001",
        "stars": 4, "price_per_night": 7800,
        "amenities": "WiFi, Restaurant, Bar, Business Centre, Laundry",
        "image_url_1": "https://images.unsplash.com/photo-1455587734955-081b22074882?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1444201983204-c43cbd584d93?w=800&q=80",
        "image_url_3": "",
    },

    # Goa
    {
        "city": "Goa",
        "name": "Sunset Beach Resort",
        "description": "Wake up to the sound of waves at this stunning beachfront resort in North Goa. Featuring infinity pools, world-class dining, and direct beach access for an unforgettable tropical escape.",
        "address": "Calangute Beach Road, North Goa 403516",
        "stars": 5, "price_per_night": 14500,
        "amenities": "WiFi, Beachfront, Infinity Pool, Spa, Water Sports, Restaurant, Bar",
        "image_url_1": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?w=800&q=80",
        "image_url_3": "https://images.unsplash.com/photo-1540541338537-1220059f851e?w=800&q=80",
    },
    {
        "city": "Goa",
        "name": "Portuguese Heritage Inn",
        "description": "A charming boutique property in Old Goa, lovingly restored from a 16th-century Portuguese villa. Surrounded by spice gardens and heritage churches, it offers a serene slice of Goan history.",
        "address": "Old Goa Road, Panaji, Goa 403001",
        "stars": 3, "price_per_night": 3800,
        "amenities": "WiFi, Garden, Pool, Heritage Tour, Restaurant",
        "image_url_1": "https://images.unsplash.com/photo-1521782462922-9318be1cd176?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800&q=80",
        "image_url_3": "",
    },

    # Jaipur
    {
        "city": "Jaipur",
        "name": "Rambagh Palace",
        "description": "Once the residence of the Maharaja of Jaipur, Rambagh Palace is a regal retreat with sprawling Mughal gardens, ornate suites, and royal dining experiences in the Pink City.",
        "address": "Bhawani Singh Road, Jaipur 302005",
        "stars": 5, "price_per_night": 25000,
        "amenities": "WiFi, Pool, Spa, Heritage Garden, Multiple Restaurants, Royal Dining, Polo",
        "image_url_1": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800&q=80",
        "image_url_3": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80",
    },
    {
        "city": "Jaipur",
        "name": "Amer Haveli",
        "description": "A beautifully restored traditional haveli near the Amer Fort, offering an authentic Rajasthani experience with hand-painted frescoes, jharokha windows, and rooftop dining under the stars.",
        "address": "Near Amer Fort, Jaipur 302028",
        "stars": 4, "price_per_night": 6500,
        "amenities": "WiFi, Rooftop Restaurant, Heritage Tour, Courtyard, Cultural Shows",
        "image_url_1": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&q=80",
        "image_url_3": "",
    },

    # Bangalore
    {
        "city": "Bangalore",
        "name": "The Leela Palace Bangalore",
        "description": "A magnificent Dravidian-inspired palace in the heart of Silicon Valley. With soaring ceilings, gold-leaf detailing, and lush gardens, it delivers a palatial experience to tech executives and leisure travellers alike.",
        "address": "23 HAL Airport Road, Bangalore 560008",
        "stars": 5, "price_per_night": 16000,
        "amenities": "WiFi, Pool, Spa, Gym, Multiple Restaurants, Bar, Concierge",
        "image_url_1": "https://images.unsplash.com/photo-1600011689032-8b628b8a8747?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1595658658481-d53d3f999875?w=800&q=80",
        "image_url_3": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=800&q=80",
    },
    {
        "city": "Bangalore",
        "name": "Indiranagar Stay",
        "description": "A modern, design-forward hotel in the trendy Indiranagar neighbourhood, steps from Bangalore's hippest cafes, craft breweries, and boutique shops. Ideal for digital nomads and weekend getaways.",
        "address": "100 Feet Road, Indiranagar, Bangalore 560038",
        "stars": 3, "price_per_night": 3200,
        "amenities": "WiFi, Café, Co-working Space, Gym, Rooftop",
        "image_url_1": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200&q=80",
        "image_url_2": "",
        "image_url_3": "",
    },

    # Chennai
    {
        "city": "Chennai",
        "name": "ITC Grand Chola",
        "description": "Inspired by the grandeur of the Chola dynasty, this architectural marvel in Chennai is one of Asia's largest hotels. With 15 dining options, a spectacular spa and opulent rooms, it's a destination unto itself.",
        "address": "Mount Road, Guindy, Chennai 600032",
        "stars": 5, "price_per_night": 13500,
        "amenities": "WiFi, Pool, Spa, 15 Restaurants, Bar, Gym, Convention Centre",
        "image_url_1": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=1200&q=80",
        "image_url_2": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&q=80",
        "image_url_3": "",
    },
]

hotel_objs = {}
for h in hotels_data:
    city = cities[h.pop("city")]
    obj, created = Hotel.objects.get_or_create(name=h['name'], city=city, defaults={**h, "city": city})
    hotel_objs[obj.name] = obj
    if created:
        print(f"✅ Hotel: {obj.name}")

# Rooms
room_types = [
    ("standard", 1, 0.8),
    ("deluxe", 2, 1.0),
    ("suite", 3, 1.5),
    ("penthouse", 4, 2.2),
]

for hotel in Hotel.objects.all():
    if hotel.rooms.count() == 0:
        for rtype, num, multiplier in room_types:
            for i in range(1, 4):
                room_num = f"{num}{i:02d}"
                price = round(float(hotel.price_per_night) * multiplier, -2)
                Room.objects.create(
                    hotel=hotel,
                    room_type=rtype,
                    room_number=room_num,
                    price_per_night=price,
                    capacity=2 if rtype in ['standard', 'deluxe'] else 4,
                    is_available=True,
                    description=f"Comfortable {rtype} room with modern amenities."
                )
        print(f"✅ Rooms created for: {hotel.name}")

print("\n🎉 Seed data loaded successfully!")
print("─" * 40)
print("Admin: http://127.0.0.1:8000/admin/")
print("  Username: admin | Password: admin123")
print("Test User: user1 | Password: user1234")
print("─" * 40)
