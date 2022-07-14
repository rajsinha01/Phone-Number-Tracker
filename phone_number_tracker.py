import phonenumbers as ph
from phonenumbers import timezone,geocoder,carrier
number = input("Enter Phone number with +_ _ : ")
phone=ph.parse(number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,'en')
reg=geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(carr)
print(reg)