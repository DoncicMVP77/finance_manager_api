from django.contrib.auth import get_user_model

User = get_user_model()

def print_user(user):
    print(user)
    return user

print(type(map(print_user, User.objects.all())))
