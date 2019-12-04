from django import template
import datetime

register = template.Library()

@register.filter(name = "my_lower_filter")
def my_lower_filter(value):  # Only one argument
	return value.lower()

@register.filter(name = "compare_number")
def compare_number(value):  
	if value == 0:
		return 'ZERO!'
	elif value > 0 and value < 10:
		return 'from 0 to 10'
	elif value > 10 and value < 50:
		return 'from 10 to 50'
	else:
		return 'Число > 50!'

@register.filter(name = "get_data_color")
def get_due_data_color(value):  
	if value == 0:
		return "red"
	elif value > 0 and value < 10:
		return "green"
	elif value > 10 and value < 50:
		return "blue"
	else:
		return "black"

register.simple_tag(lambda x: x - 1, name='minusone')

@register.simple_tag(name='minustwo')
def some_function(value):
	return value - 2


