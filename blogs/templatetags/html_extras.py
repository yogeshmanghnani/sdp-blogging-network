from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def get_first_image(content):
	my_page = BeautifulSoup(content, features='html.parser')
	try:
		link = my_page.find('img').attrs['src']
	except:
		return False
	#link = my_page.find('img').attr['src']
	return link
