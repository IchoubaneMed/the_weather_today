# the_weather_today

#### Video Demo: https://youtu.be/YduThxH4luc


this is a weather application based on the data provided by the OpenWeatherMap API, the languages used in this application are:

- HTML5
- CSS3
- JavaScript
- Python


beside these languages, i have used flask as core for this application, and leaflet library in order to render the map
So the basic of this application is pretty simple, the user type the name of the city that he want to know its weather the he click the search button 
as a result the application shows the the current weather in celsius relative the city with its location on the map 

the application contains the following folders & files:

- static:
    - logo.png (was made in Inkscape)
    - logo.svg (was made in Inkscape)
    - style.css (file that contains style for the application: font, colors, layout etc)
- templates:
    - base.html (the file that cotains the html boilerplate)
    - index.html (this file is inherted from the html boilerplate)
- app.py: this file contains the python which means the flask code 

**Why Inkscape ?**

Inkscape is a program for creating and editing vector graphics. It is ideal tool for drawing logos and icons, creating animatable graphics
for websites, for composing posters and flyers,

**What layout 'style' used?**

the layout used in the application based on flexbox, because flexbox is a powerful, well-supported layout method that was introduced with 
the latest version of CSS which is CSS3. With flexbox, it's easy to center elements on the page and create dynamic user interfaces that shrink
and expand automatically.

**Why Flask ?**

Flask gives the developer varieties of choice when developing web application, it provides you with tools, libraries, and mechanics that allow
you to build a web application. The web application can be a blog, commmercial website or some pages, it still allow the developers the opportunity
to use some extensions provided by the community that allows you to add mor functionality to the web application.


The template used in this application based on the Jinja2. Which is a Python template engine used to create both HTML and XML documents format
the template of this application is divided on three major blocks (header, body, and footer) the header encapsulates the navbar, the body
encapsulates the card and the map, the last block is for the footer. 



**the file app.py**

This file contains the Python code, at the bove i imported the Flask module, requests, and render_template
after set up the flask app, i created the function index() inside this function there are two blocks created by the if else statement
so inside the first block 'if' i created the variable 'formCity' this variable will get the name of the city typed by the user
then this variable will be used inside a formated string that contains the API key of the OpenWeatherMap in order to get the data relative to the
city, after that i casted the response of the API into the JSON format then i created the 'curWeather' dictionary, in order to get the name,
temperature, description, icon, lan, and log of the city. After i created the curWeather dictionary i sent it to the index.html template using for that
the render_template function that i imported at the beginning.



