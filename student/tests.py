from django.test import TestCase

# Create your tests here.
import random


# Generate a random 5-digit ID
random_id = random.randint(10000, 99999)

print(random_id)
