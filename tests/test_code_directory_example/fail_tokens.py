"""This is not functional code - it is used to test the code checking functions"""
import random

databricks_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

gitlab_token = "8h8qtkw98ce0v6nt3xku"

## commented token 8h8rtkw56ce0v6nt3xne

def generate_random_number():
  """Generates a random number between 1 and 100."""

  return random.randint(1, 100)

def print_random_number():
  """Prints a random number between 1 and 100."""

  random_number = generate_random_number()
  print(random_number)

def main():
  print_random_number()

if __name__ == "__main__":
  main()

def print_databricks_token():
  """Prints the Databricks token."""

  print(databricks_token)

if __name__ == "__main__":
  print_databricks_token()
