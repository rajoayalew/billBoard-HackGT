## Inspiration

## What it does
billBoard increases transparency in medical costs by crowd sourcing data on procedures and pricing from around the country. Users are able to upload how much certain common medical procedures cost them in order to create a searchable database for patients to know whether or not they are paying too much. Users are able to search by procedure and filter by state to see what other people paid as well as the median cost of the procedure. Greater transparency in the cost allows for patients to be better educated about their procedures and to protect them from predatory practices from hospitals and insurance companies trying to line their pockets. 

## How we built it
We used a Bootstrap template for the UI that was paired with JavaScript, Node.js, and a SQLite database back end. The user inputs data into the form which is then inserted into a server side relational database. The user can then search the data where the SQLite table is queried and gives the entries that match the search to then be displayed by the front end. In order to test functionality, a python script was used to generate thousands ofrandom but still realistic user entries from around country. 

## Challenges we ran into
Because we did not have much experience with JavaScript, we initially tried to have PyScript (python in HTML) be the interface between the input form and the database because we were more comfortable with python. PyScript was not a good tool to use for this as it would have required the entire database to be on the client side to be used. This system was flawed in that there was no real front end and back end and could not be used as a web app. We were guided by one of the mentors to abandon the PyScript route with only 10 hours left until the deadline, and we had to then teach ourselves JavaScript and Node.js, and how to actually set up a front end and back end. 

## Accomplishments that we're proud of
We are reallly proud of how flexible we were when our initial plans did not work out. Even though we had spent so much time in PyScript, we were still able to pivot quickly and take the development in a whole new direction without much time left. We are also proud with how we planned as we went and how well we worked together as it allowed us to make the big change in the end. 

## What we learned
We learned that whatever seems the easiest probably has some pitfalls and to properly research what we are trying to do before commiting to something. We used PyScript simply because we did not have a lot of JavaScript experience, even though that is what is used in most websites like this. We should have properly looked into the functionality of PyScript rather than just using it because we knew python. We also learned a lot of JavaScript in the last 10 hours and how to set a proper back end and front end for a website. 

## What's next for billBoard
We want to uncrease the functionality by adding fields for more data to be entered as well as more statistics about the data. More statistics than just the median will paint a better picture about the data. More data will allow us to also add more visualizations to the data like a map. We also want to be able to support any procedure and we want to properly implement the breakdown feature where you can enter in the full cost breakdown of each component procedure. We would also like to impliment bill scanner so users don't have to manually enter in all of the information. 

## Video Script
Welcome to billBoard, a platform built on the idea that each person should have a honest representation of their medical bills. On the pl