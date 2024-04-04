from generate_page import generate_pages_recursive
from static import copy_static

def main():
    copy_static()
    generate_pages_recursive("content", "template.html", "public")
main()