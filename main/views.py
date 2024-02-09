from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            email_body = f"Message from {name}:\n\n{message}\n\nReply to: {sender_email}"
            
            send_mail(
                subject=f"Message from {name} via Contact Form",
                message=email_body,
                from_email="rkerkides@gmail.com",
                recipient_list=["rkerkides@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            
    else:    
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})