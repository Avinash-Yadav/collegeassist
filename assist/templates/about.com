{% extends "base.html" %}
{% load crispy_forms_tags %}
{% block title %}COLLEGE ASSIST : About{% endblock %}
<!-- priv -->
{% block head %}
{% endblock %}
{% block content %}

{% endblock %}