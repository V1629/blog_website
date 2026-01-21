#****Returns all customers from customer table
from posts.models import User as user
from posts.models import Post as post
posts = post.objects.all()

#****Returns first customer in table
first_user = user.objects.first()

#****Returns last customer in table
last_user = user.objects.last()

#****Returns single customer by name
user_by_name = user.objects.get(name="Peter Piper")

#****Returns single customer by id
userBYId = user.objects.get(id=4)

#****Returns all orders related to customer (firstCustomer variable set above)
first_user.order_set.all()

#****Returns orders customer name: (Query parent model values)
parentName = post.objects.first().user.name

#****Returns products from products table with value of "Out Door" in category attribute
filtered_posts = post.objects.filter(category="Out Door")

#****Order/Sort Objects by id
leastToGreatest = posts.objects.all().order_by('id')
greatestToLeast = posts.objects.all().order_by('-id')

#****Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = posts.objects.filter(tags__name="Sports")


