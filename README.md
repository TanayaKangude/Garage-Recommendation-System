# Garage Management System

---
## FUNCTIONS
## Customer
- customer will signup and login into system
- customer can make request for service of their vehicle by providing details (vehicle number, model, problem description etc.)
- customer can delete request (Enquiry) if customer change their mind or not approved by admin (ONLY PENDING REQUEST CAN BE DELETED )
- customer can check status of Request(Enquiry) that is Pending, Approved
- customer can send feedback to admin
- customer can see/edit their profile
---
## Garage Owner
- Garage owner will register their garage by providing details like ( address, mobile etc.)
- Admin will approve garage owner request
- After account approval, garage owner can login into system
- Garage owner can send feedback to admin
- Garage owner can see/edit their profile
---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login , admin can see how many customer, mechanic, recent service orders on dashboard
- Admin can see/add/update/delete customers
- Admin can see/add/update/delete garage owners
- Admin can approve garages (requested by garage owner) based on their details
- Admin can see/update garages
- Admin can see/update/delete request/enquiry for service sent by customer
- Admin can also make request for service (suppose customer directly reached to service center/office)
- Admin can see feedbacks sent by customer/garage owner
---
### Other Features
- we can change theme of website day(white) and night(black)
- if customer is deleted by admin then their request(Enquiry) will be deleted automatically

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks

```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
- Login to gmail through host email id in your browser and open following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```
## Drawbacks/LoopHoles
- When customer/mechanic edit their profile then he/she must login again because their username/password is updated in db.
## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.
