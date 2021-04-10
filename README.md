"# fast-api" 
This will have a rest-API backend and the front end could be a js/mobile application.

For simplicity, let's consider only the scenario corresponding to a recruiter creating job listings in the system.

 

A Recruiter creates and maintains job listings. A candidate can view all the job listings and apply for a job that he is interested in. We will only build the rest-API backend for this minimal functionality.

 

Our rest-API  should have the following endpoints

/jobs/ (post, get, delete methods) - create, delete and get jobs

/job/{id} - get details of a specific job listing - get details of a job by id

/job/{id}/apply -

 

We will use FastAPI for building the backend. You can read more about FastAPI here https://fastapi.tiangolo.com/.

 

Your Database have to follow conditions

Define the tables like shown here in this example: https://fastapi.tiangolo.com/tutorial/sql-databases/

Define three tables

            1. candidates

            2. jobs

            3. Job applications (with foreign key to candidate and jobs table) with the proper relationship defined in sqlalchemy

 
