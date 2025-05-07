Django Recipe App
Welcome to the Django Recipe App! This application allows users to explore various recipes, including detailed instructions and ingredients. Users can also register, log in, and manage their favorite recipes.

Features
User Authentication: Users can register, log in, and log out.
Recipe Listings: Browse a variety of recipes categorized by type (e.g., desserts, vegetarian).
Recipe Details: View detailed information about each recipe, including ingredients and cooking instructions.
Favorites: Users can bookmark their favorite recipes for easy access.
Responsive Design: The application is designed to be mobile-friendly.
Technologies Used
Django: The web framework used to build the application.
HTML/CSS: For structuring and styling the web pages.
JavaScript: For interactive elements, such as dropdown menus.
Bootstrap: (Optional) For responsive design (if included in your project).
Installation
To set up the Django Recipe App locally, follow these steps:

Clone the repository:
https://github.com/PalmThanakorn/L6SDv2-24T1-A2-Assessment-v1.2-Thanakron-Chareonkunmongkon.git

Create a virtual environment:
python -m venv .venv

.venv\Scripts\activate

Install dependencies:
pip install Django

python -m django --version

python -m pip install -U Django

Run migrations:
$ python manage.py makemigrations --name changed_my_model your_app_label

Create a superuser: (optional, for accessing the admin panel):
python manage.py createsuperuser

Username:

Email address:

Password: >

Password (again): >

This password is too short. It must contain at least 8 characters.

This password is too common.

This password is entirely numeric.

Bypass password validation and create user anyway? [y/N]:

Run the development server:

python manage.py runserver

Access the application: Open your web browser and go to http://127.0.0.1:8000/.

Usage
Home: Navigate to the home page to see the list of recipes.
About: Learn more about the application and its creators.
Recipe Categories: Use the dropdown menus to filter recipes by category.
User Profile: Users can manage their profiles and favorite recipes after logging in.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries, please contact us at:

Email: @***.gmail.com
Phone: +1 (234) 567-8901
Thank you for using the Django Recipe App! We hope you enjoy exploring and cooking delicious recipes.
