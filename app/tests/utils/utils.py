import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_placekitten_url() -> str:
    return (
        f"https://www.placekitten.com/{random.randrange(1, 100)}/"
        f"{random.randrange(1, 100)}"
    )
