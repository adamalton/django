from django.test import TestCase
from .models import Musician, Song


class CreateTestCase(TestCase):
    """ Tests for the model manager `create` method. """

    def test_field_value_types_are_coerced(self):
        """ Field values of the returned object should be coerced to their correct types. """
        # If the PK is given as a string, it is coerced to its DB field type, which is int.
        obj = Musician.objects.create(id='2', name='Dave Grohl', num_bands=2)
        self.assertEqual(type(obj.id), int)

        # If a non-PK field is given as a string, that should also be coerced to its DB type
        obj = Musician.objects.create(name="Taylor Hawkins", num_bands='1')
        self.assertEqual(type(obj.num_bands), int)  # This currently fails

        # When the object already exists, fetching it by specifying the PK as a string should
        # return the correct object and coerce the PK to an int.
        obj = Musician.objects.get(id='2')
        self.assertEqual(type(obj.id), int)

        # And fetching it by specifying a non-PK integer field as a string should behave the same
        obj = Musician.objects.get(num_bands='2')
        self.assertEqual(type(obj.id), int)

        # And then test the same behaviour for foreign keys
        obj = Song.objects.create(musician_id='2')
        self.assertEqual(type(obj.musician_id), int)  # This currently fails
        # And the same if the object already exists
        obj = Song.objects.get(musician_id='2')
        self.assertEqual(type(obj.musician_id), int)
