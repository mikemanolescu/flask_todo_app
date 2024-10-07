A simple To-Do List web application built using Flask. 
This project helped me learn key aspects of web development, including handling routing, templates, forms, databases, and working with Git for version control. 
It also allowed me to gain hands-on experience with both frontend and backend technologies, and gave me insight into building and deploying a full-stack web application.

Features

	•	Task Creation: Users can add tasks with a description and priority level (low, medium, high).
	•	Task Editing: Allows users to update the description and priority of existing tasks.
	•	Task Deletion: Users can delete tasks they no longer need.
	•	Priority Display: Tasks are color-coded based on their priority for better visibility.
	•	Persistent Storage: Uses SQLite to persist tasks between server restarts.
	•	Responsive Layout: Styled with basic CSS to create a clean and responsive user interface.

Technologies Used

	•	Backend: Flask
	•	Frontend: HTML, CSS (with Flexbox for layout)
	•	Database: SQLite
	•	Version Control: Git & GitHub

 What I’ve Learned

1. Flask Routing & Views

	•	Gained an understanding of how to define routes using the @app.route decorator and how to map those routes to specific functions in Python.
	•	Handled HTTP methods like GET and POST for adding, editing, and deleting tasks.

2. Jinja2 Templating

	•	Used Jinja2 templates to dynamically generate HTML content. This included passing variables (like tasks) to the template and using logic in the templates for displaying content conditionally.

3. Handling Forms in Flask

	•	Learned how to build forms in HTML and process form submissions in Flask using request.form.get(). Implemented task addition, deletion, and updating functionality using forms.

4. Using SQLite for Data Persistence

	•	Created a simple SQLite database to store tasks, ensuring that data persists across server restarts.
	•	Wrote SQL queries to insert, update, and delete tasks from the database, as well as fetch them for display.

5. Frontend Styling with CSS and Flexbox

	•	Applied Flexbox to create a simple, responsive layout for the to-do list.
	•	Styled the priority levels (low, medium, high) with different background colors for a better user experience.

6. Version Control with Git and GitHub

	•	Learned to use Git for version control, tracking changes made to the project.
	•	Created a GitHub repository and learned how to push the project to GitHub for backup and collaboration.
