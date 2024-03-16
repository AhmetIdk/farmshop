from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from farmshop.settings import MEDIA_URL, STATIC_URL, DEFAULTS

# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'))
    
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children',
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length= 50)
    description = models.TextField(blank=True, max_length=250)
    image = models.ImageField(upload_to='images/', blank=True, default=DEFAULTS["category_image"])
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(max_length=255, unique=True, null= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path)
    
    def image_tag(self):    
        return mark_safe(f'<img src="{self.image.url}" height="50" />') 
            
    image_tag.short_description = 'Image'
    
# ürün 
class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'))
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)  # manytoonerelationwithCategory
    title = models.CharField(max_length=150)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    main_image = models.ImageField(blank=True, upload_to='images/', default=DEFAULTS["product_image"])
    price = models.FloatField()
    detail=RichTextUploadingField()
    # price=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.main_image.url}" height="50"/>') 
        # images=Image.objects.filter(product_id__exact=self.pk).first() #image nesnelerinden bu producta ait olanları filtreler
        # return mark_safe(f'<img src="{MEDIA_URL}{images.values("image")[0]["image"]}" height="50"/>') #images değerlerinden image'leri alır, ilk sıradakini döndürür

    image_tag.short_description = 'Image'
    

    
# ÜrÜnler için resim galerisi 
class Image(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/', default=DEFAULTS["product_image"])
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
    
    def product_name(self):
        return self.product_id.title #resmin kayıtlı olduğu product nesnesinin ismini döndürür
    
    image_tag.short_description = 'Image'
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject