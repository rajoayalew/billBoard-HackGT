## Inspiration
From the beginning, our team was driven to create an application to improve the quality of life and accessibility of daily services. After researching issues experienced by vulnerable populations and minority groups in healthcare and medicine, we came to the realization that medical bill transparency is a major issue across the United States.

## What it does
billBoard creates a more equitable healthcare system, one bill at a time. billBoard increases transparency in medical costs by collecting and comparing data on the most common medical procedures and their average pricing in different states across the country. The billBoard platform features data collection, analysis and verification, and comparison of medical bill data, contributed by our diverse user community. By analyzing and presenting this data, billBoard can be used to help users better understand their expected medical bill costs.

Users are able to “post a bill” with information from their previous medical bills to add to the “billBoard,” where other users are able to search for medical bills of particular procedures. All posts are anonymous and the data of each user is not shared.

Currently, billBoard takes in data from the “post a bill” website form once a user inputs information about their relevant medical experience (their “bill”). This data is then sent to a server-side relational SQL database using the HTML Post Request API. This API can write to and receive information from the database, where bill information is stored. 

As of now, the website is only able to display static medical bill information pre-generated from a Python script on the “billBoard” for a specific test case. Our team is passionate about billBoard and hopes to create a working search function to retrieve dynamic data from the database and display it on the website in real-time.

## How we built it
The billBoard website was built from a Bootstrap template with customized HTML/CSS and Javascript, taking inspiration from Figma, Google Fonts API, and Coolors.co. Express.js, Node.js, and an SQL (SQLite) database were used in the backend. 

Our team also built a Python script to automatically generate thousands of statistically-correct random numbers in order to imitate realistic user entries for the billBoard.

## Challenges we ran into
Initially, our team planned to use PyScript (Python in HTML) as the interface between the input form and the database. However, PyScript requires the entire database to be on the client side, so it would not be compatible with a web app.

With only ten hours left until the submission deadline and the backend yet to be assembled, we decided to switch routes and use Node.js and Express.js to build the backend. After self-teaching both frameworks and rebuilding the backend, the frontend was reconfigured to seamlessly connect the SQL database and the datasets. In the future, our team hopes to create a working search function to retrieve dynamic data from the database and display it on the website in real-time.

## Accomplishments that we're proud of
Our team is extremely proud of our collaboration, flexibility, and passion during HACKGT. When  things did not go as initially planned, the team was able to quickly pivot and take the development in a completely different direction, even with little time remaining.

Most of all, we are proud of how we leveraged each members’ unique skills and abilities to cooperate and make a significant, fulfilling final product.

## What we learned
Over the course of 36 hours, our team learned to continue adjusting and improving to new situations and challenges. We learned to face problems head on, including Javascript.  At the beginning, our team planned to use PyScript to interact with web pages instead of using Javascript. However, there were some limitations with PyScript, which led us to rewrite the entire backend of the project with ten hours to spare. Even so, the team was able to adapt by self-teaching Node.js and Express.js while pressed for time. In the end, billBoard regained almost all functionality.

## What's next for billBoard
billBoard’s journey does not end with HACKGT. Our team is passionate about billBoard and hopes to create a working search function to retrieve dynamic data from the database and display it on the website in real-time. In addition, we want to increase the functionality by adding additional fields, such as insurance providers and hospitals, providing a wider range of statistics, and building data visualization. Other goals include hosting the website on the public domain, applying a cost-breakdown analysis, and implementing computer vision so data does not have to be manually entered.
