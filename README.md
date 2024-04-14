# Final Project - CS5060 #
## Prediction of the US Job Market and Insurance ##
### Authors ###
Ryan Christensen

Michael Westberg

Project Proposal

### Task Description ###
#### European Call Option and Optimal Stopping Algorithm ####

Predicting the economic strength of the United States of America in the next 10 years using a European Call Option. By using current and past data of the American unemployment rate, we will aim to predict the strength of the US economy in the next 10 years. Once the strength of the economy is assessed, the data will enable us to calculate a stopping algorithm for job searching. Based upon the following criteria:
-	The number of jobs can you feasibly search for in an arbitrary amount of time
-	The number of job offers do you receive in an arbitrary amount of time
-	This will be based on a 36% interview-to-hire ratio from [Recruiting Metrics and KPIs- Career Plug](https://www.careerplug.com/blog/recruiting-metrics-and-kpis/) metrics in the United States.
-	The current and past employment data for the [Data Processing, Hosting, and Related Services: NAICS 518](https://www.bls.gov/iag/tgs/iag518.htm#workplace_trends) which includes Software Developers in the United States.
-	Given a 6-month emergency funds for cost of living based on a Utah average monthly expense/cost of living report via [SOFIs Cost of Living in Utah](https://www.sofi.com/cost-living-utah/)


#### Insurance: ####
Developing a basic pricing model for travel insurance. Using a dataset of travel insurance we will build a simple predictive model based on multiple factors about travel insurance and the buyers of the insurance. We will explore different relationships between multiple variables and how those variables influence the insurance. 

One of the main things we will be looking for is relationships between claims filed and the other variables. This will allow us to know if there is an optimal time to opt into the travel insurance vs not opting in. Similar to the midterm we will explore from different angles.

The dataset we will pull from will be from [Travel Insurance](kaggle.com).

### Task Outputs ###

#### Subtask 1: European Call Option on the US Unemployment Rate ####

Using the European Call Option Algorithm, predict the US Unemployment rate over the course of the next 10 years. The data collected will ensure more accurate data in finding results to Subtask 2, and focus on current and future state of the United States’ Economy.

#### Subtask 2: Optimal Stopping Algorithm on the US Job Market ####

Given the result from Subtask 1, simulate a job searcher with the described requirements to find an optimal stopping point for when to accept a job offer from a potential employer. The specific criteria we will aim to adhere to is as follows:
-	The number of jobs can you feasibly search for in an arbitrary amount of time
-	The number of job offers do you receive in an arbitrary amount of time
-	This will be based on a 36% interview-to-hire ratio from [Recruiting Metrics and KPIs- Career Plug](https://www.careerplug.com/blog/recruiting-metrics-and-kpis/) metrics in the United States.
-	The current and past employment data for the [Data Processing, Hosting, and Related Services: NAICS 518](https://www.bls.gov/iag/tgs/iag518.htm#workplace_trends) which includes Software Developers in the United States.
-	Given a 6-month emergency funds for cost of living based on a Utah average monthly expense/cost of living report via [SOFIs Cost of Living in Utah](https://www.sofi.com/cost-living-utah/)

#### Subtask 3: Travel Insurance ####

Using the information learned in class and in the projects about insurance we will create multiple plots that show relationships between variables across the dataset. As in the midterm we will increment, for example we will differentiate between just focusing on age and then age and gender (if they end up having a correlation with claims filed).


### Task Outcomes ###
**ST1:** Predict the Unemployment Rate in the United States over the course of the next 10 years. This will also indicate the overall economic strength of the United States. The outcome allows us to better find ST2 results.

**ST2:** Calculate the Optimal Stopping Point in a given job market as to when and if a potential employee should reject a job offer in hopes of receiving a more lucrative job offer.

**ST3:** Calculate the optimal situation to opt into travel insurance. Essentially finding the risk of each situation and when is most likely that a claim would be filed in order to increase effective use of money.

### Task Impacts ###
This work will demonstrate the US Job market, and show if it is beneficial to a potential employee to reject a job offer, and wait for a better job offer.

Because of the unknown risk that is associated with travel, the work on insurance will give people a better idea of when they should buy offered insurance in order to save them money, both from not having to pay for insurance and from avoiding having to pay for an uninsured accident while traveling.

### Task Timeline ###

| Sub Task | Title                                        | Development and Research Days |        |        |        |        |        |        |        |        |        |
|----------|----------------------------------------------|-------------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|          |                                              | 10-Apr                        | 11-Apr | 12-Apr | 13-Apr | 15-Apr | 16-Apr | 17-Apr | 18-Apr | 19-Apr | 20-Apr |
| 1        | European Call Options - US Job Market        | X                             | X      | X      |        |        |        |        |        |        |        |
| 2        | Optimal Stopping Algorithm for Job Searching |                               |        |        | X      | X      | X      |        |        |        |        |
| 3        | Insurance                                    |                               |        |        |        |        |        | X      | X      | X      | X      |
|          | **Milestones**                                   |                               |        |        |        |        |        |        |        |        |        |
| 1        | Calculate Job Market                         |                               |        | X      |        |        |        |        |        |        |        |
| 2        | Calculate Optimal Stopping Point             |                               |        |        |        |        | X      |        |        |        |        |
| 3        | Insurance                                    |                               |        |        |        |        |        |        |        |        | X      |


