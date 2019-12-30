# What is DBPortal!
**DBPortal**  is a django-based database related project centred around data-entry, updation and searching. It also has pinging services.

# Can you be more specific ?!

It's very simple all DBPortal has two types of users-
 - *Staff*
 - *DBer*
 
 A *staff* has the ability to add/modify/delete multiple users by the use of `excel sheets`. Just make an excel sheet using some particular format upload it in your staff account along with some details and you are good to go.
 The *staff* also has the ability to send mass messages using SMTP  based mailing system integrated in the DBPortal to inform `DBer` in his circle regarding anything important like-
 - Filing taxes
 - Maybe they need to update there profiles
 - Maybe to inform about a census coming soon.

The *staff* has the job to micromanage their circle keeping there data updated and keeping them updated.

A *DBer* is the `most significant and smallest building block` of the DBPortal. Why so?! Sometimes the *Staff* couldn't keep a check on each *DBer* maybe their information is not updated or maybe they want to contact a particular *DBer* to reach out to them.  

# Steps to make your own DBPortal

Okay so the project might seem very intimidating but don't worry we will guide you. So what are you required to do ?!
### STEP 1
Make a data entry system which involves uploading/deleting via excel sheet or by manually entering the data. The data of a user requires following things-

 - Aadhar Card Number (12-Digit UID)
 - First/Last Name
 - DOB
 - Gender
 - City (Dependent-Dropdown)
 - State(Dependent-Dropdown)
The site should be able to process `excel sheets` and using unique URLs for each entry one could modify/delete data.
### STEP 2
Now that your backbone of the site is properly working you can now proceed to step 2 which is add `User Authentication and Privilages`.
A lot of data can't be kept public because the users don't want everyone to know their password or keep spamming on their mail-IDs. Each `DBer` upon registration has to link thei  account to existing record of their aadhar card in DBPortal. If the record doesn't exist contact the `Staff` in your city-circle because **existence of a record is a neccessity for creation of a DBer** . 
The `Staff` account is created by an Admin with his password username and city-circle he needs to resort to. The `Staff` can change his password later to prevent any intervention.
### STEP 3
Add a `SMTP based mailing system` which a `Staff` can use for mass-pinging and a `DBer` can use for pinging a particular `DBer` or `Staff`. Add profile searching feature to a `DBer` for pinging services.
After implenting this add different privilages to different Users of the DBPortal-
**Staff Privilages-**
 - Can add/modify/delete records using excel sheets.
 - Can ping updates and messages to `DBer`s of their circle.
 - Can change their own password.

**DBer Privilages-**
 - Can modify their own records.
 - Change the password and email of their records.
 - Search for a particular record and ping the concerned `DBer`.
### Further Improvements-
This project will be used as a sample or backbone project for your implenting your future concepts. The features to be implented are as follows-

 - [ ] Using `Django-Rest-Framework` to serialize the records or for implenting URL-based filtering.
 - [ ] Using Celery to make the excel-sheet processing a background task.
 - [ ] Deploying this project on Digital Ocean and Heroku. 
