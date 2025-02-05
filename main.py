from exa_py import Exa

exa = Exa('7dd52fee-c155-4ff1-9427-8ca7e949a6a1')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

print(response)