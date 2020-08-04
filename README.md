# Camino Financial's Backend Take-home Challenge



## Your mission
Greetings. The Master Control Program has chosen you to serve your system on the Game Grid. You have 3 hours to simulate a business lending environment. Should you become successful, you will be invited to the next level in the Game Grid.

## Your task
1. Design a RESTful API that will take an online application for a business that wants a loan.
2. Implement the API using Django Rest Framework. Use Docker for extra credit.
3. Write unit test suites for all your functions.
4. (Extra Credit) Set up your code on heroku, linode or a server of your choice for a live demostration.
5. When you are done, notify your us through Indeed (or other hiring platform) and provide links to source code and your live server.

### Detail requirements on the API EndPoints to implement
1. Need one endpoint called loanapp/ to take application. Should be able to consume this [json](https://github.com/caminofinancial/BackendTakehomeChallenge/blob/master/sample.json).
2. Need one endpoint called status/ to provide a status on an application submitted given a loanapp id. Be creative about the status to return.
3. Develop some kind of algorithm to recognize duplicates in app submissions. A person could submit now on the phone and later on a desktop. A person could submit a new app 4 months down the road with almost the same information but a new mobile number. When a duplicate is found, the key thing to do is to update the original record and not to overwrite. And allow some ways to make note of this.
4. Be mindful that each business can have one or multiple business owners.
5. Save data in models.

## Tips
1. Use any libraries or tools as you see fit.
2. Be creative and deliver on-time.
3. A good template / tutorial to use https://testdriven.io/blog/deploying-django-to-heroku-with-docker/

## SRS

# DEPLOYMENT REQUIREMENT
1. Design a RESTful API using Django Rest Framework.
2. Use Docker for extra credit.
3. Write unit test suites for all your functions.
4. Set up your code for a live demostration.
5. Using cloud data store.

# MODEL REQUIREMENT
1. METHOD: POST loanapp/ to get the [json](https://github.com/caminofinancial/BackendTakehomeChallenge/blob/master/sample.json).

    function UPDATE(json):
        for key in json:
            if(key contains in json):
                UPDATE THAT KEY
            else:
                Add that key


    if(data found in db by CFRequestId):
        Save to logs
        if(date_diff<4 month):
            NOT ALLOWED
        else:
            if(phone number is same):
                NOT ALLOWED
            else:
                UPDATE
    else:
        UPDATE

2. METHOD: GET status/ OUTPUT:status INPUT:CFRequestId,scope TYPE:JSON

    if(CFRequestId found in db with the input):
        return status (CFApplicationData)
    else:
        application not found


3. Saving the data in the model in Firebase cloud data store as model


#Not added

1. 2FA Auth and SSL security so it becomes an open API 
2. Model resistance to advanced form of malformed JSON
