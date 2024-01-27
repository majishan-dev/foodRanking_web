from django.db import models


# Create your models here.
class RankingModel(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_location = models.CharField(max_length=100)
    shop_image = models.ImageField(upload_to="images/")
    buisiness_hours = models.CharField(max_length=100)
    created_data = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    # shop_type_id = models.CharField(max_length=10, blank=True, null=True) #後で外部キーに変更
    # 例models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.shop_name
