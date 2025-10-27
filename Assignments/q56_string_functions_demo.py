if __name__ == "__main__":
    s = "  Hello, World! 123 "
    print(f"Original: {repr(s)}")

    # Case transformations
    print("upper:", s.upper())
    print("lower:", s.lower())
    print("title:", s.title())
    print("capitalize:", s.capitalize())
    print("swapcase:", s.swapcase())
    print("casefold:", s.casefold())

    # Whitespace
    print("strip:", repr(s.strip()))
    print("lstrip:", repr(s.lstrip()))
    print("rstrip:", repr(s.rstrip()))

    # Searching and counting
    print("find('World'):", s.find("World"))
    print("index('World'):", s.index("World"))
    print("count('l'):", s.count("l"))
    print("startswith('  He'):", s.startswith("  He"))
    print("endswith('123 '):", s.endswith("123 "))

    # Replace and split/join
    print("replace('World', 'Python'):", s.replace("World", "Python"))
    parts = s.split(",")
    print("split(','):", parts)
    print("join with '-':", "-".join([p.strip() for p in parts]))

    # Alignment and padding
    core = s.strip()
    print("center(20,'*'):", core.center(20, "*"))
    print("ljust(20,'-'):", core.ljust(20, "-"))
    print("rjust(20,'-'):", core.rjust(20, "-"))
    print("'42'.zfill(5):", "42".zfill(5))

    # Tests
    t = "Python3"
    print("isalpha on 'Python3':", t.isalpha())
    print("isdigit on '123':", "123".isdigit())
    print("isnumeric on 'Ⅷ':", "Ⅷ".isnumeric())
    print("isalnum on 'abc123':", "abc123".isalnum())
    print("isspace on '  ':", "  ".isspace())

    # Formatting
    name, score = "Alice", 95.678
    print("format:", "Name: {}, Score: {:.2f}".format(name, score))
    print("f-string:", f"Name: {name}, Score: {score:.2f}")