from django.shortcuts import render

# Create your views here.

posts = [
		{
			'title': 'First Blog Post',
			'author': 'Yogesh',
			'content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Adipiscing elit duis tristique sollicitudin nibh. Sollicitudin aliquam ultrices sagittis orci a scelerisque. Odio ut sem nulla pharetra diam sit amet nisl. Tortor id aliquet lectus proin nibh nisl condimentum. Ut enim blandit volutpat maecenas volutpat blandit. Viverra vitae congue eu consequat ac. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum. Nisi vitae suscipit tellus mauris a. Pulvinar mattis nunc sed blandit libero volutpat. Nisl vel pretium lectus quam. Tempor id eu nisl nunc mi ipsum faucibus vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Bibendum at varius vel pharetra vel turpis nunc. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque.
			Lobortis mattis aliquam faucibus purus. Auctor neque vitae tempus quam pellentesque nec nam aliquam. Duis ultricies lacus sed turpis tincidunt id aliquet risus. Odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus. Magna etiam tempor orci eu lobortis elementum nibh. Viverra nibh cras pulvinar mattis nunc sed. Tincidunt dui ut ornare lectus sit amet. Lorem ipsum dolor sit amet consectetur adipiscing. Penatibus et magnis dis parturient. Nec ultrices dui sapien eget mi proin sed libero. Odio euismod lacinia at quis risus.
			Libero volutpat sed cras ornare arcu dui vivamus. Proin libero nunc consequat interdum varius sit amet. Vel pharetra vel turpis nunc eget lorem dolor. Quisque egestas diam in arcu cursus euismod. Amet facilisis magna etiam tempor. Ornare massa eget egestas purus viverra accumsan in nisl. Venenatis cras sed felis eget velit aliquet sagittis. Quis eleifend quam adipiscing vitae proin. Purus in mollis nunc sed id semper risus in. Velit euismod in pellentesque massa placerat duis ultricies lacus sed. Pellentesque elit eget gravida cum sociis natoque penatibus et. Dolor sed viverra ipsum nunc aliquet. Vel facilisis volutpat est velit egestas dui id ornare arcu. Vel risus commodo viverra maecenas accumsan. Orci a scelerisque purus semper eget duis.
			Sed augue lacus viverra vitae congue eu. Ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant. Mattis aliquam faucibus purus in massa. Netus et malesuada fames ac turpis egestas maecenas pharetra convallis. Laoreet suspendisse interdum consectetur libero id. Sit amet justo donec enim. Enim tortor at auctor urna nunc id cursus metus aliquam. Quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Accumsan in nisl nisi scelerisque eu ultrices vitae auctor. Sem fringilla ut morbi tincidunt augue interdum velit. Tempor commodo ullamcorper a lacus vestibulum. Vel eros donec ac odio tempor orci dapibus. Nulla facilisi etiam dignissim diam quis enim. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Sem et tortor consequat id porta nibh venenatis. Justo eget magna fermentum iaculis eu. Elementum pulvinar etiam non quam lacus suspendisse faucibus.
			Porttitor eget dolor morbi non arcu risus quis. Vivamus at augue eget arcu dictum varius duis at. Laoreet sit amet cursus sit amet dictum. Porta non pulvinar neque laoreet suspendisse interdum consectetur libero. Sed vulputate odio ut enim blandit volutpat maecenas volutpat. Ultrices in iaculis nunc sed. Nunc vel risus commodo viverra. Odio aenean sed adipiscing diam donec adipiscing tristique. Consectetur lorem donec massa sapien faucibus et. Tincidunt id aliquet risus feugiat in ante."""
		},	
		{
			'title': 'Second Blog Post',
			'author': 'Yogesh',
			'content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Adipiscing elit duis tristique sollicitudin nibh. Sollicitudin aliquam ultrices sagittis orci a scelerisque. Odio ut sem nulla pharetra diam sit amet nisl. Tortor id aliquet lectus proin nibh nisl condimentum. Ut enim blandit volutpat maecenas volutpat blandit. Viverra vitae congue eu consequat ac. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum. Nisi vitae suscipit tellus mauris a. Pulvinar mattis nunc sed blandit libero volutpat. Nisl vel pretium lectus quam. Tempor id eu nisl nunc mi ipsum faucibus vitae. Eu augue ut lectus arcu bibendum at varius vel pharetra. Bibendum at varius vel pharetra vel turpis nunc. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque.
			Lobortis mattis aliquam faucibus purus. Auctor neque vitae tempus quam pellentesque nec nam aliquam. Duis ultricies lacus sed turpis tincidunt id aliquet risus. Odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus. Magna etiam tempor orci eu lobortis elementum nibh. Viverra nibh cras pulvinar mattis nunc sed. Tincidunt dui ut ornare lectus sit amet. Lorem ipsum dolor sit amet consectetur adipiscing. Penatibus et magnis dis parturient. Nec ultrices dui sapien eget mi proin sed libero. Odio euismod lacinia at quis risus.
			Libero volutpat sed cras ornare arcu dui vivamus. Proin libero nunc consequat interdum varius sit amet. Vel pharetra vel turpis nunc eget lorem dolor. Quisque egestas diam in arcu cursus euismod. Amet facilisis magna etiam tempor. Ornare massa eget egestas purus viverra accumsan in nisl. Venenatis cras sed felis eget velit aliquet sagittis. Quis eleifend quam adipiscing vitae proin. Purus in mollis nunc sed id semper risus in. Velit euismod in pellentesque massa placerat duis ultricies lacus sed. Pellentesque elit eget gravida cum sociis natoque penatibus et. Dolor sed viverra ipsum nunc aliquet. Vel facilisis volutpat est velit egestas dui id ornare arcu. Vel risus commodo viverra maecenas accumsan. Orci a scelerisque purus semper eget duis.
			Sed augue lacus viverra vitae congue eu. Ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant. Mattis aliquam faucibus purus in massa. Netus et malesuada fames ac turpis egestas maecenas pharetra convallis. Laoreet suspendisse interdum consectetur libero id. Sit amet justo donec enim. Enim tortor at auctor urna nunc id cursus metus aliquam. Quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Accumsan in nisl nisi scelerisque eu ultrices vitae auctor. Sem fringilla ut morbi tincidunt augue interdum velit. Tempor commodo ullamcorper a lacus vestibulum. Vel eros donec ac odio tempor orci dapibus. Nulla facilisi etiam dignissim diam quis enim. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Sem et tortor consequat id porta nibh venenatis. Justo eget magna fermentum iaculis eu. Elementum pulvinar etiam non quam lacus suspendisse faucibus.
			Porttitor eget dolor morbi non arcu risus quis. Vivamus at augue eget arcu dictum varius duis at. Laoreet sit amet cursus sit amet dictum. Porta non pulvinar neque laoreet suspendisse interdum consectetur libero. Sed vulputate odio ut enim blandit volutpat maecenas volutpat. Ultrices in iaculis nunc sed. Nunc vel risus commodo viverra. Odio aenean sed adipiscing diam donec adipiscing tristique. Consectetur lorem donec massa sapien faucibus et. Tincidunt id aliquet risus feugiat in ante."""
		}
]

def home(request):
	context = {
			'posts': posts,
			'title' : "Blog Posts",
			'blog_home': 'uk-active'
			}
	return render(request, 'blogs/home.html', context)


def about(request):
	context = {
			'blog_about': 'uk-active'
			}
	return render(request, 'blogs/about.html', context)
