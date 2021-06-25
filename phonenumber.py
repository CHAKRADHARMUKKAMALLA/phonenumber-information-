import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phone_number = phonenumbers.parse("ENTER YOUR MOBILE NUMBER")
timeZone = timezone.time_zones_for_number(phone_number)

carrier = carrier.name_for_number(phone_number, 'en')

region = geocoder.description_for_number(phone_number, 'en')

print(phone_number)
print(timeZone)
print(carrier)
print(region)
