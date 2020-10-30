from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

	def test_create_user_email_successful(self):
		"""Test creating a new user with an email is successfull"""
		email="indragtzade@gmail.com"
		password="Test123"
		user=get_user_model().objects.create_user(
			email=email,
			password=password
			)

		self.assertEqual(user.email,email)
		self.assertTrue(user.check_password(password))



	def test_new_user_email_normalized(self):
		"""Test eamil for new user is normalized"""
		email="indragtzade@GMAIL.COM"
		user=get_user_model().objects.create_user(email,"Test123")
		self.assertEqual(user.email,email.lower())




	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises valuerror"""
		with self.assertRaises(ValueError):
			user=get_user_model().objects.create_user(None,"Test123")



	def test_create_new_superuser(self):
		"""Test creating new super user"""
		user=get_user_model().objects.create_superuser(
			"test@test.com",
			"Test123"
			)
		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)