from django.db import models
from django.db.models import Q, Sum
from bands.utils.data_conversion import get_duration_string

SEZNAM_ZANRU = (
    (0, "Neznamy"),
    (1, "Classic"),
    (2, "Dechovka"),
    (3, "Pop"),
    (4, "Rock"),
    (5, "Heavy metal"),
)


class GetDataEngine:
    """Chceme aby kazdy Model mel nasledujici metody:
    get_data -> vrati data daneho modelu (vcetne provazanych modelu)
    print_data -> vytiskne data na konzoli a na uvod a zaver zobrazi "--------"
    save_data -> ulozi data nekam mimo Django
    """
    def get_data(self):
        """Vrati retezec reprezentujici data modelu"""
        return None

    def print_data(self):
        """"""
        print("--------------")
        print(self.get_data())
        print("--------------")

    def save_data(self):
        """Uklada data nekam"""
        pass


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        """Developer print data"""
        return self.name


class BandQuerySet(models.QuerySet):
    """"""
    def search(self, query):
        """Vyhledava rezetec query v datech modelu"""
        if query:
            query = query.strip()
            return self.filter(name__icontains=query)
        return self

    def aktivni(self):
        """"""
        return self.filter(still_active=True)


class BandManager(models.Manager):
    """"""
    def get_queryset(self):
        """"""
        return BandQuerySet(self.model, using=self._db)

    def search(self, query):
        """"""
        return self.get_queryset().search(query)


class Band(models.Model, GetDataEngine):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True, blank=True)
    still_active = models.BooleanField(default=False, blank=True)
    # genre = models.IntegerField(choices=SEZNAM_ZANRU, default=0, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)

    # Uprava Queryset
    objects = BandManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        """Developer print data"""
        return self.nice_name

    def __repr__(self):
        """Developer print data"""
        return f"{self.name} - {self.year} - ({self.pk})"

    def get_data(self):
        """"""
        return (f"Nazev: {self.name}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.get_genre_display()}\n"
                f"Still active: {'Ano' if self.still_active else 'Ne'}\n"
                f"PK: {self.pk}")

    @property
    def nice_name(self):
        """Nazev kapely (rok)"""
        return f"{self.name} ({self.year})"

    @property
    def full_name(self):
        """Nazev kapely (rok)"""
        return f"{self.name} * {self.year_string} * {self.genre}"

    @property
    def year_string(self):
        """Vrati rok nebo pomlcku"""
        if self.year:
            return self.year
        else:
            return "-"

    def zobraz_aktivitu(self):
        return "ano" if self.still_active else "ne"

    @property
    def roletove_menu_pojmenovani(self):
        """"""
        return f"{self.name} - ({self.genre}) - ({self.year_string})"


class Album(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    class Meta:
        ordering = ("band__name", "year")

    def __str__(self):
        """Developer print data"""
        return f"{self.name} - {self.year} - ({self.pk})"

    @property
    def nice_name(self):
        """Nazev kapely (rok)"""
        return f"{self.name} ({self.year})"

    @property
    def celkova_delka(self):
        """Vrati celkovou delku pisni na albu"""
        return self.song_set.secti_delky_seconds()

    @property
    def celkova_delka_string(self):
        """Vrati celkovou delku pisni na albu"""
        return self.song_set.all().secti_delky_string()


class SongQuerySet(models.QuerySet):
    """"""
    def search(self, query):
        """Vyhledava rezetec query v datech modelu"""
        if query:
            query = query.strip()
            return self.filter(name__icontains=query)
        return self

    def secti_delky_seconds(self):
        """"""
        return self.aggregate(total_length=Sum('duration'))['total_length']

    def secti_delky_string(self):
        """"""
        return get_duration_string(self.secti_delky_seconds())


class SongManager(models.Manager):
    """"""
    def get_queryset(self):
        """"""
        return SongQuerySet(self.model, using=self._db)

    def search(self, query):
        """"""
        return self.get_queryset().search(query)

    def secti_delky_seconds(self):
        """"""
        return self.secti_delky_seconds()

    def secti_delky_string(self):
        """"""
        return self.secti_delky_string()


class Song(models.Model):
    name = models.CharField(max_length=64)
    duration = models.IntegerField()  # delka skladby v sekundach
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    objects = SongManager()

    def __str__(self):
        """"""
        return f"{self.name}"

    def get_absolute_url(self):
        """"""
        pass

    def get_duration_str(self):
        """Vratit retezec duration ve tvaru mm:ss"""
        return get_duration_string(self.duration)


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        """"""
        return f"{self.last_name} {self.first_name}"
