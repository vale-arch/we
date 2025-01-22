from models import db, User
import logging

logging.basicConfig(level=logging.INFO)

def create_user(email, profile_picture=None):
    try:
        new_user = User(email=email, profile_picture=profile_picture)
        db.session.add(new_user)
        db.session.commit()
        logging.info(f"User created with email: {email}")
    except Exception as e:
        logging.error(f"Error creating user with email {email}: {e}")

def get_user_by_email(email):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            return {
                'id': user.id,
                'email': user.email,
                'profile_picture': user.profile_picture
            }
        return None
    except Exception as e:
        logging.error(f"Error retrieving user with email {email}: {e}")
        return None

def update_user_profile_picture(email, profile_picture):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            user.profile_picture = profile_picture
            db.session.commit()
            logging.info(f"Updated profile picture for user with email: {email}")
            return True
        return False
    except Exception as e:
        logging.error(f"Error updating profile picture for user with email {email}: {e}")
        return False