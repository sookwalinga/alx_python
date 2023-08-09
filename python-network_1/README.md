### Python - Network

1. **What a URL is**: A URL (Uniform Resource Locator) is a web address that specifies the location of a resource on the internet, including the protocol, domain, path, and other optional components.

2. **What HTTP is**: HTTP (Hypertext Transfer Protocol) is a protocol used for communication between web browsers (clients) and web servers. It enables the transfer of resources such as HTML pages, images, and files over the internet.

3. **How to read a URL**: Reading a URL involves understanding its components, such as the protocol (e.g., HTTP), domain name (e.g., example.com), path, query parameters, and fragments, if present.

4. **The scheme for a HTTP URL**: The scheme for an HTTP URL is typically "http://" or "https://", specifying how the resource should be accessed (unencrypted or encrypted).

5. **What a domain name is**: A domain name is a human-readable name that corresponds to the numeric IP address of a server hosting a resource on the internet.

6. **What a sub-domain is**: A sub-domain is a part of a larger domain, often used to organize and categorize content within a website (e.g., "blog.example.com").

7. **How to define a port number in a URL**: A port number can be defined in a URL using a colon followed by the port number (e.g., "http://example.com:8080").

8. **What a query string is**: A query string is a set of key-value pairs appended to a URL after a question mark, used to pass parameters to a web resource (e.g., "?name=John&age=25").

9. **What an HTTP request is**: An HTTP request is a message sent by a client (e.g., a web browser) to a server, specifying the action to be performed, such as retrieving a webpage.

10. **What an HTTP response is**: An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains the requested resource and additional metadata.

11. **What HTTP headers are**: HTTP headers are metadata included in both requests and responses, providing information about the data being sent or received, such as content type or authentication details.

12. **What the HTTP message body is**: The HTTP message body contains the actual content of the request (in POST, PUT, etc.) or the response (data like HTML, JSON) sent between the client and server.

13. **What an HTTP request method is**: An HTTP request method indicates the type of action the client wants to perform on a resource, such as GET, POST, PUT, DELETE, etc.

14. **What an HTTP response status code is**: An HTTP response status code is a three-digit number sent by the server to indicate the outcome of a request (e.g., 200 for success, 404 for not found).

15. **What an HTTP Cookie is**: An HTTP Cookie is a small piece of data sent from a server and stored on the client's side. It's often used for maintaining user sessions and remembering user preferences.

16. **How to make a request with cURL**: cURL is a command-line tool to make HTTP requests. You can use it to send various types of requests and retrieve data from URLs.

17. **What happens when you type google.com in your browser (Application level)**: At the application level, your browser sends an HTTP request to the server hosting Google's website. The server processes the request and sends back an HTTP response containing the HTML content of the Google homepage, which your browser then renders for you to see.

18. **How to fetch internet resources with the Python package urllib**: The `urllib` package in Python provides modules to fetch and manipulate URLs. You can use `urllib.request.urlopen()` to open a URL and read its content.

19. **How to decode urllib body response**: You can decode the response content obtained using `urllib` by using the `.decode()` method on the response object, specifying the appropriate character encoding.

20. **How to use the Python package requests**: The `requests` package in Python simplifies making HTTP requests. It provides easy-to-use methods to perform GET, POST, PUT, DELETE, etc., requests and handle responses.

21. **How to make HTTP GET request**: You can make an HTTP GET request using the `requests.get()` method in the `requests` package, passing the URL as an argument.

22. **How to make HTTP POST/PUT/etc. request**: You can make different types of HTTP requests like POST, PUT, DELETE using the corresponding methods like `requests.post()`, `requests.put()`, `requests.delete()` in the `requests` package.

23. **How to fetch JSON resources**: To fetch JSON resources, make an HTTP request using `requests.get()` and then use the `.json()` method on the response object to parse the JSON data.

24. **How to manipulate data from an external service**: After fetching data from an external service (e.g., via an API), you can manipulate it using Python's data processing tools, like dictionaries and lists, to extract, transform, and analyze the information as needed.
