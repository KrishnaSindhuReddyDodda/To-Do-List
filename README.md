1) A task list also called a to-do list. It's a list of tasks to be completed, such as chores or steps toward completing a project. It is a tool that which serves as an alternative to memory. Task lists are used in self-management, business management, project management, and software development. This project is designed with HTML,CSS(front-end), python in the back-end and by using SQLite3 database. In this we can add, delete and view all added lists.
2) At last I deployed this application in Amazon EC2 through AWS S3 bucket. 
3) The following are the steps to deploy the application in Amazon EC2.
4)    I) Initially I created a zip file (to_do_list.zip), with all these application (html, css , python) files in it.
5)    II) Now in AWS management console, I created a bucket and uploaded this to_so_list.zip folder in it as an object.
      III) On the other hand, I created one EC2 instance and launched it. Once when our instance starts running, open AWS Command Line Interface.
      IV) Now copy the object url of that zip folder in the S3 bucket.
      V) Next I created the empty directory through AWS CLI and changed the current directory to that empty directory.
      VI) Now to download the zip folder from S3 bucket in this directory, type this command in CLI **wget object_url**.
      VII) Now I unzipped the folder using this command **unzip to_do_list.zip** to view all the files(html, css, python) in it.
      VIII) Finally I started the service with this command **service https start**
      IX) Now go to EC2 instance and copy the IPv4 public address and paste in browser to view our application. 
