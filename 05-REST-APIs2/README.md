# Learning Goals
- Build and Execute GET <:id> Requests
- Discuss the Importance of Serializers
- Demonstrate How to Properly Set Up Serializers
- Demonstrate How to Use Serializers to Render Structured Data in API Responses
- Continue to Reinforce RESTful Conventions When Naming Routes
- Discuss Mass Assignment and How it Helps Improve Development Workflow
- Discuss the Importance of Handling Exceptions in the Controller and Demonstrate How to Do So for at Least One Action

# Lecture Topics
- Get-one
- SQLAlchemy-Serializer
- Serializing Relationships
- Serializing Associations


## Why should we use serializer?

### Current Problem:
- We have access to the Project model, and we want to access associated models like Roles and Actors. While we could create another endpoint for the user to review data, using a serializer is a better approach.

- Limitations of the `jsonify()` method include converting `SQLAlchemy objects` into `JSON objects` by obtaining a list of keys and values to pass to the client. This approach is not scalable, and jsonify can be finicky with Python objects.

## The Solution:
The solution lies in using `Flask-SQLAlchemy serializer`.

## Why Should We Use a Serializer?
 - Data Conversion: Serializers typically convert data into common formats like JSON (JavaScript Object Notation).
 - Accessing Associated Data: Our current response body may not show the associated relationship, but by using a serializer, we can achieve this.

 - SerializerMixin adds a `to_dict()` instance method, allowing us to utilize the `to_dict()` method in `app.py` and eliminating the need for repeatedly converting `SQLAlchemy objects` into `JSON objects`.