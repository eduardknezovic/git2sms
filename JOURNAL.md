
# git2sms

### Success criteria

Get the SMS notification when the git repository gets updated

### Technical Overview

#### Execution

- Get data from GitHub API  
- Compare the current state
- If data is not matching to the data from database:
    - Send an SMS (Currently from Twilio API)
    - Update the state 
    
### Possible expansions

- Monitored repository doesn't have to be git. Be open to add additional types

### Marketing

We can spam random job-posters on Upwork.   
They may be willing to throw a buck so they can monitor  
programmers on the go.   
(The old gits are probably so paranoid about having their code published online  
that they wouldn't even consider having the code in such popular repository!)

They don't have to use github, we can monitor git repositories, wherever they may be!
How do we achieve the connection? This is the trick. But first, github will suffice.

How would we onboard random users? Can we integrate some payment service?  
