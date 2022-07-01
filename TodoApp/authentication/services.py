import dataclasses
from datetime import datetime, timedelta
from hashlib import algorithms_available
from typing import TYPE_CHECKING
from .import models
import datetime
import jwt
from django.conf import settings


if TYPE_CHECKING:
    from .models import User

@dataclasses.dataclass
class UserDataClass:
    phone_number: int
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None




    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            phone_number= user.phone_number,
            first_name= user.first_name,
            last_name= user.last_name,
            email= user.email,
            id = user.id

        )



def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        phone_number=user_dc.phone_number,
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        email=user_dc.email
    )

    if user_dc.password is not None:
        instance.set_password(user_dc.password)

        instance.save()

        return UserDataClass.from_instance(instance)




def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user


def user_phone_selector(phone_number: int, ) -> "User":
    user = models.User.objects.filter(phone_number=phone_number).first()

    return user




def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET)

    return token
