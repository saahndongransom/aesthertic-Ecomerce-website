# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, Category
from django.contrib.sessions.models import Session
from .models import Notification
import paypalrestsdk
from django.conf import settings
from .models import FAQ
from .forms import FAQForm
from django.shortcuts import render, redirect
from .models import FAQ
from .forms import FAQForm


from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Subscription
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse



from django.shortcuts import render
from .models import Product, Category, Notification

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:3]
    
    
    notifications = Notification.objects.all()
    notification_count = Notification.objects.count()

    context = {
        'categories': categories,
        'products': products,
        'notifications': notifications,  
        'notification_count': notification_count  
    }
    
    return render(request, "index.html", context)

def about(request):
    
    notifications = Notification.objects.all()
    notification_count = Notification.objects.count()

    context = {
      
        'notifications': notifications,  
        'notification_count': notification_count  
    }
    return render(request, 'about.html',context)

def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
       

    return render(request, 'contact.html')

def shop(request):
  
    unread_notifications_count = request.session.get('unread_notifications_count', 0)

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products, 'unread_notifications_count': unread_notifications_count}
        
    notifications = Notification.objects.all()
    notification_count = Notification.objects.count()

    context = {
        'categories': categories,
        'products': products,
        'notifications': notifications, 
        'notification_count': notification_count  
    }
    return render(request, 'shop.html', context)

def shop_single(request):
    return render(request, 'shop-single.html')

def simulate_notification(request):
   
    unread_notifications_count = request.session.get('unread_notifications_count', 0)
    request.session['unread_notifications_count'] = unread_notifications_count + 1
    return JsonResponse({'success': True})

def notifications(request):
    notifications = Notification.objects.all()
    notification_count = Notification.objects.count()

    context = {
      
        
        'notification_count': notification_count  
    }
    return render(request, 'notifications.html', {'notifications': notifications,'notification_count': notification_count})





def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

       
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email, 
            ['saahndongransom@gmail.com'],  
            fail_silently=False,
        )

        return render(request, 'success_page.html', {'message': 'Email sent successfully!'})
            
    notifications = Notification.objects.all()
    notification_count = Notification.objects.count()

    context = {
        
        'notifications': notifications,  
        'notification_count': notification_count  
    }

    return render(request, 'contact.html',context)

def success_page(request):
    return render(request, 'success_page.html')



def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    grouped_related_products = [related_products[i:i+3] for i in range(0, len(related_products), 3)]
    return render(request, 'shop-single.html', {'product': product, 'related_products': related_products,'grouped_related_products': grouped_related_products})

def products_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {'categories': categories, 'products': products, 'selected_category': category}
    return render(request, 'shop.html', context)



def paypal_process_payment(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        amount = request.POST.get('amount')
  
        paypalrestsdk.configure({
            "mode": "sandbox",  # Change to "live" for production
             "client_id": settings.PAYPAL_CLIENT_ID,
            "client_secret": settings.PAYPAL_CLIENT_SECRET
            
        })
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": amount,
                    "currency": "USD"
                },
                "description": "Payment for product ID: {}".format(product_id)
            }],
            "redirect_urls": {
               "return_url": "http://localhost:8000/return/",
               "cancel_url": "http://localhost:8000/cancel/"
            }
        })

        if payment.create():
            approval_url = payment.links[1].href  
            return JsonResponse({'approval_url': approval_url})
        else:
            return JsonResponse({'error': payment.error})

    return JsonResponse({'error': 'Invalid request method'})

def return_page(request):
    return render(request, 'return.html')

def cancel_page(request):
    return render(request, 'cancel.html')

def paypal_checkout(request):
   
    approval_url = "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-5SU861680K660312P"
    return redirect(approval_url)


def faq(request):
    faqs = FAQ.objects.all()
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')  
    else:
        form = FAQForm()
    return render(request, 'faq.html', {'faqs': faqs, 'form': form})

def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')
    else:
        form = FAQForm()
    return render(request, 'add_faq.html', {'form': form})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscription

@csrf_exempt
def subscribe(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        email = request.POST.get('email')
        if email:
            
            subscription, created = Subscription.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'message': 'Subscribed successfully!'})
            else:
                return JsonResponse({'error': 'Email already subscribed'}, status=400)
        else:
            return JsonResponse({'error': 'Email is required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def send_message_page(request):
    return render(request, 'send_message.html')

@csrf_exempt
def send_message_to_all(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if subject and message:
            subscribers = Subscription.objects.all()
            email_list = [subscriber.email for subscriber in subscribers]
            send_mail(subject, message, 'saahndongransom@gmail.com', email_list)
            return JsonResponse({'message': 'Messages sent successfully!'})
        else:
            return JsonResponse({'error': 'Subject and message are required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

