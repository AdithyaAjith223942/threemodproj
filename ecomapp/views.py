from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Cart, Product,Category, userdetails


def Home(request):
    return render(request, 'Home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff:  # Check if user is admin
                login(request, user)
                return redirect('adminpanel')
            elif user.is_active:  # Check if user is active
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('userpanel')
            else:
                messages.info(request, 'Your account is inactive!')
        else:
            messages.info(request, 'Invalid username or password!')

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pswd = request.POST['pass']
        email = request.POST['email']
        address= request.POST['addr']
        age = request.POST['age']
        cnum = request.POST['cnum']
        file = request.FILES.get('img')
        if User.objects.filter(username=uname).exists():
            messages.info(request, 'This username already exists!!!!!!')
            return redirect('signup')
        else:
            user = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=uname,
                password=pswd,
                email=email
                )
            user.save()

            reg= userdetails(
                address=address,
                user=user,
                number=cnum,
                usimg=file
            )
            reg.save()
        return redirect('signin')
    
            

    return render(request,'signup.html')


def smartwatches(request):
    return render(request, 'smartwatches.html')

def laptop(request):
    return render(request, 'laptop.html')

def desktops(request):
    return render(request, 'desktops.html')

def graphicscards(request):
    return render(request, 'graphicscards.html')

def buy(request):
    return render(request, 'buy.html')






def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')

        if Category.objects.filter(category_name=category_name).exists():
            messages.error(request, 'Category already exists.')
        else:
            Category.objects.create(category_name=category_name)
            messages.success(request, 'Category added successfully.')
            return redirect('adminpanel')

    return render(request, 'add_category.html')

def add_product(request):
     category=Category.objects.all()
     return render(request,'add_product.html',{'categories':category})

def adminpanel(request):
    product_count = Product.objects.all().count()
    user_count = User.objects.all().count()
    return render(request, 'adminpanel.html', {
        'product_count': product_count,
        'user_count': user_count,
    })

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})

def view_users(request):
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})

def logout(request):
    auth.logout(request)
    return redirect('Home')


# Category Add View
def category_add(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        
        
        category = Category(
            category_name=category_name,
        )
        category.save()
        messages.success(request, 'Category added successfully!')
        return redirect('adminpanel')
    
    return render(request, 'category_add.html')


# Product Add View
def product_add(request):
    if request.method=='POST':
        sname=request.POST['product_name']
        add=request.POST['price']
        age=request.POST['description']
        img = request.FILES.get('p_image')
        
        sel=request.POST['sel']
        product1=Category.objects.get(id=sel)
        std=Product(prname=sname,prprice=add,prdesc=age,primg=img,category=product1)
        std.save()
        return redirect('product_add')
    return render(request, 'add_product.html')



def delete_product(request, pk):
    product = Product.objects.filter(pk=pk)
    product.delete()
    return redirect('view_products')



def userpanel(request):
    categories = Category.objects.all()
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'userpanel.html', {'categories': categories, 'cart': cart})


# def checkout(request):
    
#     return render(request, 'checkout.html')


    

    

def delete_user(request, pk):
    User.objects.filter(pk=pk).delete()
    return redirect('view_users')



def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'category_detail.html', {'category': category, 'products': products,'cart': cart})


def cart(request):
    current_user = request.user
    pr=Product.objects.get()
    cart_Item, created=Cart.objects.get_or_create(user=request.user,prod=pr)
    if not created:
        cart_Item.quantity +=1
        cart_Item.save()
    crt = Cart.objects.filter(user=current_user)
    num = len(crt)
    cat = Category.objects.all()
    ct = Cart.objects.all()
    
    user_id = request.user.id
    total = sum(item.subtotal() for item in ct if item.user.id == user_id)
    
    return render(request,'cart.html',{'category':cat,"cart":ct,'ttl':total, 'number':num})

def add_cart(request,pk):
    pdt = Product.objects.get(id=pk)
    user_id = request.user.id
    usr = User.objects.get(id=user_id)
    ct = Cart(user=usr,prod=pdt)
    ct.save()
    return redirect('cart')    



def increment_quantity(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrement_quantity(request, pk):
    cart_item = Cart.objects.get(pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove(requst,ct):
    crt = Cart.objects.get(id=ct)
    crt.delete()
    return redirect('cart')

# def remove_from_cart(request, pk):
#     cart_item = Cart.objects.get(pk=pk)
#     cart_item.delete()
#     return redirect('cart')


# def view_cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         cart_items = Cart.objects.filter(user=user)
#         total = sum(item.prod.price * item.quantity for item in cart_items)
#         return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})
#     else:
#         return redirect('login')

# @login_required
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     user = request.user
#     cart_item, created = Cart.objects.get_or_create(user=user, prod=product)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('view_cart')

# @login_required
# def remove_from_cart(request, cart_id):
#     cart_item = Cart.objects.get(id=cart_id)
#     cart_item.delete()
#     return redirect('view_cart')