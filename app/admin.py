from django.contrib import admin
from app.models import Product, RepairProduct, RejectedProduct, DailyInventory, InHandStock, ProductTracking

# Register your models here.
class ProductData(admin.ModelAdmin):
    list_display = ('product_id', 'product_name','product_quantity','product_status','created_at')
admin.site.register(Product, ProductData)

class RepairProductData(admin.ModelAdmin):
    list_display = ('rp_id', 'product','product_quantity','date_started','date_finished','rp_status','created_at')
admin.site.register(RepairProduct, RepairProductData)

class RejectedProductData(admin.ModelAdmin):
    list_display = ('rj_id', 'product','reason','created_at')
admin.site.register(RejectedProduct, RejectedProductData)

class DailyInventoryData(admin.ModelAdmin):
    list_display = ('di_id', 'date','product','quantity','status','created_at')
admin.site.register(DailyInventory, DailyInventoryData)

class InHandStockData(admin.ModelAdmin):
    list_display = ('ihs_id', 'product','quantity','product_type','created_at')
admin.site.register(InHandStock, InHandStockData)

class ProductTrackingData(admin.ModelAdmin):
    list_display = ('pt_id', 'product','quantity','event_date','status','created_at')
admin.site.register(ProductTracking, ProductTrackingData)
