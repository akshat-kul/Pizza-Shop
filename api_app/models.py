from django.db import models

class PizzaItem(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ToppingItem(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    base = models.ForeignKey(PizzaItem, related_name="base_id", on_delete=models.CASCADE)
    toppings = models.ManyToManyField(ToppingItem, related_name="toppings")
    
    def __str__(self):
        return self.base
