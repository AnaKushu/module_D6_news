#{% extends 'flatpages/default.html' %}

#{% load custom_filters %}
#{% load custom_tags %}

#{% block title %}
#News
#{% endblock title %}

#{% block content %}
#   <h1>Новостная лента</h1>
#   <h3>{{ time_now|date:'d M Y' }}</h3>
#   <h3> {{ next_post|default_if_none:"Чуть позже сообщим о свежих новостях!" }} </h3>
#   <hr>
#   {% if perms.news.add_post %}
#   <a href="{% url 'post_create' %}">Добавить пост</a>
#   {% endif %}

#   {% if news %}
#        <table>
#            <tr>
#                <td>Название</td>
#                <td>Описание</td>
#                <td>Дата публикации</td>
#                <td>Категория</td>

#                {% if perms.news.change_post or perms.news.delete_post %}
#                <td>Действия</td>
#                {% endif %}

#            </tr>
#            {% for post in news %}
#            <tr>
#                <td>{{ post.title|censor }}</td>
#                <td><div align="center">{{ post.text|censor|truncatechars:15 }}</div></td>
#                <td>{{ post.dateCreation|date:'d M Y ' }}</td>
#                <td>{% for cat in post.postCategory.all %}
#                    {{ cat.name }}
#                    {% endfor %}
#                </td>
#                <td>
#                    {% if perms.news.change_post %}
#                    <a href="{% url 'post_update' pk=post.id %}">Изменить</a>
#                    {% endif %}
#                    {% if perms.news.delete_post %}
#                    <a href="{% url 'post_delete' pk=post.id %}">Удалить</a>
#                    {% endif %}
#                </td>
#            </tr>
#            {% endfor %}
#        </table>
#{% else %}
#    <h2>Новостей нет!</h2>
#{% endif %}

#{% if page_obj.has_previous %}
#    <a href="?{% url_replace page=1 %}">1</a>
#    {% if page_obj.previous_page_number != 1 %}
#        ...
#        <a href="?{% url_replace page=page_obj.previous_page_number %}">{{ page_obj.previous_page_number }}</a>
#       {% endif %}
#    {% endif %}

#    {{ page_obj.number }}

#    {% if page_obj.has_next %}
#        <a href="?{% url_replace page=page_obj.next_page_number %}">{{ page_obj.next_page_number }}</a>
#        {% if paginator.num_pages != page_obj.next_page_number %}
#            ...
#            <a href="?{% url_replace page=page_obj.paginator.num_pages %}">{{ page_obj.paginator.num_pages }}</a>
#        {% endif %}
#    {% endif %}

#{% endblock content %}


#{% if is_paginated %}
#<nav aria-label="...">
#    <ul class="pagination pagination-sm justify-content-center">
#    {% if page_obj.has_previous %}
#        <li class="page-item"><a class="page-link" href="?page=1">Начало</a></li>
#        <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}"><<<</a></li>
#    {% endif %}

#    {% for num in page_obj.paginator.page_range %}
#        {% if page_obj.number == num %}
#            <li class="page-item active"><a class="page-link">{{ num }}</a></li>
#        {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'-3' %}
#            <li class="page-item"><a class="page-link" href="?page={{ num }}">{{ num }}</a></li>
#        {% endif %}
#    {% endfor %}

#    {% if page_obj.has_next %}
#        <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">>>></a></li>
#        <li class="page-item"><a class="page-link" href="?page={{ page_obj.paginator.num_pages }}">Конец</a></li>
#    {% endif %}
#    </ul>
#</nav>

#{ % if is_not_subscriber %}
#<p class ="text-center" > < a href="{}" class ="btn btn-secondary btn-sm" > Подписаться < / a > < / p >
#{ % endif %}