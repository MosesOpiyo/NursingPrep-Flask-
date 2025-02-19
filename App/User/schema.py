from App import mm
from .models import User

class ProfileSchema(mm.Schema):
    class Meta:
        model = User
        fields = ['username','email']