from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
    if markdown_block[0] == "#" and len(markdown_block.split(" ")[0]) < 7 and all(ch in "#" for ch in markdown_block.split(" ")[0]):
        return BlockType.HEADING
    elif markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return BlockType.CODE
    elif list(filter(lambda x: x[0] == ">", markdown_block.split("\n"))) == markdown_block.split("\n"):
        return BlockType.QUOTE
    elif list(filter(lambda x: x[:2] == "- ", markdown_block.split("\n"))) == markdown_block.split("\n"):
        return BlockType.UNORDERED_LIST
    else:
        split = markdown_block.split("\n")
        count = 0
        for i in range(len(split)):
            if split[i][:3] == f"{i + 1}. ":
                count += 1
            else:
                break
        if count == len(split):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH