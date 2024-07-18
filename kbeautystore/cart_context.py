from .models import CartItem

def cart_items(request):
    cart_items = []
    if request.user.is_authenticated:
        # Retrieve cart items for the logged-in user
        cart_items = CartItem.objects.filter(user=request.user)
    return {'cart_items': cart_items}
