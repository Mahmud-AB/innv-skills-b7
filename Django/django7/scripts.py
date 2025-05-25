# from app1.models import Profile
# from django.contrib.auth.models import User
## CRUD 
## Create, Read, Update, Delete
## Create
# user = User.objects.create(username='testuser', password='password123',first_name='Test', last_name='User',)
# print("User created:", user)
# obj = Profile(
#     user=user,
#     phone='1234567890',
#     address='123 Test St, Test City, TC 12345',
# )
# obj.save()
# print("Profile created successfully")

#Read
# all_profile = Profile.objects.all()
# print("All profiles:", all_profile)
# for profile in all_profile:
#     pic = profile.profile_pic.url if profile.profile_pic else None
#     print("Profile:", profile.user.username,profile.full_name, profile.phone, profile.address,pic)

# profile = Profile.objects.get(id=2,user__username='testuser')
# print("Profile single:",profile.user.username)

# profile = Profile.objects.filter(user__username='testuser')
# print("Profile filter:",profile)
# print(Profile.objects.filter(user__username='testuser').exists())

# profile = Profile.objects.exclude(user__username='testuser')
# print("Profile exclude:",profile)

# Field lookup
# i -> insensitive -> capital,small,upper,lower - X
# exact,contains,iexact,icontains,gt/gte/lt/lte(time,date,calculation),range,startwith

#update
# profile = Profile.objects.get(id=1)
# profile.phone = '9876543210'
# profile.save()

# profile = Profile.objects.get(id=2)
# profile.user.first_name = 'UpdatedFirstName'
# profile.user.save()

# profile.objects.filter(user__username='testuser').update(phone='1111111111')

#delete
# profile = Profile.objects.get(id=1)
# profile.delete()
# print("Profile deleted successfully")

# Profile.objects.filter(user__username='testuser').delete()


