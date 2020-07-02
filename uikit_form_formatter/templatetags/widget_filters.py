from django import template, forms
from django.shortcuts import render

register = template.Library()


@register.filter
def is_textinput(field):
	return isinstance(field.field.widget, forms.TextInput)

@register.filter
def is_emailinput(field):
	return isinstance(field.field.widget, forms.EmailInput)

@register.filter
def is_checkbox(field):
	return isinstance(field.field.widget, forms.CheckboxInput)

@register.filter
def is_password(field):
	return isinstance(field.field.widget, forms.PasswordInput)

@register.filter
def is_radioselect(field):
	return isinstance(field.field.widget, forms.RadioSelect)

@register.filter
def is_select(field):
	return isinstance(field.field.widget, forms.Select)

@register.filter
def is_checkboxselectmultiple(field):
	return isinstance(field.field.widget, forms.CheckboxSelectMultiple)

@register.filter
def is_file(field):
	return isinstance(field.field.widget, forms.FileInput)

@register.filter
def is_clearable_file(field):
	return isinstance(field.field.widget, forms.ClearableFileInput)

@register.filter
def is_multivalue(field):
	return isinstance(field.field.widget, forms.MultiWidget)


@register.filter
def classes(field):
	"""
	Returns CSS classes of a field
	"""
	return field.widget.attrs.get('class', None)

@register.filter("add_class")
def add_class(field, css_class):
	return append_attr(field, "class:" + css_class)

@register.filter('klass')
def klass(ob):
	return ob.__class__.__name__
