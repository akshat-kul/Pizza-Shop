from django.test import TestCase

from api_app.models import OrderItem, PizzaItem, ToppingItem


# Create your tests here.

class TestModel_PizzaBase(TestCase):
    def test_should_create_pizza_base(self):
        base = PizzaItem.objects.create(name="Double Cheese Burst")
        base.save()
        self.assertEqual(str(base), 'Double Cheese Burst')

class TestModel_Topping(TestCase):
    def test_should_create_topping(self):
        topping = ToppingItem.objects.create(name="Veggie Special")
        topping.save()
        self.assertEqual(str(topping), 'Veggie Special')

class TestModel_PizzaBase_Fail(TestCase):
    def test_should_not_create_pizza_base(self):
        base = PizzaItem.objects.create(name="Barley")
        base.save()
        self.assertNotEqual(str(base),"Thick Crust")

class TestModel_Topping_Fail(TestCase):
    def test_should_not_create_topping(self):
        base = PizzaItem.objects.create(name="Chilly")
        base.save()
        self.assertNotEqual(str(base),"Paneer")
