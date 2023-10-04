# REST APIs with Flask (Part 1)

## Learning Goals
- Review API Fundamentals
- Discuss MVC Architecture and Reinforce Patterns / Best Practices
- Introduce RESTful Routing
- Build and Execute GET / POST Requests
- Introduce and Use Postman to Interact with APIs


## Lecture Topics
- Introduction to APIs
- Command Line Flask
- MVC Architecture
- RESTful Routing Conventions
- Testing APIs with Postman
- GET/POST


    # API Fundamentals
    # MVC Architecture and Patterns / Best Practices
    # RESTful Routing
    # Postman

https://flask-slide.netlify.app/slides/001-intro/

# What is API (Application Programming Interface)?
- a set of rules and protocols that allows different software applications to communicate with each other.
- RESTful APIs 
- SOAP APIs: SOAP (Simple Object Access Protocol) uses XML, known for typing, complex operations.
- Web APIs: enable web applications, mobile apps to access remote services or data.

# What is RESTful API?
- pokemonAPI, googleAPI, They are all built in a very specific way. 
- This client and server request response cycle is part of rest.
- RESTful APIs: Representational State Transfer (REST) is a popular architectural style for designing APIs
- Based on standard HTTP methods (GET, POST, PUT, DELETE) 
- Stateless principle: each request from a client to the server must contain all the information needed to understand and process the request.
- Resource-based endpoints, JSON or XML
- Use of HTTP Status Codes: RESTful APIs use HTTP status codes to indicate the outcome of a request (e.g., 200 OK for success, 404 Not Found for a missing resource, 500 Internal Server Error for server issues).

# Restful HTTP verbs / HTTP method

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|


### Status Code
- Status codes to indicate the outcome of a request
- https://http.cat/

# | #        	|    Description       	|   
# |-----------	|:----------------:	    |
# | 200       	|   Successful  	    |   
# | 401       	|   Unauthorized 	    |   
# | 404      	|   Not Found   	    |   
# | 405      	| Method not Allowed    |   
# | 500     	|Internal Server Error  | 

# MVC in Flask
MVC (Model-View-Controller) architecture separates an application into three key components: 
- Models interact with data sources
- Views format the response for the client based on the HTTP request and routes
- The Controllers act as an intermediary between the Model and View. It receives user input from the View, processes it, updates the Model, and updates the View accordingly.