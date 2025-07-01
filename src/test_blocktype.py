import unittest

from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test1(self):
        md = "# Title"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test2(self):
        md = "## Title"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test3(self):
        md = "```This is a code block```"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, block_type)
    
    def test4(self):
        md = ">Hello\n>This is a quote\n>It is now done"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, block_type)
    
    def test5(self):
        md = "- This is an\n- unordered list\n- goodbye"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)
    
    def test6(self):
        md = "1. First element of ordered list\n2. I hope this works\n3. Farewell to you"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)
    
    def test7(self):
        md = "This is just a normal paragraph\nthat happens to have an extra line\nJoe is out"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

if __name__ == "__main__":
    unittest.main()