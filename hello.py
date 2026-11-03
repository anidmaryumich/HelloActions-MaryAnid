import os

# read the WHO_TO_GREET variable and set default if variable isn't set
name = os.environ.get("WHO_TO_GREET", "World")
print(f"Hello {name}!")
print("This program is running inside Github Actions.")
