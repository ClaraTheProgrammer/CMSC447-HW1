# CMSC447-HW1
CSMC447 Homework1

notes on how to set up website...

To run the website:
When in parent folder holding CMSC447-HW1 folder:
in Window's command prompt write: 
    CMSC447_HW1\env\Scripts\activate
    set FLASK_APP=CMSC447_HW1
    python -m flask run

How to create the Database db:
When in parent folder holding CMSC447-HW1 folder:
in Window's command prompt write: 
    python3
    from CSMC447_HW1 import db, create_app
    db.create_all(app=create_app())