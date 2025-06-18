from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from django.contrib.admin.views.decorators import staff_member_required
import calendar

from admissions.models import Student, CommissionDetails
from .models import UserProfile


def login_page(request):
    return render(request, 'login_page.html')


@login_required
def admission_form(request):
    return render(request, 'Admission_form.html')


@login_required
def accounts_first_page(request):
    students = Student.objects.all()
    return render(request, 'accounts_first_page.html', {'students': students})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST.get('role')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        UserProfile.objects.create(user=user, role=role)
        user.save()

        messages.success(request, "Registration successful! Please login")
        return redirect('/login/')

    return render(request, 'register.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.userprofile.role == 'Admissions':
                return redirect('/admissions_form/')
            elif user.userprofile.role == 'Accounts':
                return redirect('/accounts_first_page/')
            else:
                messages.error(request, "Role not assigned")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login_page.html')


@staff_member_required
@staff_member_required
def monthly_dashboard(request):
    from django.db.models import F, ExpressionWrapper, DecimalField
    import json

    commissions = CommissionDetails.objects.select_related('student')

    # Extract available years from course_start_date
    year_choices = commissions.annotate(
        year=ExtractYear('student__course_start_date')
    ).values_list('year', flat=True).distinct()
    year_choices = sorted(set(int(y) for y in year_choices if y))

    # Use all 12 months for dropdown
    month_names = list(calendar.month_name)[1:]

    # Get selected filters or defaults
    selected_year = int(request.GET.get('year', year_choices[-1] if year_choices else 2025))
    selected_month = request.GET.get('month', 'January')

    # Filter commissions by year and month
    filtered = commissions.annotate(
        year=ExtractYear('student__course_start_date')
    ).filter(
        year=selected_year,
        student__month=selected_month
    )

    # Overall stats
    total_admissions = filtered.count()
    total_commission = filtered.aggregate(Sum('commission_earned'))['commission_earned__sum'] or 0
    total_claimed = filtered.aggregate(Sum('amount_received'))['amount_received__sum'] or 0
    remaining = total_commission - total_claimed

    # 🔹 Calculate remaining amount per student
    student_remaining = (
        filtered
        .annotate(remaining_amount=ExpressionWrapper(
            F('commission_earned') - F('amount_received'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        ))
        .values('student__name', 'remaining_amount')
    )

    # 🔹 Format for Chart.js
    student_names = [item['student__name'] for item in student_remaining if item['remaining_amount'] > 0]
    remaining_amounts = [float(item['remaining_amount']) for item in student_remaining if item['remaining_amount'] > 0]

    context = {
        'years': year_choices,
        'months': month_names,
        'selected_year': selected_year,
        'selected_month': selected_month,
        'entry_count': total_admissions,
        'total_commission': total_commission,
        'total_claimed': total_claimed,
        'remaining_amount': remaining,

        # ⬇️ For the new chart
        'student_names_json': json.dumps(student_names),
        'remaining_amounts_json': json.dumps(remaining_amounts),
    }

    return render(request, 'dashboard.html', context)
