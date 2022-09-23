# Scale-Real-Task
Pizza Topping related task

# creating-a-rest-api-with-django

## Instructions to run this project locally:  
  
1. Go to `shopping_cart`:    
  
```console   
$ cd shopping_cart   
```   
    
2. Install requirements:  
  
```console  
$ pip install -r requirements.txt  
```  
  
3. Set up DB:   
   
```console  
$ python manage.py makemigrations   
$ python manage.py migrate   
```  
   
4. Run the app:   
  
```console   
$ python manage.py runserver  
```   

5. Working endpoints:
'''
$ http://127.0.0.1:8000/api/pizza/bases/

$ http://127.0.0.1:8000/api/pizza/toppings/

$ http://127.0.0.1:8000/api/orders/

$ http://127.0.0.1:8000/api/orders/10
'''

6. Additional:
'''
$ For additional testing of POST & GET methods postman collection is also added in the github repo
$ Please do refer
'''