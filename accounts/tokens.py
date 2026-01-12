##WE WILL LEARN HOW TO GENERATE TOKENS MAUALLY
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User  = get_user_model()

def create_jwt_pair_for_user(User):
    refresh  = RefreshToken.for_user(User)

    tokens = {
        "access" : str(refresh.access_token),
        "refresh" : str(refresh)
    }

    return tokens