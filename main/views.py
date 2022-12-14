from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def BaseView(request):
    return render(request, 'main/base.html', {'Customer':Customer})







def RegisterCustomerView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            Customer.objects.create(user=request.user, first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), phone=request.POST.get('phone'), email=request.POST.get('email'))
            messages.warning(request, "Your profile has been created succcessfully")        
        else:
            form = CustomerForm()
        return render(request, 'main/customer-create.html', {'form':form, 'customer':False})
    else:
        return redirect('/login')






def UpdateCustomerView(request):
    if request.user.is_authenticated:
        try:
            customer = get_object_or_404(Customer, user = request.user)
            form = CustomerForm(request.POST or None, instance=customer)
            if request.method == 'POST':
                customer.first_name = request.POST.get('first_name')
                customer.last_name=request.POST.get('last_name')
                customer.phone=request.POST.get('phone')
                customer.email=request.POST.get('email')
                return redirect('/')
            return render(request, 'main/customer-create.html', {'form':form, 'customer':customer})
        except:
            form = CustomerForm(request.POST or None)
            return render(request, 'main/customer-create.html', {'form':form, 'customer':False})
    else:
        return redirect('/login')






def listAll(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('cart-add-button'):
            if request.user.is_authenticated:

                # getting the particular product and the particular cart to which a cartitem will be tied to
                id_ = int(request.POST.get('cart-add-button')[0])
                product = Product.objects.get(id = id_)
                product.in_a_cart = True
                product.save()
                cart = get_object_or_404(Cart, user=request.user)

                # check is there is already a cartitem that links the product and the cart and add to the amount of the cartitem 
                try:
                    cartitem = CartItem.objects.filter(cart=cart, product=product)[0]
                    cartitem.amount = cartitem.amount + 1
                    cartitem.save()
                    messages.warning(request, f"Successfully added {product.name} to cart :-)") 
                    print('adding to a previous cartitem')

                # if not, create a new cartitem that will link the product and the cart
                except :
                    cartitem = CartItem.objects.create(product=product, cart=cart)
                    print('creating a new cartitem')
                product.amount_in_carts += 1
                product.inventory -= 1
                product.save()

            else:
                return redirect('/login')

    categories = Category.objects.all()
    
    return render(request, 'main/product-list.html', {'products':Product.objects.all(), 'categories':categories})






def listCategory(request, category):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('cart-add-button'):
            if request.user.is_authenticated:
                id_ = int(request.POST.get('cart-add-button')[0])
                product = Product.objects.get(id = id_)
                product.in_a_cart = True
                product.save()
                cart = get_object_or_404(Cart, user=request.user)
                try:
                    cartitem = CartItem.objects.filter(cart=cart, product=product)[0]
                    cartitem.amount = cartitem.amount + 1
                    cartitem.save()
                    print('adding to a previous cartitem')
                except :
                    cartitem = CartItem.objects.create(product=product, cart=cart)
                    print('creating a new cartitem')
                product.amount_in_carts += 1
                product.inventory -= 1
                product.save()
               
            else:
                return redirect('/login')

    categories = Category.objects.all()
    return render(request, 'main/product-list.html', {'products':Product.objects.filter(category__name=category), 'categories':categories})







def CartView(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        return render(request, 'main/cart-view.html', {'cart_items':cart.items.all()})
    return redirect('/login')




#---------------------------- Unused Code ------------------------------#

"""
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES) 
        print(form) 
        if form.is_valid():
            form.save()
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'main/img-upload.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'main/img-upload.html', {'form': form})  
def SellerCreateView2(request):
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Getting the current instance object to display in the template  
            seller_object = form.instance  
            return render(request, 'main/seller-create.html', {'form': form, 'seller_obj': seller_object})  
    else:  
        form = SellerForm()  
  
    return render(request, 'main/seller-create.html', {'form': form})
def SellerUpdateView2(request):
    obj = get_object_or_404(Seller, id=1)
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SellerForm()
    return render(request, 'seller-update.html', {'form':form})
class SellerCreateView(CreateView):
    form_class = SellerForm
    template_name = 'main/seller-create.html'
    queryset = Seller.objects.all()
    success_url = '/'
    def form_valid(self,form):
        return super().form_valid(form)
class SellerUpdateView(UpdateView):
    form_class = SellerForm
    template_name = 'main/seller-create.html'
    queryset = Seller.objects.all()
    success_url = '/'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Seller, id=id_)
    def form_valid(self,form):
        return super().form_valid(form)
class AllProductView(ListView):
    template_name = 'main/product-list.html'
    queryset = Product.objects.all
    def post(self, request):
        print(request.POST)
class RegisterCustomer(CreateView):
    form_class = CustomerForm
    template_name = 'main/customer-create.html'
    success_url = '/'
    def form_valid(self, form):
        return super().form_valid(form)
def ProductDetailView(request, id):
    product_obj = Product.objects.get(id=id)
    return render(request, 'product-detail.html', {'product':product_obj})
"""
