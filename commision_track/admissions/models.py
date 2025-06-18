from django.db import models

# Create your models here.
class Student(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    name = models.CharField(max_length=100)
    lead_code = models.CharField(max_length=20)
    lead_name = models.CharField(max_length=100)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES,default=None)
    university = models.CharField(max_length=50,default=None)
    education_consultant = models.CharField(max_length=20,default=None)
    course = models.CharField(max_length=20)
    student_ref_no = models.IntegerField(default=0)
    intake = models.CharField(max_length=20,default=None)
    scholarship = models.IntegerField(default=0)
    cashback_amt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    referal_cashback = models.IntegerField(default=0)
    semesters = models.IntegerField(default=0)
    tuition_fee = models.IntegerField(default=0)
    coe_issue_date = models.DateField(null=True, blank=True)
    course_start_date = models.DateField(null=True, blank=True)
    course_end_date = models.DateField(null=True, blank=True)
    
    ## yess i am working on a project
    def __str__(self):
        return self.name
    
class CommissionDetails(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    claiming_branch = models.CharField(max_length=100)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    commission_earned = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_commission_inc_gst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    commission_type = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comments_by_accounts = models.TextField(null=True, blank=True)
    expected_date = models.DateField(null=True, blank=True)
    cashback = models.CharField(max_length=50, null=True, blank=True)
    cashback_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cashback_paid = models.CharField(max_length=50, null=True, blank=True)
    cb_payment_expected_date = models.DateField(null=True, blank=True)
    net_profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    coe_status = models.CharField(max_length=50, null=True, blank=True)