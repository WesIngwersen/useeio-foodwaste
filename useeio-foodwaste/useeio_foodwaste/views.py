# views.py (useeio-foodwaste)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of views."""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest


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


def jupyter(request):
    """Renders the jupyter page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'jupyter.html',
        {
            'title': 'Jupyter',
            'message': 'Jupyter Notebook.',
            'year': datetime.now().year,
        }
    )


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
