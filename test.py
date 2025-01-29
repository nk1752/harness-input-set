def test():
    
  client: str = "Sales_and-Services"

  # Replace underscores and hyphens with spaces
  formatted_client = client.replace("_", " ").replace("-", " ")

  # Convert to title case, then lowercase the first letter
  formatted_client = formatted_client.title()
  formatted_client = formatted_client[0].lower() + formatted_client[1:]
  formatted_client = formatted_client.replace(" ", "")

  print(formatted_client)

  url: str = "https://www.google.com"
  url = url.removeprefix("https://")
  print(url)

if __name__ == '__main__':
    test()