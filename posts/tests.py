from rest_framework.test import APITestCase,APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import PostListCreateView
from django.contrib.auth import get_user_model

User = get_user_model()


class HelloWorldTestCase(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse('posts_home'))

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["message"],"Hello world")


class PostListCreateTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('list_posts')


    def authenticate(self):
        self.client.post(reverse('signup'),{
            "email" : "jonathon@gmail.com",
            "password" : "1234567890",
            "username" : "jonathon123"
        })

        respsonse = self.client.post(reverse('login'),{
            "email" : "jonathon@gmail.com",
            "password" : "1234567890",

        })
        # print(respsonse.data)
        token= respsonse.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {token}")

    

    def test_list_posts(self):
        
        response = self.client.get(self.url)


        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['count'],0)
        self.assertEqual(response.data['results'],[])


    def test_post_creation(self):
        self.authenticate()
        sample_data = {
            "title" : "sample title",
            "content" : "this is a sample content"
        }

        response = self.client.post(reverse('list_posts'),
                                    sample_data
                                    )
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"],sample_data["title"])


    


# Create your tests here.
