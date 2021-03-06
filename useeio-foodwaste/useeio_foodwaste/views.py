# views.py (useeio-foodwaste)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of views."""

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


@login_required
def lab_data(request):
    """Renders the lab_data page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'lab_data.html',
        {
            'title': 'Lab Data',
            'message': 'Lab Data.',
            'year': datetime.now().year,
        }
    )


@login_required
def sdmp(request):
    """Renders the sdmp page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sdmp.html',
        {
            'title': 'SDMP',
            'message': 'Scientific Data Management Plan.',
            'year': datetime.now().year,
        }
    )
