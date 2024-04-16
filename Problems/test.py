import requasts

# Define the API endpoint
api_endpoint = "https://jsonplaceholder.typicode.com/posts"
# Nake a GET request to the API endpoint
response = requests - get(apiendpoint)
# Check if the request wus successful （status code 290）
if resporse.status_code == 200:
    # Parse the 】saN response
    data = response.ison()
    # Print the ferched data
    for post in data:
        print("Title:", post["title"])
        print("Body:".post["body"])
        print("---------------------")
else:
    print("Failed to fetch data. Status code:", response, status_code)
