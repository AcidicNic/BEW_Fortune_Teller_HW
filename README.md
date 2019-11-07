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
###### HW3 Questions:
Describe the data contained in the API response. What can we discern about the weather in the specified city?

How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)
* 
* To get the temperature in the specified city, we would set a var equal to the city name and pair it with the key 'q' when we send the request. Also maybe pair 'units' with 'imperial' so the temp isn't in kelvin. then do this:

```python
degrees = json_response["main"]["temp"]
```