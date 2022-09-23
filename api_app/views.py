#from django.shortcuts import render
from email.mime import base
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import OrderItem, ToppingItem, PizzaItem

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Home(View):
    def get(self, request):
        return JsonResponse("hello", status=200, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class PizzaCart(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))  
        pizza_id = data.get('id')
        pizza_name = data.get('name')

        product_data = {
            'id': pizza_id,
            'name': pizza_name,
        }

        cart_item = PizzaItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Pizza Base with id: {cart_item.id}"}
        return JsonResponse(data, status=200)

    def get(self, request):
        items_count = PizzaItem.objects.count() 
        items = PizzaItem.objects.values()
        print('------------------------PIZZA BASE GET REQUEST-------------------------')
        print("ITEMS ==>", items)

        items_data = list(items)
        return JsonResponse(items_data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ToppingCart(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))  
        id = data.get('id')
        name = data.get('name')

        product_data = {
            'id': id,
            'name': name,
        }

        cart_item = ToppingItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Toppings with id: {cart_item.id}"}
        return JsonResponse(data, status=200)

    def get(self, request):
        items = ToppingItem.objects.values() 
        print('------------------------TOPPING GET REQUEST-------------------------')
        print("ITEMS ==>", items)
        items_data = list(items)
        return JsonResponse(items_data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class OrderCart(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))  
        id = data.get('id')
        base_id = data.get('base_id')
        toppings = data.get('toppings')

        pizza_base = PizzaItem.objects.get(id=base_id)
        topping_items = ToppingItem.objects.filter(id__in=toppings)

        print(topping_items)
        topping_ids = [items.id for items in topping_items]
        print(topping_ids)

        product_data = {
            'id': id,
            'base_id': pizza_base.id,
        }
        order_item = OrderItem.objects.create(**product_data)
        print(product_data)
        order_item.toppings.set(topping_ids)
        order_item.save()

        data = { "message" : "Successfully Created" }
        return JsonResponse(data, status=200)

    def get(self, request, **args):
        if args == {}:
            items = OrderItem.objects.values()
            final_data = []
            
            for i in range(0,len(items)):
                topping_name = []
                base_name = PizzaItem.objects.filter(id = items[i]['base_id']).values()

                topping_id = OrderItem.toppings.through.objects.filter(orderitem_id = i+1).values()
                for j in range(0,len(topping_id)):
                    name = ToppingItem.objects.filter(id = topping_id[j]['toppingitem_id']).values()
                    topping_name.append(name[0]['name'])
                    
                final_data.append({'id':i+1, 'base_name': base_name[0]['name'], 'topping_name': topping_name})
            return JsonResponse(final_data, safe=False)

        else:
            item_data = list(OrderItem.objects.filter(id=args['order_id']).values())
            base_name = PizzaItem.objects.filter(id = item_data[0]['base_id']).values()
        

            topping_name = []
            topping_id = OrderItem.toppings.through.objects.filter(orderitem_id = args['order_id']).values()
            for i in range(0,len(topping_id)):
                name = ToppingItem.objects.filter(id = topping_id[i]['toppingitem_id']).values()
                topping_name.append(name[0]['name'])


            final_data = {'id': args['order_id'], 'base_name': base_name[0]['name'], 'topping_name': topping_name}
            return JsonResponse(final_data, safe=False)
