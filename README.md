# buyonicPyRender
Webserver for payment using pix.

### This is an integration between EFÍ bank webhook API payment via brazilian PIX platform. The project consists in using a FastAPI webserver running on Render Platform. The payment can be retrieved by an edge hardware, such as an ESP32 IoT micro controller in order to automate old vending machines which works only by cash (coins and/or notes).

<div style="display: inline_block">
<img align="center" src="/demo.gif" alt="Demonstração"  width="40%">
</div>

## Requirements

- FastAPI
- uvicorn
- python-dotenv

## Deploying the project

1. Fork this repository
2. Generate a secret key:
Run the following in a python terminal or jupyter notebook
```
import secrets
print(secrets.token_hex(32))
```
3. Copy the code and save into a `.env` file asthe following:
`WEBHOOK_SECRET=<PASTE THE CODE HERE>`
4. Include the `.env` into your `.gitignore` file
5. Go to `https://dashboard.render.com/` and click on "Add new" > "Web Service" > "Public Git Repository" and paste the link to your forked github repository

- Environment: Python 3

- Build Command: `pip install -r requirements.txt`

- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

- Choose Free plan and click on "Create Web Service"