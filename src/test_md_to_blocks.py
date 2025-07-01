import unittest

from md_to_blocks import markdown_to_blocks

class TestMDToBlocks(unittest.TestCase):
    def test1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         ["This is **bolded** paragraph",
                          "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                          "- This is a list\n- with items",],)
    
    def test2(self):
        md = """
Hello, this is the first paragraph
with some text on another line

- This list
- has many
- points
- because
- it
- is
- inefficient

This should be fine
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         ["Hello, this is the first paragraph\nwith some text on another line",
                          "- This list\n- has many\n- points\n- because\n- it\n- is\n- inefficient",
                          "This should be fine",],)