--------------------------http://127.0.0.1:8000/auth/register/  -post-------------------------------------


{
	"username":"shyam",
	"password":"sagar",
	"email":"shyam@gmail.com",
	"mobile":"556655",

}

===============================================================================================
-------------------------------------http://127.0.0.1:8000/auth/login/-------post----------------------
{
	"email":"shyam@gmail.com",
	"password":"sagar"
}
------------output---------
{
    "response": {
        "name": "shyam",
        "access_token": "0T3om9cmaH132vJuptEctBxBrAxuma",
        "expires_in": 36000,
        "token_type": "Bearer",
        "refresh_token": "uysKS0NgzQkPeoG7DU4Y4GM38ApHZ9",
        "client_id": "vCCDLXKIj27QvWcCCF6jC4tIOvImRD0XfTwLbUzm",
        "client_secret": "NCTSLqaOAVQOWKkh0K5iJXbx46AccvcIYL0Dij2tJ9hMwn91fHL35M5Yk4SLi1CNPokri6ld9Z9dL7f80LyQjjhffXicdovxPdZV1gRQdrmrcrdBywr7sjq3E1M3EwDK"
    }
}
============================================================================================================
------------------------------http://127.0.0.1:8000/auth/change_password/6/-----put-------------------------------------

{
	"old_password":"sagar",
	"new_password":"radhe"
}
-------------------------output---------
{
    "RESPONSE": " Password Change Successfully"
}
---------------------------------

---------------------------------------------------------------reset password-----post--
http://127.0.0.1:8000/reset_password/--


{
	"email":"sagar1@gmail.com"
}
======================================================================================================================
--------------------http://127.0.0.1:8000/reset_password/confirm/-------post--

{
	"token":"e69bd1349feb3731f6e7cc5162680c36f68eb6fa472e0301",
	"password":"noida@123"
}
=================================================================================================================
------------------------------------update profile--------------
   http://127.0.0.1:8000/auth/updateuserprofile/5/----put
{
	"email":"sapna@gmail.com",
	"password":"sapna",
	"mobile":"556565656",
	"username":"sapna"
	
}
---------------------------------------------------------------

