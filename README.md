# Django-Blog
This projected started as a django blog application in order for me to learn django. After showing my manager at work he asked if I could make something similar for our workplace, so I decided to use this project for that. Our workplace is at a homeless shelter and this application will be used as a platform for the team to provide quick, real time updates and shift reports to help improve communication between the different shifts. 

Features:
  -User Authentification System
  -Password Reset
  -Blog Posts
  -Updating and Deleting Posts
  -Comment System for Posts 
  -Update and Delete comments 

Goals:
The goal of this project was to learn django and get some backend development experience. The new goal is to make a seameless blog platform for the team at the shelter. I want this application to improve communication between the team by giving everyone a chance to provide real time updates in an easy manner. There is a severe lack of communication between the different shifts and creating a place dedicated to the shelter should help improve on this. Currently, we use emails to send out shift reports but it becomes convoluted due to the high amount of emails from the team at the shelter and the rest of company constantly sending out emails that have nothing to do with the shelter. This application gives us our own private place to communicate.

Challenges:
As of now the hardest challenge was implementing the comment system. Originally, I tired implementing it through the post detail view and it became a mess that would not work. However, I decided to implement it using its own class based view and had better luck. I had issues involving passing in the right pk value (I kept passing the post value instead of the comment value) and having it return to the post detail view after the comment was deleted. These were small issues but as a beginner it took some trial and error to figure it out. In the end, it helped me understand class based views better and I look foward to the challenges the upcoming features will present. 

Upcoming Features:
  -Pinned-Posts System
  -Notification System
  -Different type of users based on position (i.e. supervisors, case managers, support staff)


