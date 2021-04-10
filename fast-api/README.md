"# fast-api" 
This will have a rest-API backend and the front end could be a js/mobile application.

/jobs/ (post, get, delete methods) - create, delete and get jobs

/job/{id} - get details of a specific job listing - get details of a job by id

/job/{id}/apply -


Define three tables

            1. candidates

            2. jobs

            3. Job applications (with foreign key to candidate and jobs table) with the proper relationship defined in sqlalchemy

 candidates -names
 jobs -  developer,tester,manager
         desc       desc   desc
 job_applications - [status] -> [applied] [processing] [review]
 
