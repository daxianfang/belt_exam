from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
	def register(self, request, name, alias, email, password, confirm_password):
		NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
		ALIAS_REGEX = re.compile(r'^[a-zA-Z]+$')
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

		is_valid = True

		# User name validation
		if len(name) == 0:
			messages.error(request, 'User name is required.')
			is_valid = False
		elif len(name) < 2:
			messages.error(request, 'User name cannot be less than 2 characters.')
			is_valid = False
		elif not NAME_REGEX.match(name):
			messages.error(request, 'User name is letters only.')
			is_valid = False

		# User alias validation
		if len(alias) == 0:
			messages.error(request, 'User alias is required.')
			is_valid = False
		elif len(alias) < 2:
			messages.error(request, 'User alias cannot be less than 2 characters.')
			is_valid = False
		elif not ALIAS_REGEX.match(alias):
			messages.error(request, 'User alias is letters only.')
			is_valid = False

		# User email validation
		if len(email) == 0:
			messages.error(request, 'User email is required.')
			is_valid = False
		elif not EMAIL_REGEX.match(email):
			messages.error(request, 'User email format is not correct.')
			is_valid = False
		elif User.objects.filter(email=email):
			messages.error(request, 'This email has been taken.')
			is_valid = False

		# User password validation
		if len(password) == 0:
			messages.error(request, 'User password is required.')
			is_valid = False
		elif len(password) < 8:
			messages.error(request, 'User password is not strong enough, must be no less than 8 characters.')
			is_valid = False
		if len(confirm_password) == 0:
			messages.error(request, 'Please re-enter user password.')
			is_valid = False
		elif len(confirm_password) < 8:
			messages.error(request, 'User password is not strong enough, must be no less than 8 characters.')
			is_valid = False
		if password != confirm_password:
			messages.error(request, 'User password and confirmed password don\'t match.')
			is_valid = False

		if is_valid:
			hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
			User.objects.create(name=name, alias=alias, email=email, pw_hash=hashed)

		return is_valid

	def login(self, request, email, password):

		valid_login = True

		# Check whether the user is exist in database
		if len(email) == 0:
			messages.error(request, 'User email is required.')
			valid_login = False
		elif not User.objects.filter(email=email):
			messages.error(request, 'User does not exist.')
			valid_login = False
		else:
			attempt_user = User.objects.filter(email=email)[0]

			# Validate user password
			if bcrypt.hashpw(password.encode('utf-8'), attempt_user.pw_hash.encode('utf-8')) != attempt_user.pw_hash:
				messages.error(request, 'Incorrect password.')
				valid_login = False
			
		return valid_login

class User(models.Model):
	name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	pw_hash = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

class Friendship(models.Model):
	user = models.ForeignKey('User', related_name="usersfriend")
	friend = models.ForeignKey('User', related_name="friendsfriend")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)








