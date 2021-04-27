# [Django-Blog](http://prechy-blog.herokuapp.com)

This project is a simple django blog creating using mainly ClassBasedViews

## Features

- A `blog` app which is the main component of the blog adding new posts and comments and displaying them to the user.

- An `accounts` app for registration and login

- A `Post` model that creates a new post with `author', `title` and post `body`.

- A  `Comment` model that creates a new Comment object using `post`, `author` and `comment`.

- A home page showing posts

- A post page showing post title, body and comment section

 -  A delete post page 

 -  An edit post page

 -  A register page (a new user can register, their details stored in a database file). 

-    login (checks in the file and logs them in if they are already registered)

-    reset password

-    logout

-    A comment section, you must be logged in to comment

### Database used
SQLite

### Deployment
http://prechy-blog.herokuapp.com/

