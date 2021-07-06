import json

json_text1='{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
          '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj=json.loads(json_text1)

key="messages"
json_text2=obj[key][1]

key1="message"
print(json_text2[key1])

