# Project-4 Django Blog Website


This Blog Website Django app is a powerful web application designed to facilitate the creation, management, and sharing of blog posts. With a comprehensive set of features, the app offers a complete solution for bloggers, content creators, and website owners.
Overall, the Blog Website app provides a powerful and comprehensive solution for anyone looking to create, manage, and share their blog content in a secure and flexible manner.

<img src="staticfiles/images/homepage.PNG">

Project Summary and Main Features
================

  + Crud operation on blogs
  + Custom user model
  + Registration
  + Authentication through username plus email
  + Personal profile management
  + Filter blogs by different criteria (title, category, tags)
  + Search blogs by different criteria
  + Like blogs
  + Comment and replies on blogs
  + Follow unfollow other users
  + Notification system
  + Mute unmute notifications
  + Feedback functionalities


Click here to view website: [Blog](https://project-4-blog.herokuapp.com/)


# UXD - User Experience Design

Epic 1: Blog Management
+ As a user, I want to be able to perform CRUD operations on blogs so that I can create, read, update and delete my own blogs or blogs of other users.

User Stories
+ As a user, I want to be able to create a new blog post so that I can share my ideas with others.
+ As a user, I want to be able to edit my existing blog post so that I can make changes to my post whenever I want.
+ As a user, I want to be able to delete my own blog post so that I can remove any unwanted posts from my profile.
+ As a user, I want to be able to view other users' blog posts so that I can read and learn from them.
+ As a user, I want to be able to filter the blogs by different criteria such as title, category, and tags so that I can easily find the blogs of my interest.

Epic 2: User Management
+ As a user, I want to be able to manage my personal profile and interact with other users in the platform.

User Stories
+ As a user, I want to be able to register on the platform using my email and password so that I can create an account and use the platform.
+ As a user, I want to be able to update my profile information such as name, profile picture.
+ As a user, I want to be able to search for other users on the platform so that I can connect with them.
+ As a user, I want to be able to follow/unfollow other users so that I can stay updated with their latest blog posts.
+ As a user, I want to be able to like and comment on other users' blog posts so that I can interact with them.
+ As a user, I want to be able to receive notifications for activities such as likes, comments, and follows so that I can stay informed.
+ As a user, I want to be able to mute/unmute notifications so that I can customize my notification settings according to my preferences.

Epic 3: Security and Authentication
+ As a user, I want my data to be secure and my account to be authenticated through multiple means.

User Stories
+ As a user, I want to be able to login using my email and password so that I can access my account.
+ As a user, I want my account to be authenticated through both username and email so that my account is more secure.
+ As a user, I want my password to be encrypted and my account information to be secure so that my data is safe from unauthorized access.

Epic 4: Blog Interaction
+ As a user, I want to be able to interact with other users' blog posts by commenting and replying to comments.

User Stories
+ As a user, I want to be able to comment on other users' blog posts so that I can express my thoughts and opinions.
+ As a user, I want to be able to reply to other users' comments so that I can continue the conversation and engage with the community.
+ As a user, I want to be able to like other users' comments so that I can express my agreement.
+ As a user, I want to be able to receive notifications for new comments and replies on my blog posts so that I can stay engaged with the community.

Epic 5: Advanced Search and Filtering
+ As a user, I want to be able to perform advanced searches and filtering on blogs based on various parameters.

User Stories
+ As a user, I want to be able to search for blogs based on advanced parameters such as author and keyword.

Epic 6: Feedback and Support
+ As a user, I want to be able to give feedback and receive support from the admin so that I can improve my experience on the platform.

User Stories
+ As a user, I want to be able to contact the admin through a support form so that I can report bugs or suggest improvements.
+ As a user, I want to be able to receive timely and helpful responses from the admin so that my issues can be resolved quickly.
+ As an admin, I want to be able to track user feedback and support requests so that I can improve the platform based on user needs.

Epic 7: Admin Panel Access
+ As an administrator, I want to be able to access the admin panel easily, so that I can manage the website efficiently.

User Story
+ As an administrator, I want to see a button that takes me to the admin panel when I'm logged in, so that I can quickly access the tools I need to manage the website. When I click the button, it should take me directly to the admin panel without requiring additional logins or authentication.

Epic 8: Feedback Page
+ As an administrator, I want to have quick access to the feedback page without going through the admin panel.

User Story
+ As an administrator, I want a button to appear on the navigation bar when I log in to the system, so that I can easily access the feedback page without navigating to the admin panel. The button should only be visible to me as an admin user, and clicking on it should take me directly to the feedback page.


## Agile Methodology
This application was developed using agile methodology. 

<img src="staticfiles/images/agile8.PNG">


# Design

The color palette chose is blue and white. It is a popular combination that can evoke a sense of calmness, professionalism, and simplicity.
White is a neutral color that can help create a clean and modern look for a website. It also provides a blank canvas that can be complemented with other colors to add emphasis or contrast.
Blue, on the other hand, is often associated with trust, stability, and intelligence. It can convey a sense of security, which makes it a popular choice for corporate and financial websites. Blue can also be used to create a sense of depth and serenity, making it a popular choice for websites related to wellness, health, or technology.
When used together, blue and white can create a sophisticated and elegant aesthetic that can be easily associated with professionalism and quality. The combination is a classic choice for businesses, organizations, and individuals looking for a timeless and reliable look for their website.


# Features


### Navigation Bar
The navigation bar is fixed at the top of every page and includes links to other pages and a search box(searching posts).
The link for the current page is shown in grey to visually indicate which page the user is on.
<img src="staticfiles/images/nav.PNG">

### Home Page

The home page contains the nav bar with all relevant links (Home, Blogs, Category, User), in the body we have the most recent post (with the ability to scroll right/left) and the footer containing links to the social media websites (Facebook, Twitter, Linkedin) and a Send Feedback link.

<img src="staticfiles/images/home.PNG">
<img src="staticfiles/images/footer.png">


### Blogs Page

This Page shows the latest blog posts.

<img src="staticfiles/images/blogs.PNG">


### Sign Up Page

Sign Up page is accessed from the Login page on the sign up button. 
Users can enter their details here to register and log in. 

### Log In Page

Log In page is accessed from the Log In link on the navigation bar, which is available to users who are not logged in already.
Returning users can enter their details here to log in to avail of all the features.

<img src="staticfiles/images/log.PNG">


### Category

The category button is a dropdown menu which can be used as a filter by category

<img src="staticfiles/images/categories.PNG">

### User(User name after login in)

The user button appears when you are logged in and it is a dropdown menu which includes: "My profile", "Notifications" and "Logout" options.

<img src="staticfiles/images/users.PNG">

My Profile: The users can edit their details from here:
<img src="staticfiles/images/profile.PNG">
Using the My blogs page, users can view, edit and delete their posts.
<img src="staticfiles/images/myblogs.PNG">
Using the Add blog page, users can create new posts.
<img src="staticfiles/images/add.PNG">


### Notifications

From the notifications page you can view notifications regarding your posts(i.e another user liked your post or started to follow you.)

<img src="staticfiles/images/notifications.PNG">



### Footer
The footer includes links to Facebook, Twitter and LinkedIn plus a link where user can send feedback to the admin. 
<img src="staticfiles/images/footer.png">
<img src="staticfiles/images/f.png">
<img src="staticfiles/images/t.png">

### Follow/Unfollow and Mute/Unmute notifications
You can as well follow/unfollow other users and mute/unmute notifications:
<img src="staticfiles/images/follow.PNG">

### Comment and like on other users posts
There is a functionality built, which allows other user to comment and like your posts:
<img src="staticfiles/images/comment.PNG">


### Feedback and Admin Panel buttons
When logged as an admin, the user will have two more buttons, one in the nav bar, where they can easily see the feedback from other users and one on the top left, where they can easily access the admin panel.

<img src="staticfiles/images/feeds.PNG">


### Custom Error Pages
<img src="staticfiles/images/404.PNG">
<img src="staticfiles/images/500.PNG">


# Technologies Used

## Languages
* [HTML](https://html.spec.whatwg.org/) was used to create the content and structure for the application.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) was used to add styling to the application.
* [Python](https://www.python.org/) was used to add functionality to the application.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to create interactive content for the application.

## Frameworks, Libraries and Tools Used within the Application
* [Django](https://www.djangoproject.com/) was used as the main Python framework for the application.
* [ElephantSQL](https://www.elephantsql.com/) was used for the Production database.
* [Cloudinary](https://cloudinary.com/) was used initialy to store all static files and images. I had quite a challenging time with this as it wasn't reading all my CSS, not able to show "fontawesome" icons and some characters in the Description table(they all work perfectly on local), therefore I took the decision to use instead [Withenoise](https://whitenoise.readthedocs.io/en/latest/), only to realize later that you can't upload images on whitenoise, so what I did next was to use both Cloudinary (to store the images) and Whitenoise (to store the rest of the static files).
* [Git](https://git-scm.com/) was used for version control and tracked changes in the codes.
* [GitHub](https://github.com/) was used to store the repository and the codes.
* [Gitpod](https://www.gitpod.io/) was used to create, edit and preview the codes during the development.
* [Heroku](https://id.heroku.com/login) was used to deploy the application.

## Validation
* Lighthouse for performance check:

<img src="staticfiles/images/lighthouse.PNG">

* [W3C HTML Validator](https://validator.w3.org/) was used to validate HTML codes.

<img src="staticfiles/images/html2.PNG">
<img src="staticfiles/images/html3.PNG">

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS codes.

<img src="staticfiles/images/css1.PNG">
<img src="staticfiles/images/css2.PNG">

* [JSHint](https://jshint.com/) was used to validate JavaScript codes.

<img src="staticfiles/images/js1.PNG">
<img src="staticfiles/images/js2.PNG">

* [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate Python codes.

<img src="staticfiles/images/py1.PNG">
<img src="staticfiles/images/py2.PNG">


## Manual Testing

Crud Operation on Blogs
+ All CRUD operations (Create, Read, Update, Delete) are working correctly.
+ Create operation is correctly adding new blogs to the database with all the required fields.
+ Read operation correctly displays all blogs on the main blog page.
+ Update operation is correctly editing and updating blog posts in the database.
+ Delete operation is correctly deleting blog posts from the database.
+ All CRUD operations are correctly functioning on both the admin and user side.

Custom User Model
+ Custom user model is correctly implemented and is functioning correctly.
+ New users can be created with all the required fields.
+ User authentication is correctly implemented with the custom user model.
+ User profiles are correctly linked to the custom user model and can be accessed by the user and the admin.
+ All user information is correctly stored in the database and can be edited and updated.

Registration
+ User registration is correctly implemented and working.
+ All required fields for registration are correctly validated and stored in the database.
+ Duplicate username and email addresses are correctly rejected.
+ Error messages correctly display if any field is not valid.

Authentication through Username Plus Email
+ User authentication through username and email is correctly implemented and working.
+ Users can log in using either their username or email and their password.
+ Error messages correctly display if login credentials are not valid.

Personal Profile Management
+ Personal profile management is correctly implemented and working.
+ All user profile information is correctly stored in the database and can be edited and updated.
+ Users can correctly view their profile and change their profile picture.
+ Users can correctly update their password.

Filter Blogs by Different Criteria (Title, Category, Tags)
+ Filtering blogs by different criteria is correctly implemented and working.
+ Users can correctly filter blogs by title, category, and tags.

Search Blogs by Different Criteria
+ Searching blogs by different criteria is correctly implemented and working.
+ Users can correctly search blogs by keywords.

Like Blogs
+ Liking blogs is correctly implemented and working.
+ Users can correctly like blogs and the number of likes is correctly reflected on the blog page.

Comment and Replies on Blogs
+ Comments and replies on blogs are correctly implemented and working.
+ Users can correctly add comments and replies to blog posts.
+ All comments and replies are correctly stored in the database and are correctly displayed on the blog page.

Follow Unfollow Other Users
+ Follow unfollow functionality is correctly implemented and working.
+ Users can correctly follow and unfollow other users.
+ All follow and unfollow actions are correctly stored in the database.

Notification System
+ Notification system is correctly implemented and working.
+ Users correctly receive notifications for new comments, replies, and followers.
+ All notifications are correctly stored in the database.
+ Users can correctly view all their notifications.

Feedback Functionalities
+ Feedback functionalities are correctly implemented and working.
+ Users can correctly submit feedback using the feedback form.
+ All feedback is correctly stored in the database and can be accessed by the admin.
+ Admin can correctly view and manage all feedback submissions.



### Deployment - Heroku
The following are the steps to deploy the application on Heroku.

1. Create a repository in GitHub using [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Open GitPod from the newly created repository
3. Install Django and supporting libraries:
4. Create requirements.txt
5. Create a Django project
6. Create an app
7. Add the newly created app into settings.py
8. Migrate the Changes
9. Run the server to verify that the basic skelton project is now up and running
10. Create an app in [Heroku](https://dashboard.heroku.com/login)
11. Create a database in [ElphantSQL](https://www.elephantsql.com/)
12. Create an env.py
13. Modify settings.py file
14. Migrate Database Structure to the ElephantSQL database
15. Push the Changes to GitHub
16. Set Up Cloudinary and Whitenoise
17. Set up Heroku Config Vars
18. Update settings.py
19. Create Static Files
20. Create Procfile
21. Push the Changes to GitHub
22. Deploy the app in Heroku


 ## Credits
 This tutorial helped me put the base of my Django project, it's a great tutorial explaining step by step how to build a project like this [Django Tutorial](https://www.youtube.com/watch?v=WpyXXBTcERc&list=PLFIUQuoVboS-nnEsyVYuwS0S1-tQJRwc8&index=8&t=13s&ab_channel=NabilMoiun)

 I used [this repository](https://github.com/mikyrenato/happy-beans) to inspire myself when creating the readme file.

 I also used the following online resources:

- [Code Institute](https://codeinstitute.net/ie/)
- [Slack](https://slack.com/intl/en-ie/) 
- [Stack OverFlow](https://stackoverflow.com)
- [YouTube](https://www.youtube.com/)
- [W3Schools.com](https://www.w3schools.com/)
- [Chat GPT](https://chat.openai.com/)

<br>

----
 ## Acknowledgements

 Many thanks to my mentor Harry Dhillon for his guidance and support and to my friend Marcin Placek for helping me with the testing of the website.
