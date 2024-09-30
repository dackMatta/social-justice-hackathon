from django.shortcuts import render, redirect
from .forms import CaseForm,CaseAssignmentForm,CommentForm
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from .models import Case,Authority,Comment,Conversation
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.views.decorators.http import require_POST


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:profile')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreationForm()
    return render(request, 'account/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home:profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'account/login.html', {"form": form})



@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('home:home')



@login_required
def profile(request):
    return render(request, 'account/profile.html')



def submit_case_form(request):
    form=CaseForm()
    if request.method=='POST':
        form=CaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Case submitted successfully')
            return redirect('home:raised_cases')
    return render(request, 'home/submit_case.html', {'form': form})



def raised_cases(request):
    cases = Case.objects.all()
    cases = cases.order_by('-created_at')
    for case in cases:
        if case.attachment:
            case.attachment_url = case.attachment.url
        else:
            case.attachment_url = None
    return render(request, 'home/raised_cases.html', {'cases': cases})



def case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    return render(request, 'home/case_details.html', {'case': case})


@login_required
def assign_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        authority_id = request.POST.get('authority_id')
        lawyer = get_object_or_404(Authority, id=authority_id)
        
        case.assigned_to = lawyer
        case.assigned_at = timezone.now()
        case.status = 'In Progress'
        case.save()
        
        messages.success(request, f'Case assigned to {lawyer.names} successfully.')
        return redirect('case_detail', pk=case.id)
    
    else:
        form = CaseAssignmentForm()
    
    lawyers = Authority.objects.all()
    return render(request, 'home/assign_case.html', {'case': case, 'lawyers': lawyers, 'form': form})



def lawyers(request):
    authorities=Authority.objects.all()
    return render(request,'home/lawyers.html',{'authorities':authorities})


@login_required
def track_case(request, case_id):
    if case_id:
        case = get_object_or_404(Case, id=case_id)
    else:
        case = None
    user = request.user
    
    if not case.tracked_by.filter(id=user.id).exists():
        case.tracked_by.add(user)
        messages.success(request, f'Case {case.id} has been added to your tracked cases.')
    else:
        messages.info(request, f'You are already tracking case {case.id}.')
    
    tracked_cases = user.tracked_cases.all()
    return render(request, 'home/track_case.html', {'tracked_cases': tracked_cases})

@login_required
def tracked_cases(request):
    user = request.user
    tracked_cases = user.tracked_cases.all()
    return render(request, 'home/tracked_cases.html', {'tracked_cases': tracked_cases})


@login_required
def send_message(request, lawyer_id):
    lawyer = get_object_or_404(Authority, id=lawyer_id)                     
    conversation, created = Conversation.objects.get_or_create(lawyer=lawyer, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.conversation = conversation
            comment.sender = request.user
            comment.save()
            return redirect('home:lawyer_chat', lawyer_id=lawyer_id)
    else:
        form = CommentForm()
    comments = conversation.comments.all().order_by('-created_at')
    context={
        'lawyer':lawyer,
        'form':form,
        'comments':comments,
    }
    return render(request, 'home/lawyer_chat.html', context)
 
