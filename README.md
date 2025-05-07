# Django Project Setup Guide

This guide walks you through setting up a Django project from scratch.

## 1. Create Virtual Environment
```bash
python -m venv myenv
```

## 2. Activate Environment
```bash
myenv\Scripts\activate
```

## 3. Install Django in Virtual Environment
```bash
pip install Django
```

## 4. Create Project
```bash
django-admin startproject habibi
cd habibi
```

## 5. Run the Project
```bash
python manage.py runserver
```

## 6. Create New App
```bash
python manage.py startapp main
```

## 7. Register App in Settings
Add the following to `INSTALLED_APPS` in `settings.py`:
```python
'main.apps.MainConfig'
```

## 8. Create Directory Structure
Create these folders in the root project directory:
```bash
mkdir templates static media
```

## 9. Configure Static and Media Files
Add to `settings.py`:
```python
import os  # Add this to top of the file

MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 9.1. Configure Templates Directory
In `settings.py`, update `TEMPLATES` setting:
```python
TEMPLATES = [
    {
        # Other settings...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # Other settings...
    },
]
```

## 10. Configure Static URLs
In your project's main `urls.py` file:
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Other URL patterns...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 11. Create App URLs
Create `urls.py` in your `main` app:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

## 12. Link App URLs with Base URLs
In your project's main `urls.py` file:
```python
from django.urls import path, include

urlpatterns = [
    # Other URL patterns...
    path('', include('main.urls')),
]
```

## 13. Create View
In your app's `views.py` file:
```python
from django.shortcuts import render

def index(request):
    return render(request, 'base.html')
```