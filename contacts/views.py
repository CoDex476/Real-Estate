from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.contrib import messages

from .models import Contact

def contact(request):
    # method check
    if request.method == "POST":
        # get values
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # user enquiry submission check
        if request.user.is_authenticated:
            user_id = request.user.id

            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You've already made an enquiry for this property")
                return redirect('/listings/' + listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # send email
        send_mail(
            f"New Enquiry for Listing: {listing}",
            f"""
            You have a new property Enquiry.

            Listing: {listing}
            Name: {name}
            Phone: {phone}

            Please log in to the admin panel to view more details.
            """,
            "abednegodunyah@gmail.com",
            [realtor_email],
            fail_silently=False,
        )

        messages.success(request, 'Your enquiry has been submitted successfully, the realtor will get in touch soon')

        return redirect('/listings/' + listing_id)
