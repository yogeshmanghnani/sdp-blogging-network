from . import dbreader
from users.models import User
from blogs.models import Blog_Post


u = User.objects.all()[5]
for i in dbreader.rows:
	b = Blog_Post(title = i[1], content = i[2], author = u)
	b.save()
