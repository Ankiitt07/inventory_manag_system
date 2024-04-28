from django.db import models
from django.utils import timezone


# Create your models here.

def default_special_date():
    return timezone.datetime(1, 1, 1)

status_choice = [
    (0, 'Inactive'),
    (1, 'Active'),
]

inventory_status_choice = [
    (1, 'Packed'),
    (2, 'Dispatched'),
    (3, 'Repaired'),
    (4, 'Returned')
]

product_status_choice = [
    (1, 'Inprocess'),
    (2, 'Repaired'),
    (3, 'Dispatched'),
]



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_quantity = models.IntegerField(default=0)
    product_status = models.IntegerField(
        choices=status_choice,
        default=1
    )
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(default="0")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default="0")
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(default="0")

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'product_table'
        managed = True

class DailyInventory(models.Model):
    di_id = models.AutoField(primary_key=True)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    status = models.IntegerField(
        choices=inventory_status_choice,
        default=1
    )
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(default="0")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default="0")
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(default="0")


    def __str__(self):
        return str(self.date)
    
    class Meta:
        db_table = 'daily_inventory_table'
        managed = True


class RepairProduct(models.Model):
    rp_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=0)
    date_started = models.CharField(max_length=200, blank=True, null=True)
    date_finished = models.CharField(max_length=200, blank=True, null=True)
    rp_status = models.IntegerField(
        choices=product_status_choice,
        default=1
    )
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(default="0")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default="0")
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(default="0")


    def __str__(self):
        return str(self.rp_id)
    
    class Meta:
        db_table = 'repair_product_table'
        managed = True


class RejectedProduct(models.Model):
    rj_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(default="0")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default="0")
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(default="0")


    def __str__(self):
        return str(self.rj_id)
    
    class Meta:
        db_table = 'rejected_product_table'
        managed = True


class InHandStock(models.Model):
    ihs_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_type = models.CharField(max_length=200, blank=True, null=True) # product type can be raw, packaged or dispatched
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(default="0")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default="0")
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(default="0")


    def __str__(self):
        return str(self.ihs_id)
    
    class Meta:
        db_table = 'inhand_stock_table'
        managed = True

class ProductTracking(models.Model):
    pt_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    event_date = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(
        choices=inventory_status_choice,
        default=1
    )
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(default="0")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default="0")
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.IntegerField(default="0")


    def __str__(self):
        return str(self.pt_id)
    
    class Meta:
        db_table = 'product_tracking_table'
        managed = True
