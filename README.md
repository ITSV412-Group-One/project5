# project5
Group project #5: Build a REST API
The goal of this project will be to build a simple REST Links to an external site. API [1 Links to an external site., 2 Links to an external site.] in Python. You are free to use any Python web framework you want, but I strongly recommend Flask (http://flask.pocoo.org

Links to an external site.) for its simplicity and ease of use. Your API should run on port 4000, and expose the following URIs:

/md5/<string>
This endpoint will return the MD5 hash of the string that is passed as the input. Ex.: for a string of Hello World the MD5 hash should be b10a8db164e0754105b7a99be72e3fe5. Don’t forget to handle spaces and other special HTTP characters correctly!

/factorial/<int>
This endpoint will return the factorial (product of the integer and all integers below it) for the integer that is passed as input. If the input is not a positive integer, the output should contain and error description.

/fibonacci/<int>
This input will return an array of integers with all the Fibonacci numbers (in order) that are less than or equal to the input number. If the input is not a positive integer, return an error description. 

/is-prime/<int>
This endpoint will return a boolean value depending on whether the input is a prime number. Again, return a descriptive error if the input is invalid.

/slack-alert/<string>
This endpoint is the only one that has a side-effect. Your API should attempt to post the value of the input into a Slack channel in our class Slack team, then return a boolean value that indicates whether the message was successfully posted to the channel. 

Each URI endpoint should return the same result: a JSON

Links to an external site. payload that consists of an input and an output value. The data type of the two values should vary depending on the endpoint that is being called, like this example for the /factorial/ URI:

{
  "input": 4,
  "output": 24
}

I will be automating the grading of this assignment using a script that test the JSON output for an expected result, given a regular input set. I would suggest you assign one or two members of your team to build your own automated test script so that you can be sure that what I do will perform as expected, and to try and come up with various test inputs that might cause your API to break.

The grade for this project will rest on the following criteria:

    Does the Python project build and run?
    What percentage of my automated tests pass (meaning that the HTTP status and JSON output returned matches what my tests expect for any given URL)?
    What does the electronic record of group collaboration in both GitHub and Slack tell me about your team affinity and effectiveness?
