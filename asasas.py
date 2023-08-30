import bardapi
import os

# set your __Secure-1PSID value to key
token = 'ZwgY43vCX67P2Qi2dLTpDUpD0Yo_5wvcpvlrPh4EoYgjHdPho0bp-MAjgAg3Nn7IIrLOBw'

# set your input text
input_text = "What is the weather today in jakarta"

# Send an API request and get a response.
response = bardapi.core.Bard(token).get_answer(input_text)