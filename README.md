# Summary

Computer networks lesson project
Simple blog design using Flask, JavaScript, CSS, HTML
This blog has the following features:
*   1. Registration
*   2. Entry and exit
*   3. Displaying posts registered by users
*   4. Adding a new post
*   5. Editing and deleting posts
*   6. Display the number of registered users

## Project structure

```shell
	blog/
	├── run.py               
	├── blog.db                   
	├── README.md
	├── blog                       
	│   ├── __init__.py	                
	│   ├── form.py                  
	│   ├── models.py 
	│   ├── templates
	│   │	 ├── 403.html
	│   │	 ├── 404.html
	│   │	 ├── about.html
	│   │	 ├── base.html
	│   │	 ├── contact.html
	│   │	 ├── detail.html       
	│   │	 ├── edit_profile.html 
	│   │	 ├── home.html 
	│   │	 ├── login.html
	│   │	 ├── new_post.html 
	│   │	 ├── profile.html
	│   │	 ├── register.html 
	│   │	 ├── update.html
	│   │	 └── inc
	│   │	 │   ├── form_errors.html
	│   │	 │   ├── messages.html
	│   │	 │   └── nav.html                                                  
	│   └── static
	│   │	 ├── fechapi.js.html
	│   │	 ├── css
	│   │	 │   ├── style.css
	│   │	 └── img
	
```

## Run

```
	$ cd ~

	$ git clone https://github.com/dylanninin/blog.git
```
Change the route
```
	$ cd blog
```
start a blog
```
	$ python run.py
```
![2](https://github.com/falakian/Simple-blog/assets/107622368/272e040d-4a9f-4661-aa7f-d751125dff2e)

![3](https://github.com/falakian/Simple-blog/assets/107622368/9959b6b9-8312-42fa-9177-da4c6a1f403e)
