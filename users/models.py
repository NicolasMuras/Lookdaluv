import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from simple_history.models import HistoricalRecords



class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have a username.')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "profile_images/default_profile_photo.png"


class User(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(
        max_length=255, 
        upload_to=get_profile_image_filepath, 
        null=True, 
        blank=True, 
        default=get_default_profile_image
        )
    hide_email = models.BooleanField(default=True)

    historical = HistoricalRecords()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/')]

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='profile')

    name = models.CharField(max_length=30, unique=False, null=False, blank=False)
    last_name = models.CharField(max_length=30, unique=False, null=False, blank=False)
    age = models.DateField(default=datetime.date.today)
    nationality = models.CharField(max_length=30, unique=False, null=False, blank=False)
    subscription_end_date = models.DateField(default=datetime.date.today)
    level = models.IntegerField(default=1)

    class Language(models.IntegerChoices):

        ES_ES                   = 1, "es-es"
        EN_US                   = 2, "en-us"


    language = models.PositiveSmallIntegerField(
        'Language', 
        choices=Language.choices,
        default=Language.ES_ES
    )

    class Rank(models.IntegerChoices):

        SIMPL                   = 1, "SIMPL"
        SEDUCER                 = 2, "Seducer"
        KAIZEN_MIND             = 3, "Kaizen Mind"
        CASANOVA                = 4, "Casanova"
        AVEN                    = 5, "Aven"

    rank = models.PositiveSmallIntegerField(
        'Rank', 
        choices=Rank.choices,
        default=Rank.SIMPL
    )

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.__str__()


class ProfileStatistics(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', related_name='profilestatistics')

    personal_growth_completed = models.IntegerField()
    chatbot_completed = models.IntegerField()
    simpl_deconstructor_completed = models.IntegerField()
    date_simulation_completed = models.IntegerField()
    sex_arts_completed = models.IntegerField()
    environment_dominance_completed = models.IntegerField()

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Profile Statistic'
        verbose_name_plural = 'Profiles Statistics'