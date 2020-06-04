# admin.py (app)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Defines classes used to generate 'app' Django Admin portion of website.

Available functions:
- There should be Admin class for each Model that can be modified by admin user.
"""

from django.contrib import admin
from app.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """Assigns 'USER ID' number, once user registers with HELP."""

    list_display = ("user_id", )
    search_fields = ("user__username",)
    exclude = ('created_by', 'last_modified_by',)
    list_filter = ("user_id",)
    list_per_page = 25


admin.site.register(UserProfile, UserProfileAdmin)
