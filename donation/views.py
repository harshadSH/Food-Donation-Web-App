from sqlite3 import IntegrityError

from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_logins(request):
    return render(request, 'all_logins.html')

def donor_login(request):
    error = ""
    if request.method == 'POST':
        
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            # User authentication successful, log the user in
            login(request, user)
            error = "no" # Change 'success_page' to the URL name of your success page
        else:
            # Authentication failed
            error = "yes"

    return render(request, 'donor_login.html', locals())

def volunteer_login(request):
    error = ""
    if request.method == 'POST':

        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            try:
                user1 = Volunteer.objects.get(user=user)
                if user1.status != "pending":
                    login(request, user)
                    error = "no"  # Change 'success_page' to the URL name of your success page
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            # Authentication failed
            error = "yes"

    return render(request, 'volunteer_login.html', locals())

def ngo_login(request):
    error = ""
    if request.method == 'POST':

        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            # User authentication successful, log the user in
            login(request, user)
            error = "no"  # Change 'success_page' to the URL name of your success page
        else:
            # Authentication failed
            error = "yes"
    return render(request, 'ngo_login.html', locals())
def donor_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST.get('first_name', '')
        ln = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        password = request.POST.get('password', '')
        userpic = request.FILES.get('userpic', None)
        address = request.POST.get('address', '')

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, email=email, password=password)
            donor = Donor.objects.create(user=user, contact=contact, userpic=userpic, address=address)
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor_reg.html', locals())

def volunteer_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST.get('first_name', '')
        ln = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        password = request.POST.get('password', '')
        userpic = request.FILES.get('userpic', None)
        idpic = request.FILES.get('idpic', '')
        address = request.POST.get('address', '')
        aboutme = request.POST.get('aboutme', '')

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, email=email, password=password)
            volunteer = Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address, aboutme=aboutme, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'volunteer_reg.html', locals())

def donor_base(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donor_base.html')


def donate_now(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)

    if request.method == 'POST':
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']



        try:
            # Create a new Donation object
            donation = Donation.objects.create(
                donor=donor,
                donationname=donationname,
                collectionloc=collectionloc,
                donationpic=donationpic,
                description=description,
                status="Pending"
            )
            # If the donation is successfully created, redirect the user to a success page
            error = "no"
        except:
            # If there's an error, set the error message
            error = "yes"

    return render(request, 'donate_now.html', locals())



def Logout(request):
    logout(request)
    return redirect('all_logins')

def donor_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'donor_history.html', locals())

def foram(request):
    return render(request, 'foram.html')

def donate(request):
    error = None
    if request.method == 'POST':
        # Extract form data
        donation_name = request.POST.get('donationname', '')
        collection_address = request.POST.get('collectionloc', '')
        description = request.POST.get('description', '')
        donation_pic = request.FILES.get('donationpic', None)

        try:
            donation = Donation.objects.create(
                donationname=donation_name,
                collectionloc=collection_address,
                description=description,
                donationpic=donation_pic,
                status="Pending"  # Set initial status
            )
            error = "no"
        except IntegrityError:
            error = "yes"
    return render(request, 'donate.html', locals())

def ngo_base(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    return render(request, 'ngo_base.html')

def ngo_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST.get('first_name', '')
        ln = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        password = request.POST.get('password', '')
        userpic = request.FILES.get('userpic', None)
        idpic = request.FILES.get('idpic', '')
        address = request.POST.get('address', '')
        aboutme = request.POST.get('aboutme', '')

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=email, email=email, password=password)
            ngo = NGO.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address, aboutme=aboutme, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'ngo_reg.html', locals())

def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    donations = Donation.objects.filter(status="Pending")
    return render(request, 'pending_donation.html', locals())

def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donations = Donation.objects.filter(Q(valname= volunteer.user.first_name) & (Q(status="On Route") | Q(status="Collected")))
    return render(request, 'accepted_donation.html', locals())

def available_order(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donations = Donation.objects.filter(status= "Accepted")
    return render(request, 'available_order.html', locals())

def view_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    donation = Donation.objects.get(id=pid)
    if request.method == 'POST':

            # Update the donation status to "Accepted"
        donation.status = "Accepted"
        user = request.user
        ngo = NGO.objects.get(user=user)
        donation.deliveryloc = ngo.address
        donation.ngoname = ngo.user.first_name
        donation.ngo_contact = ngo.contact
        donation.save()

    return render(request, 'view_detail.html', {'donation': donation})

def donation_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    if request.method == 'POST':
        # Get the current donation
        user = request.user
        volunteer = Volunteer.objects.get(user=user)

        # Check the current status of the donation
        if donation.status == "Accepted":
            donation.status = "On Route"

            donation.valname = volunteer.user.first_name
            donation.val_contact = volunteer.contact
            donation.save()

        elif donation.status == "On Route":
            # Update the status to "Collected"
            donation.status = "Collected"
            # Save the changes
            donation.save()

        elif donation.status == "Collected":
            # Update the status to "Completed"
            donation.status = "Completed"
            # Save the changes
            donation.save()


    return render(request, 'donation_detail.html', locals())

def volunteer_base(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    return render(request, 'volunteer_base.html', locals())

def vol_history(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donations = Donation.objects.filter(valname=request.user.first_name)
    return render(request, 'vol_history.html', locals())

def ngo_history(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    donations = Donation.objects.filter(ngoname= request.user.first_name)
    return render(request, 'ngo_history.html', locals())

def pending_order(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donations = Donation.objects.filter(Q(status="On Route") | Q(status="Collected"))
    return render(request, 'pending_order.html', locals())


