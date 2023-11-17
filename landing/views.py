from django.shortcuts import render, redirect
from .form import ContactForm
from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives, send_mail


def send_message(name, email, number):
    text = get_template('message.html')
    context = {'name': name, 'email': email, 'number': number}
    subject = 'developer'
    from_email = 'from@example.com'

    text_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.send('tursunbayev7277@gmail.com')



def home(request):
   context = {}
   if request.method == 'POST':
      form= ContactForm(request.POST)
      if form.is_valid():
        send_message(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['number'])
        context= {'success': 1}
   else:
     form=ContactForm()
   context['form']= form
   return render(request, 'home.html', context=context)



    
