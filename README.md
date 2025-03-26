# LabelBoxMini

LabelBoxMini is a web application designed to help users build and deploy computer vision applications. It provides functionalities for creating projects, uploading images, annotating images, and managing projects.

## Project Structure

```
LabelBoxWebsite/
│
├── LabelBoxMini/
│   ├── __init__.py
│   ├── annotate.py
│   ├── auth.py
│   ├── dashboard.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── Login.html
│   │   ├── Dashboard.html
│   │   ├── Annotator.html
│   ├── static/
│   │   ├── Login.css
│   │   ├── index.css
│   │   ├── Dashboard.css
│   │   ├── Annotator.css
│   ├── other files/
│   │   ├── Home.py
│   │   ├── Dashboard.py
│   │   ├── Annotator.py
│
├── main.py
├── README.md
```

## Functionalities

### Home Page
- **File:** `Home.py`
- **Description:** Displays the main landing page with information about the application and navigation links.

### Dashboard
- **File:** `Dashboard.py`
- **Description:** Provides functionalities for creating, editing, and deleting projects. Users can upload images and view their projects.

### Annotator
- **File:** `Annotator.py`
- **Description:** Allows users to annotate images within their projects. Users can draw bounding boxes and label them.

### Authentication
- **File:** `auth.py`
- **Description:** Handles user authentication, including login and registration.

### Models
- **File:** `models.py`
- **Description:** Defines the database models for users, projects, images, and annotations.

### Views
- **File:** `views.py`
- **Description:** Contains the main routes for rendering templates and handling basic navigation.

### Static Files
- **Directory:** `static/`
- **Description:** Contains CSS files for styling the application.

### Templates
- **Directory:** `templates/`
- **Description:** Contains HTML templates for rendering the web pages.

## How to Run

1. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```
   python main.py
   ```

3. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## **Project Demo**
![Screenshot (3)](https://github.com/user-attachments/assets/1cc3184f-cf53-4f90-a837-42e00efd1bcc)

Link : https://www.canva.com/design/DAGi1LjMz7s/pZSjP3n6V9MnvavGcIBp5A/watch?utm_content=DAGi1LjMz7s&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h2b5e81956f







## License

This project is licensed under the MIT License.
