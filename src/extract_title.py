def extract_title(markdown):
    blocks = markdown.split("\n\n")
    if blocks[0][:2] == "# ":
        return blocks[0].strip("#").strip()
    raise Exception("Website must have an h1 header")