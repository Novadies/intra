from smtplib import SMTPException

from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.db.models.signals import Signal
from django.dispatch import receiver
from django.template.loader import render_to_string

from logs.logger import logger

