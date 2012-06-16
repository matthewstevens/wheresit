from datetime import datetime
from django.db import models
from apps.profiles.models import Person

class Item(models.Model):
    """
    An item that is borrowable
    """
    item_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    meta_tags = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class BorrowedItem(models.Model):
    """
    An occurance of an item being borrowed
    """
    date_created = models.DateTimeField(default=datetime.now)
    borrower = models.ForeignKey(Person)
    owner = models.ForeignKey(Person, related_name='owner')
    item = models.ForeignKey(Item, related_name='item')
    def __str__(self):
        return "{0} borrowed {1} from {2}".format(self.borrower.name, self.item.name, self.owner.name)
