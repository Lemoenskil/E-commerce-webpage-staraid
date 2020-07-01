from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class CaseInsensitiveAuth:
    """
    Authenticate a of User by using a case-insensitive query to check a
    combination of the supplied email/username and password.
    To avoid the risk of having two users with similar usernames,
    distinguished only by letter case (e.g. 'john' and 'John'), consider
    updating your User model to save usernames as lower case entries to
    the database.
    This will ensure all usernames have unique spellings, and as a result,
    our case insensitive query will return a single result only.
    """
    def authenticate(self, username_or_email=None, password=None):
        """
        Get an instance of User using the supplied username
        or email (case insensitive) and verify the password
        """
        # Filter all users by searching for a match by username/ email.
        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))
        if not users:
            return None

        # Then get the first result of the query (which is your user).
        user = users[0]
        # If the password is correct, return user object
        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        """
        Used by the Django authentication system to retrieve a User instance
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(verbose_name="birth date")
    full_name = models.CharField(verbose_name="full name", max_length=50, blank=False)
    phone_number = models.CharField(verbose_name="phone number", max_length=20, blank=False)
    country = models.CharField(verbose_name="country", max_length=40, blank=False)
    postcode = models.CharField(verbose_name="postcode", max_length=20, blank=True)
    town_or_city = models.CharField(verbose_name="town or city", max_length=40, blank=False)
    street_address1 = models.CharField(verbose_name="street address 1", max_length=40, blank=False)
    street_address2 = models.CharField(verbose_name="street address 2", max_length=40, blank=False)
