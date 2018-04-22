from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required
import stripe
import sys
# import request

pub_key = "pk_test_JQjapwoMEXZYA01fnjDTBQaV"
secret_key = "sk_test_x5RMbDg4B2MKf8hh1ysaWuBY"
stripe.api_key = secret_key

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # for i in request.POST:
            #     print(i)
# prod_CMQhlNvWEC1GTB
            # try:
            email= request.POST['stripeEmail']
            source= request.POST['stripeToken']
            # user.email = email
            user = form.save()

            for i in request.POST:
                print(i)
            customer = stripe.Customer.create(
                email=user.email,
                # plan = 'prod_CNva2YwamwS3D0',
                card = request.POST['stripeToken']
                #user.stripe_id,
                # card = form.cleaned_data['stripe_id'],
            )

            charge = stripe.Charge.create(
                customer=customer.id,
                amount=1999,
                currency="USD",
                description='test',
                # source=request.POST['stripeToken']
            )
            print("Customer id is : " + customer.id)

            subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'plan': 'test'}],
            )
            user.stripe_id = customer.id
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/saferdb/query')

            # except stripe.CardError e:
            #     form.add_my_error("Card has been declined.")
        # except ImportError:
        #         print('shit failed')
        #         form = RegistrationForm(request.POST)
        #         args = {'form': form, 'pub_key': pub_key}
        #         return render(request, 'accounts/reg_form.html', args)
        else:
            form = RegistrationForm(request.POST)
            args = {'form': form, 'pub_key': pub_key}
            return render(request, 'accounts/reg_form.html', args)
    else:
        form = RegistrationForm(request.POST)
        args = {'form': form, 'pub_key': pub_key}#
        return render(request, 'accounts/reg_form.html', args)

# @login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)
# @login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user )

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form}
            return render(request, 'accounts/edit_profile.html', args )
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args )

def cancel_subscription(request):
    #try:
    customer = stripe.Customer.retrieve(request.user.stripe_id)
    customer.cancel_subscription(at_period_end=True)

    # except Exception e:
    # messages.error(request, e)
    return render(request, '')

def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user )

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/accounts/profile')
            else:
                return redirect('/account/change-password')
        else:
            form = PasswordChangeForm(user=request.user)

            args = {'form': form}
            return render(request, 'accounts/change_password.html', args )
