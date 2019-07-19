from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.school = Image(name = 'school', description = 'school character')
        self.school.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.school, Image))
    def test_save_method(self):
        self.school.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
    def test_delete_method(self):
        self.new_image = Image(name = 'flower', description = 'the attractive scent of the flower despite the thorns')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)
    def test_update_method(self):
        self.tony = Image(name = 'tony', description = 'picture of tony')
        self.tony.save_image()
        self.tony = Image(name = 'tony', description = 'picture of tony')        
        self.tony.update_image(name = 'tony')
        self.tony.save_image()
        images = Image.objects.filter(name = 'tony')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)

