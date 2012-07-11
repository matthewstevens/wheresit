from datetime import datetime
from django.db import models
from apps.profiles.models import Person, Profile

class Item(models.Model):
    """
    An item that is borrowable
    """
    item_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    meta_tags = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class OwnedItem(models.Model):
    """
    An instance of an item owned by a person
    """
    item = models.ForeignKey(Item)
    user = models.ForeignKey(Profile)


class BorrowedItem(models.Model):
    """
    An occurance of an item being borrowed
    """
    date_created = models.DateTimeField(default=datetime.now)
    borrower = models.ForeignKey(Person)
    owner = models.ForeignKey(Person, related_name='owner')
    owned_item = models.ForeignKey(OwnedItem, related_name='owned_item')
    def __str__(self):
        return "{0} borrowed {1} from {2}".format(self.borrower.name, self.item.name, self.owner.name)
