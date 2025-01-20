from App import user_registered,db
from .models import UserProgress

def create_user_profile(sender, **kwargs):
    user = kwargs.get('user')
    if user:
        profile = UserProgress(user_id=user.id)
        db.session.add(profile)
        db.session.commit()

# Connect the signal to the profile creation function
user_registered.connect(create_user_profile)