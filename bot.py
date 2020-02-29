from users.models import User
with open('bot.txt', 'r') as f1:
	fc = [u.strip() for u in f1.readlines()]
	for u in fc:
            try: 
                User.objects.create_user(u, email=u+"@gmail.com", password="abc123")
            except:
                pass
