# Django REST Main Project

This is a Django-based REST API project with multiple apps for managing blogs, employees, and students.

## Project Structure

```
django_rest_main/
├── api/
├── blogs/
├── employees/
├── students/
├── manage.py
├── db.sqlite3
```

- **api/**: Core API logic, filters, pagination, serializers, and views.
- **blogs/**: Blog models, views, and serializers.
- **employees/**: Employee management.
- **students/**: Student management.
- **django_rest_main/**: Project settings and configuration.

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/nahidn4p/Django-rest-framework.git
   cd Django-rest-framework
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

4. **Run the development server**

   ```sh
   python manage.py runserver
   ```

## API Endpoints

- Blog, Employee, and Student endpoints are available under their respective apps.
- See [api/urls.py](api/urls.py), [blogs/views.py](blogs/views.py), [employees/views.py](employees/views.py) for details.

