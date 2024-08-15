from ninja import ModelSchema
from . models import CustomUser
from pydantic import BaseModel  # Added on - another difference with DRF


# # Schema is similar to form validation but with JSON for frontend. A checking mechanism looking for model fields data.
# class UserSchema(ModelSchema):
#     class Config:
#         model = CustomUser
#         model_fields = ['id', 'username', 'email']


class SignInSchema(BaseModel):
    email: str
    password: str
