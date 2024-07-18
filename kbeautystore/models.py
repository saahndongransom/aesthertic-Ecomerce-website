from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', default='default_images/default_category_image.jpg')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    comments_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    duration_field = models.DurationField(null=True, blank=True)
    

    def __str__(self):
        return self.name




from django.db import models

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)  # Allow answer to be blank initially

    def __str__(self):
        return self.question



from django.db import models

class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


