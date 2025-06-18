from django.contrib import admin
from .models import Student, CommissionDetails

class CommissionDetailsInline(admin.StackedInline):
    model = CommissionDetails
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'lead_code', 'lead_name', 'university',
        'semesters', 'tuition_fee',

        # Commission fields
        'get_claiming_branch', 'get_commission_rate', 'get_commission_earned',
        'get_coe_status'
    ]
    inlines = [CommissionDetailsInline]

    def get_field(self, obj, field):
        return getattr(obj.commissiondetails, field) if hasattr(obj, 'commissiondetails') else '-'

    def get_claiming_branch(self, obj): return self.get_field(obj, 'claiming_branch')
    get_claiming_branch.short_description = 'Claiming Branch'

    def get_commission_rate(self, obj): return self.get_field(obj, 'commission_rate')
    get_commission_rate.short_description = 'Commission Rate (%)'

    def get_commission_earned(self, obj): return self.get_field(obj, 'commission_earned')
    get_commission_earned.short_description = 'Commission Amount'

    def get_gst(self, obj): return self.get_field(obj, 'gst')
    get_gst.short_description = 'GST'

    def get_total_commission(self, obj): return self.get_field(obj, 'total_commission_inc_gst')
    get_total_commission.short_description = 'Total Commission (INC GST)'

    def get_commission_type(self, obj): return self.get_field(obj, 'commission_type')
    get_commission_type.short_description = 'Commission Type'

    def get_amount(self, obj): return self.get_field(obj, 'amount')
    get_amount.short_description = 'Amount'

    def get_bonus(self, obj): return self.get_field(obj, 'bonus')
    get_bonus.short_description = 'Bonus'

    def get_total(self, obj): return self.get_field(obj, 'total')
    get_total.short_description = 'Total'

    def get_amount_received(self, obj): return self.get_field(obj, 'amount_received')
    get_amount_received.short_description = 'Amount Received'

    def get_remaining_balance(self, obj): return self.get_field(obj, 'remaining_balance')
    get_remaining_balance.short_description = 'Remaining Balance'

    def get_comments_by_accounts(self, obj): return self.get_field(obj, 'comments_by_accounts')
    get_comments_by_accounts.short_description = 'Comments by Accounts'

    def get_expected_date(self, obj): return self.get_field(obj, 'expected_date')
    get_expected_date.short_description = 'Expected Date'

    def get_cashback(self, obj): return self.get_field(obj, 'cashback')
    get_cashback.short_description = 'Cashback'

    def get_cashback_amount(self, obj): return self.get_field(obj, 'cashback_amount')
    get_cashback_amount.short_description = 'Cashback Amount'

    def get_cb_payment_expected_date(self, obj): return self.get_field(obj, 'cb_payment_expected_date')
    get_cb_payment_expected_date.short_description = 'CB Payment Expected Date'

    def get_net_profit(self, obj): return self.get_field(obj, 'net_profit')
    get_net_profit.short_description = 'Net Profit'

    def get_remark(self, obj): return self.get_field(obj, 'remark')
    get_remark.short_description = 'Remark'

    def get_coe_status(self, obj): return self.get_field(obj, 'coe_status')
    get_coe_status.short_description = 'COE Status'
