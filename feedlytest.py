import json
import requests

# Feedly

feedaccess = "A0IgCr9FnuSlREUdYwmXxHLvzi0HBHB_yqRJeibJ1qnap1HJ3jNpyAkDO-gaMtt7_c2c8Dag73Bbna_46rAF_mcVjb9ncSsU9NUipU_bXQbYkwPDJJT6kGo09QlJ5ZkVUBSn7ne8ED9COludkx6E3nnFv8YhoQrm-Bnl2k0PAkhLJ1PP-OgA43j571io9N0WQaG7S0F5PLeHDXWZP86Zcjz4R5ddog:feedlydev"
myfeedid = "user/966c7b97-9708-4cb4-8e3e-19d0b7b1f9c9/category/Tutorial"
feedcount = "20"
myurl = "http://cloud.feedly.com/v3/streams/contents?streamId=" + myfeedid + "&count=" + feedcount


headers = {'Authorization': 'OAuth ' + feedaccess}
res = requests.get(url=myurl, headers=headers)
con = res.json()
print json.dumps(con , indent=4)