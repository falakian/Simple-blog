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
![2](https://github.com/falakian/Simple-blog/assets/107622368/dcaf7bf3-14f4-4a67-92fa-1b403e62b28d)

![3](https://github.com/falakian/Simple-blog/assets/107622368/8024c5aa-27c5-4f58-b0e3-5f12ac2a56c1)
