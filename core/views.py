from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def store(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'core/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    context = {'items': items, 'order': order}
    return render(request, 'core/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    context = {'items': items, 'order': order}
    return render(request, 'core/checkout.html', context)

def updateItem(request):
  data = json.loads(request.body)
  print("update start")
  productId = data['productId']
  action = data['action']
  quantity = data.get('quantity') #Test
  print('Action:', action)
  print('Product:', productId)
  print('Quantity:', quantity)

  customer = request.user.customer
  product = Product.objects.get(id=productId)
  order, created= Order.objects.get_or_create(customer=customer, complete=False)

  orderItem, created= OrderItem.objects.get_or_create(order=order, product=product)

  """
  if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
  elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
  """

  if action == 'add' and quantity is None:
    # Increment the quantity by 1 if no specific quantity is provided (add-to-cart button)
    orderItem.quantity += 1
  elif action == 'remove' and quantity is None:
    # Decrement the quantity by 1 if no specific quantity is provided (remove button)
    orderItem.quantity -= 1
  elif quantity is not None:
    orderItem.quantity = int(quantity)

  orderItem.save()

  if orderItem.quantity <= 0:
    orderItem.delete()

  return JsonResponse('Item was added', safe=False)

def confirm(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {'order': order}
    return render(request, 'core/confirm.html', context)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    return JsonResponse('Payment Submitted', safe=False)