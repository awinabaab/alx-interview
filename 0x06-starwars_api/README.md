# Star Wars API
  - HTTP Requests in JavaScript:

    - Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
    - A Complete Guide to Making HTTP Requests in Node.js

  - Working with APIs:

    - Understanding the basics of RESTful APIs and how to interact with them.
    - Parsing JSON data returned by APIs.
    - Working with APIs in JavaScript

  - Asynchronous Programming:

    - Managing asynchronous operations with callbacks, promises, and async/await syntax.
    - Handling API response data asynchronously.
    - Asynchronous Programming in JavaScript
  
  - Command Line Arguments in Node.js:

    - Using the process.argv array to access command-line arguments passed to a Node.js script.
    - How to Parse Command Line Arguments in Node.js

  - Array Manipulation and Iteration:

    - Iterating over arrays and manipulating data structures to format and display character names.
    - JavaScript Array Methods


## Files
### [0-starwars_characters](https://github.com/awinabaab/alx-interview/blob/main/0x06-starwars_api/0-starwars_characters.js)
A script that prints all characters of a Star Wars movie:

  - Usage: `./starwars_characters.js <movie_id>`
  - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
  - Displays one character name per line in the same order as the “characters” list in the /films/ endpoint
  - Uses the [Star wars API](https://swapi-api.alx-tools.com/)
  - Uses the request module
