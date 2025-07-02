from htmlnode import LeafNode, ParentNode

from md_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from raw_md_to_text_nodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block != "" and block != None:
            blocktype = block_to_block_type(block)
            if blocktype != BlockType.CODE:
                mod_block = block.replace("\n", " ")
                textnodes = text_to_textnodes(mod_block)
                htmlnodes = []
                for t in textnodes:
                    htmlnodes.append(text_node_to_html_node(t))
            if blocktype == BlockType.HEADING:
                count = 1
                while block[count] == "#":
                    count += 1
                block_nodes.append(ParentNode(f"h{count}", htmlnodes))
            elif blocktype == BlockType.CODE:
                text = block[4:-3]
                block_nodes.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, text)],),]))
            elif blocktype == BlockType.QUOTE:
                block_nodes.append(ParentNode("blockquote", htmlnodes))
            elif blocktype == BlockType.UNORDERED_LIST:
                mod_htmlnodes = []
                for node in htmlnodes:
                    mod_htmlnodes.append(ParentNode("li", node))
                block_nodes.append(ParentNode("ul", mod_htmlnodes))
            elif blocktype == BlockType.ORDERED_LIST:
                mode_htmlnodes = []
                for node in htmlnodes:
                    mode_htmlnodes.append(ParentNode("li", node))
                block_nodes.append(ParentNode("ol", mod_htmlnodes))
            else:
                block_nodes.append(ParentNode("p", htmlnodes))
    return ParentNode("div", block_nodes)
