# Django imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# external imports
from lib.utils.image.core import compress

from .managers import CustomUserManager

# app imports
from .mixins import DateTimeMixin


class User(DateTimeMixin, PermissionsMixin, AbstractBaseUser):
    """
    Customer model defines basic user attributes for login and signup
    """

    name = models.CharField(max_length=50, help_text=_("Name"))
    surname = models.CharField(max_length=50, help_text=_("Surname"))
    email = models.EmailField(_("User Email"), unique=True)
    is_active = models.BooleanField(
        _("Account Activation status"), default=True
    )
    is_frozen = models.BooleanField(_("Account frozen status"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    REQUIRED_FIELDS = ["name", "surname"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return self.name + " " + self.surname


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "users_pics/user_{0}/{1}".format(instance.user.id, filename)


class UserPic(DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.FileField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        default="default_pro_pic.jpeg",
    )
    thumb_picture = models.ImageField(blank=True)

    # calling image compression function before saving the data
    def save(self, *args, **kwargs):
        new_image = compress(self.picture)
        self.picture = new_image
        super().save(*args, **kwargs)


# @receiver(pre_save, sender=Customer)
# def activate_customer_account(sender, instance, **kwargs):
#     instance.is_active = True
