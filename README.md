# Fortune Teller
###### HW1 Questions:
What happens when you press the “submit” button? Paste the full URL you are sent to on submit.

What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?

What are the values of the URL query string? How do they correspond to what the user entered or typed?

* "http://127.0.0.1:5000/fortune_results?name=nicollle&siblings=666&thing=idk"
* the url directs you to /fortune_results/ with the values from the form in the url
* "name" is the text from the name text box. "siblings" is a number from the siblings text box. "thing" is the value from the thing select. 
* the values are: "nicollle" for the "name" field. "666" for the "siblings" field. "idk" for the "thing" field.

###### HW1 Stretch Challenge Question:

Is there a way to pass multiple values through the URL query string for a single key? How can we do so?
* arrays
---