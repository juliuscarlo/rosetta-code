import unittest

from solution import BucketSet


class TestBucketSetMethods(unittest.TestCase):

    def test_get_bucket_value(self):
        self.assertEqual("foo".upper(), "FOO")

    def update_value(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def transfer_content(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that transfer does not leave bucket with negative value
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
