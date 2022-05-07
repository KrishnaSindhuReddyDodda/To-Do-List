1) A task list also called a to-do list. Tha main goal of this project is to list a tasks to be completed, such as chores or steps toward completing a project. It is a tool that which serves as an alternative to memory. Task lists are used in self-management, business management, project management, and software development. This project is designed with HTML,CSS(front-end), python in the back-end and by using SQLite3 database. In this we can add, delete and view all added lists.
2) The UI is like there are three buttons (add, delete, view)
3) Add button helps to add task_id, task description; Delete button helps to remove the particular task with it's task_id; View button will list all the tasks available or need to do.
4) At last I deployed this application in Amazon EC2 through AWS S3 bucket. 
5) The following are the steps to deploy the application in Amazon EC2.
6)   a) Initially I created a zip file (to_do_list.zip), with all(html, css , python) files in this application.
7)   b) Now in AWS management console, I created a bucket and uploaded this to_so_list.zip folder in it as an object.
8)   c) On the other hand, I created one EC2 instance and launched it. Once when our instance starts running, open AWS Command Line Interface.
9)   d) Now copy the object url of that zip folder in the S3 bucket.
10)   e) Next I created the empty directory through AWS CLI and changed the current directory to that empty directory.
11)   f) Now to download the zip folder from S3 bucket in this directory, type this command in CLI **wget object_url**.
12)  g) Now I unzipped the folder using this command **unzip to_do_list.zip** to view all the files(html, css, python) in it.
13)  h) Finally I started the service with this command **service https start**
14)  i) Now go to EC2 instance and copy the IPv4 public address and paste in browser to view our application. 
