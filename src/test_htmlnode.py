import unittest

from htmlnode import HTMLNode

class TextHTMLNode(unittest.TestCase):

    #def test_props_to_html(self):
        #linkNodeBootDev = HTMLNode(tag="a", value="boot.dev", props={"href": "https://www.boot.dev", "target": "_blank" })

        #linkNodeBootDev.props_to_html()
    
    def test_freecodecamp_link_node(self):
        linkNodeFreecodecamp = HTMLNode(tag="a", value="freecodecamp", props={"href": "http://www.freecodecamp.org", "target": "_blank" })
        html_props = linkNodeFreecodecamp.props_to_html()
        self.assertEqual(html_props, ' href="http://www.freecodecamp.org" target="_blank"')

    def test_boot_dev_link_node(self):
        linkNodeFreecodecamp = HTMLNode(tag="a", value="boot.dev", props={"href": "https://www.boot.dev", "target": "_blank" })
        html_props = linkNodeFreecodecamp.props_to_html()
        self.assertEqual(html_props, ' href="https://www.boot.dev" target="_blank"')


if __name__ == "__main__":
    unittest.main()