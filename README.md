

### Implementation Tips
- Use Flask
- User Authentication: Use Flask-Login for handling user authentication and authorization.
  - Consider using Flask-Security or Flask-Social for more advanced authentication features, such as social logins.
- Database Integration: Use Flask-SQLAlchemy for database interactions.
- Templates: Use Jinja2 for rendering dynamic HTML templates.
- APIs: Integrate external APIs to add more functionality (e.g., Google Maps, payment gateways, etc.).
- Asynchronous Tasks: Use Celery for background tasks (e.g., sending emails, processing data).
- Front-End: Use Flask-Restful for creating RESTful APIs if you plan to use a front-end framework like React or Vue.js.

### Ideas for the App 
- require phone number to sign up for event.
  - post-event send a short survey where they can reply from 1-10 how they would rate the event... or they can click a link to submit a more comprehensive review.
