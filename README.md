# Entry-Management-Software
This project is an `Entry Management Software`. With its help we will be able to track all the visitors (Name, Email Id, Phone Number, Checkin Time, Checkout Time).Now let us try to understand the basic work flow of this project.</br>
</br>![flow-chart](https://user-images.githubusercontent.com/25201552/69768674-777b4780-11a7-11ea-9a23-5749e82a57dd.png)
### How to run -
All the scripts are written in python3. So in order to execute , just run `python3 main.py`.
### Input -
Details of Host - Name, Email Id, Phone Number , Address. </br>
</br>![entry-of-host](https://user-images.githubusercontent.com/25201552/69768771-f1133580-11a7-11ea-899b-27b85c14e814.png)

### Options -
There are four options available.</br>
(1) To Check-in </br> 
(2) To Check-out </br>
(3) To export database into an ` Excel Sheet `</br>
(4) To exit </br>

But before running the `main.py` script, we need to create database to store all the visitors's record. Run `db_setup.py` file to create database named `db1` and a table named `visitor`. To login into mysql run `mysql -u user -p` and then give the password.
### Check-in
 If a visitor wants to check in , he/she needs to press 1. Then fill their details. A mail as well as a sms will be delivered to the host containing the information of visitor along with the check in time.
 </br> ![checkin-visitor-1](https://user-images.githubusercontent.com/25201552/69769139-967ad900-11a9-11ea-9343-c4a04a3998ef.png)
 </br>
 #### Mail to the host about details of the visitor</br>
 </br>![checkin-111](https://user-images.githubusercontent.com/25201552/69769279-24ef5a80-11aa-11ea-8ade-8d0520dd8280.png)
</br>
#### SMS to the host about the details of the visitor</br>
</br>![sms-jags](https://user-images.githubusercontent.com/25201552/69769333-6f70d700-11aa-11ea-8f01-3a4926b02930.png)

#### SMS
For SMS, SNS is being used (an AWS service).Function ` sms` in `sns.py` is responsible for sending SMS to the host. Actually to login AWS from console we need access key id and secret access key which are provided by `cred.json` file. Actually these credentials should be encrypted.
#### Mail
For mailing purpose, SMTP library is being used. Function `mail` in `mail.py` is the one for mailing details to host along with the time stamp. For adding time stamp, function `timeStamp` in `entry.py` is being used.
To further add visitors, again press `1`.</br>


### Check-out
On pressing 2, a visitor can simply checkout. But in order to find out which visitor wants to checkout , it will first ask the `email address of the visitor`. The visitor with that specific email will be able to checkout. A mail is delivered with details of visitor, check-in time, check-out time, host name and address visited. </br>
</br>
#### Mail to the visitor at the time of check-out
![checkout-visitor-2 2](https://user-images.githubusercontent.com/25201552/69769867-b8c22600-11ac-11ea-90dd-7b48512e1f85.png)
Along with this , there are two more tasks which take place. </br>
#### Database
Now its time to insert details related to the visitors in our database. As soon as a visitor leave we will insert its entry in database `db1` Function `create_database` in `create_visitor_database.py` is responsible for the same.</br>
</br>
![database-at-the-end-of-day](https://user-images.githubusercontent.com/25201552/69770055-82d17180-11ad-11ea-8e25-3ef477a5effe.png)
</br>
#### Google Spreadsheet
This is an additional feature included with our software. Actually the most commonly used tool these days is google spreadsheets. Accessible from any internet-connected computer or mobile device, allowing others to view online files, shared access and editing in real time of online files and so on. Because of so many used cases, we added this as a feature in our software.
So, as a visitor checkout , his/her entry will be added in google spreadsheet.</br>
</br>
![entry-in-spreadsheet-after-checkout](https://user-images.githubusercontent.com/25201552/69770226-4e11ea00-11ae-11ea-86e1-b1b95c4353b6.png)
</br>
Function `visitor_db` from `visitor_db.py` will perform this task. </br>
 For more details , check out this [repository](https://github.com/amanpreet9391/Python-Google-Spreadsheets). </br>
 </br>
 ### Export
 Excel sheets or Google spreadsheets are used a lot more often these days. In the last section, google spreadsheet was discussed. Now its time for Excel sheet. With this functionality , one can export the whole visitor database into an excel sheet. This export operation is generally used for taking database backup. We can use this backup later for various purposes. For example, this will help to reuse backup for restoring the database in the future.
</br>
![option-for-export](https://user-images.githubusercontent.com/25201552/69770614-b44b3c80-11af-11ea-9c8e-2412a3e3883b.png)
</br>
![xcel-sheet-created](https://user-images.githubusercontent.com/25201552/69770439-1d7e8000-11af-11ea-9f44-71bca3f465b9.png)
</br>
On pressing key `3` , it will automatically create a `test_workbook.xsls` sheet containing the whole database.</br>
#### Note -
 There is a `function.txt` file , which list down all the functions used in our project along with there description. For setup there is `requirement.txt` file.</br>


















