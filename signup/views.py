from django.shortcuts import render
from django.http import HttpResponseRedirect
from mailsnake import MailSnake

def signup(request):
  return render(request, 'signup.html')

def thanks(request):
  return render(request, 'thanks.html')

def earlyAccessSubmit(request):
    from signup.forms import SignupForm
    if request.method == 'POST': # If the form has been submitted...
        form = SignupForm(request.POST) # A form bound to the POST data
        if form.is_valid():
          ms = MailSnake('60a810702ef83b7de50b150df5008109-us5')
          lists = ms.lists()
          ms.listSubscribe(
            id = lists['data'][0]['id'],
            email_address = form.cleaned_data['email'],
            merge_vars = {
                'GROUPINGS': [
                    {'id': 7197,
                     'groups': 'Pre-Launch',},]
                },
            update_existing = True,
            double_optin = False,
            )
          return HttpResponseRedirect('/signup/thanks/') # Redirect after POST

    else:
        form = SignupForm() # An unbound form

    return render(request, 'signup.html', {
        'form': form,
    })
    
def getInTouchSend(request):
    from signup.forms import GetInTouchForm
    if request.method == 'POST': # If the form has been submitted...
        form = GetInTouchForm(request.POST) # A form bound to the POST data
        if form.is_valid():
          name = form.cleaned_data['name']
          myList = ['Website Form Message from',name]
          subject = ' '.join(myList)
          sender = form.cleaned_data['email']
          message = form.cleaned_data['message']
          recipients = ['info@swept.in']

          from django.core.mail import send_mail
          send_mail(subject, message, sender, recipients)
          return HttpResponseRedirect('/signup/thanks/') # Redirect after POST
    else:
        form = GetInTouchForm() # An unbound form

    return HttpResponseRedirect('/signup/thanks/') # Redirect after POST
