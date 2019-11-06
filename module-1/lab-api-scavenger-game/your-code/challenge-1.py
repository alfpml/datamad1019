import os
import requests
from dotenv import load_dotenv
load_dotenv()

# https://developer.github.com/v3/
def githubRequestAuthorized(resource):
    authToken = os.getenv("GITHUB_API_TOKEN")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        print("We have a github token: ", authToken[0:4])
    headers = {
        "Authorization": "token {}".format(authToken)
    }
    url = "https://api.github.com{}".format(resource)
    print("Requesting authorized {}".format(url))
    res = requests.get(url, headers=headers)
    return res

data = githubRequestAuthorized("/repos/ironhack-datalabs/datamad1019/forks").json()

languages=list(map(lambda forks: forks["language"], data))
print(list(set(languages)))
## ANswer I get is: [None, 'Jupyter NOtebook']