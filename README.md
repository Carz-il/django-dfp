django-dfp
==========

This Django app provides template tags and other support for google DFP service.

How to install on your project
-------------------------------

1. Install the package
2. Add the app to your settings.py and your google DFP id:

```python
INSTALLED_APPS = (
    ...,
    ...,
    'djangogoogledfp'
)

GOOGLE_DFP_ACCOUNT_ID = "18123349"


```



Whenever you need to display an ad unit, make sure you place the init script on the page with the template tag:

```django
{% load  google_dfp %}
<head>
...
{% google_dfp_init_script %}
</head>
```

Than, you can put your ad:
(the height and weight are always px)

```django
{% load  google_dfp %}
.....

{% dfp_ad_unit "MY_AD250x250" 250 250 %}

.....
```

