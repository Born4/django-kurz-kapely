"""
Knihovna pro pristup a manipulaci s Modely
"""
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def check_object_duplicity(model, **kwargs):
    """
    Otestujeme duplicvitu objektu daneho mopdelu pomoci perednaych parametry kwargs
    ktere odpovidaji paerametrum napr. pri vy5vareni nove instance modelu

    params = {
        "name": "Moravnka",
        "year": 1950,
        }
    Band.objects.filter(**params)
    """
    duplicity = False
    try:
        duplicity = model.objects.get(**kwargs)
    except MultipleObjectsReturned as e:
        # logger
        print("Nekolikanasobna duplicita!!!")
        duplicity = True
    except ObjectDoesNotExist:
        pass
    return duplicity
