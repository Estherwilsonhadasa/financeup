from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from	django.utils	import	timezone

class Profile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# class Transaction(models.Model):
# 	transaction_id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	bank_name = models.CharField(max_length=200)
# 	branch = models.CharField(max_length=200)
# 	account_name = models.CharField(max_length=200)
# 	account_number = models.IntegerField()
# 	depositors_name = models.CharField(max_length=200)
# 	amount = models.IntegerField()
# 	created_at = models.DateField()
# 	updated_at =models.DateField()

# 	def __str__(self):
# 		return u'%s %s %s %s %s %s %s %s %s' %(self.user,self.bank_name,self.branch,self.account_name,
# 		self.account_number,self.depositors_name,self.amount,self.created_at,self.updated_at)


class Record(models.Model):
	transaction_id = models.AutoField(primary_key=True)
	user=models.ForeignKey('auth.User',  on_delete=models.CASCADE)
	bank_name = models.CharField(max_length=200)
	branch = models.CharField(max_length=200)
	account_name = models.CharField(max_length=200)
	account_number = models.IntegerField()
	depositors_name = models.CharField(max_length=200)
	amount = models.IntegerField()
	comment = models.TextField(default="")
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(blank=True,	null=True)

	def __str__(self):
		return u'%s %s %s %s %s %s %s %s %s %s'   %(self.user,self.bank_name,self.branch,self.account_name,
		self.account_number,self.depositors_name,self.amount,self.comment,self.created_at,self.updated_at)

