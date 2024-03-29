


# <p align=center> <a name="top">Instagram---Django-project </a></p>  

This is the first version of the Instagram project on my github. If you want to check out the next version which is fully based on Django Rest Framework [click here.](https://github.com/krzysztofgrabczynski/Instagram---DRF-project)

Additionaly, you can find here 2 branches:
- main branch, is an improved version of the project, based on classes, splitting applications, using many tools, etc.
- old_version branch, holds the original version of the project. Simple, based on funtions, without many tools and methodologies (it was my first project based on Django)

## Description
It's a simple social media site inspired by Instagram. If you want to use this kind of Instagram, you have to sign up. Then, you have some options. You can follow someone if you want to see what posts that particular user is posting, you can add comment below any post and use thumb up option. All data changes dynamically. Bootstrap templates and partially ready-made html/css models were used in this application because the creation of this project is mainly focused on the backend functionalities using Django. 

Unit tests in progress...

If you want to check out my other projects [click here.](https://github.com/krzysztofgrabczynski)

## Tools used in project

<p align=center><a href="https://www.python.org"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/></a> 
<a href="https://www.djangoproject.com/"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="60" height="60"/> </a>
<a href="https://git-scm.com/"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git" width="60" height="60"/> </a> 
<a href="https://aws.amazon.com/"> <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" alt="aws" width="60" height="60"/> </a>
<a href="https://www.postgresql.org.pl/"> <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/postgresql/postgresql-original-wordmark.svg" alt="psql" width="60" height="60"/> </a>
<a href="https://www.docker.com/"> <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/docker/docker-original-wordmark.svg" alt="docker" width="60" height="60"/> </a>
<a href="https://python-poetry.org/"> <img src="https://github.com/python-poetry/website/blob/main/static/images/logo-origami.svg" alt="redis" width="60" height="60"/> </a></p>

## Preview
<p align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217864503-6da8f31e-a7a7-4ad5-9adc-1f9e1229245e.gif">
</p>


## Install for local use (using Docker)
- Clone the repository
- Create .env file and add requirement variables such as 'SECRET_KEY' or database parameters
- Build the Docker image using ``` docker-compose build ```
- Run containers using ``` docker-compose up ```
- Everything done! 

## Install for local use (using poetry)
- Clone the repository
- Create .env file and add requirement variables such as 'SECRET_KEY' or database parameters
- Enter the ``` poetry install ```
- Now enter the ``` poetry shell ``` to open virtualenv and start app with ``` python manage.py runserver ```
- Everything done! You can open Instagram app in your browser by ctrl + left click on http link in your console

For local use without Docker, you also need to configure Postgres and Poetry



## Features
In this version, you can do some specific stuff, here is list of the most important features:
- [x] [log in on account or if you don't have, sign up](#loggin-and-sign-up)
- [x] [change some stuff e.g. edit password, edit account (name, email etc.), edit profile (gender, profile img, description)](#user-settings)
- [x] search for a profile of someone else using search bar
  - [x] [then, follow specific user or unfollow](#follow-and-unfollow)
- [x] move to the home page by clicking on the 'Instagram' and add new post
- [x] on the profile check some dynamic information like number of posts, followers, following and your own posts
- [homepage functionality:](#homepage-functionality)
  - [x] on the home page you can see your posts and posts of the followed users
- [posts functionality:](#post-functionality)
  - [x] use thumbs up option under the post and check the list of users who gave likes
  - [x] owners of the posts, can delete the post or edit (this options will be shown only for post owner)
  - [x] make a comment, it will be show below the post with your personal data, date of creation and deletion option

<br><br>



## Loggin and sign up
Your first step using this application is to sign up. You have to fill all fields and set password according to the presented rules (password authentication is provided by Django).
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217618679-a96ca44d-50f7-4fd9-940a-dd87014625c8.png"/>
</p>
If you have an account, you can logg in. If you make any mistake, you will be informed about it.
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217618696-c1c998a2-c8f6-475d-a0b4-c4bf381c484a.png"/>
</p>

[Go to top](#top) 
  
  
## User settings
After loggin, you will se navbar menu with options like: logout, settings, profile, search and Instagram. When you click the settings button you will see dropwon menu with options to change data about your account.
<p  align="center">
  <p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217619210-6daeaffb-4c21-4c0b-a4b5-1f32a9cee7b6.png"/>
</p>
In the profile settings, you can change your gender, add a description and set any profile picture. Field 'description' is required, so you have to fill it.
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217619310-dbd1e39f-c0ae-4712-9c7f-56cbd5d44d20.png"/>
</p>
In the account settings, you can change your personal data (all forms are generated by bootstrap-forms)
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217619338-ddb0b0dd-e29b-4214-bfee-c3fd039a9779.png"/>
</p>
In the edit password tab you can change your password. Verification is provided by Django Authentication Views.
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217619364-8f24be64-6778-420f-aed2-64bb7307deb1.png"/>
</p>
After first loggin, your account looks like this one. Profile picture is set by default.
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217624866-6059fb5c-ac73-467d-89b4-daa5570513d3.png"/>
</p>
Below, you can see profile with a sample profile image and description. Posts, Followers and Following are all set to zero.
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217624876-dd8b50e1-116b-44ca-9edb-dcaa8063566e.png"/>
</p>

[Go to top](#top) 


## Follow and unfollow 
You can use the user search bar to find someone. All you have to do is enter the specific username you want to check and click "Search". Then, just click the 'Follow' under the user's profile image if you want to have that user's posts visible on your homepage. After clicking, Follow button will change to Unfollow button and number of followers will increase. You can check followers and following by clicking on the dynamic numbers on the user profile (it will be shown as modal window with users names)


[Go to top](#top) 


## Homepage functionality
On the home page, you have several options such as adding a new post, navigate using the menu navbar at the top, and checking your posts and the users you follow (posts are ordered by creation date). As you can see at gif below, user named Mary can scroll homepage through posts (own posts, and followed users).
![home_page](https://user-images.githubusercontent.com/90046128/217638004-cbe80f09-4247-4f32-90b2-a4c50b2f3d1d.gif)

[Go to top](#top) 


## Post functionality
Any user can create posts. We can split a single post for two section. Main section with post image and icons - first icon is responsible for the thumbs up option, next one is a modal window with the list of users who gave thumb up, the next two icons appear only to the owner of the post and are responsible for the editing and deleting the post. Second section is the comments section. All users can leave a comment below the post and delete own comment.
<p  align="center">
  <img src="https://user-images.githubusercontent.com/90046128/217635247-751556d7-b472-445c-b944-7d8da2bb83fd.png"/>
</p>


[Go to top](#top) 
