from django import forms
from .models import Student, CommissionDetails

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CommissionForm(forms.ModelForm):
    class Meta:
        model = CommissionDetails
        fields = [
            'claiming_branch',
            'commission_rate',
            'commission_earned',
            'gst',
            'total_commission_inc_gst',
            'commission_type',
            'amount',
            'bonus',
            'total',
            'amount_received',
            'remaining_balance',
            'comments_by_accounts',
            'expected_date',
            'cashback',
            'cashback_amount',
            'cashback_paid',
            'cb_payment_expected_date',
            'net_profit',
            'remark',
            'coe_status',
        ]
