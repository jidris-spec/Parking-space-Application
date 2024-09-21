from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from space.models import ParkingSpace
from space.forms import ParkingSpaceForm



def home(request):
    spaces = ParkingSpace.objects.all()
    return render(request, 'home.html', {'spaces': spaces})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password and confirm password
        if password == confirm_password:
            try:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('login')  # Redirect to the login page after successful signup
            except Exception as e:
                messages.error(request, f"Error creating account: {e}")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'signup.html')


def login_view(request):
    return render(request, 'login.html')


def list_space(request):
    if request.method == 'POST':
        form = ParkingSpaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parking space listed successfully!")
            return redirect('home')  
    else:
        form = ParkingSpaceForm()

    return render(request, 'list-space.html', {'form': form})


def space_list(request):
    spaces = ParkingSpace.objects.all()  # Retrieve all parking spaces
    return render(request, 'space-list.html', {'spaces': spaces})
