from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
        user_email = request.args.get('user_email')
        print('USER_EMAIL==', user_email)
        s =  """<!DOCTYPE html>
            <html>
            <head>
                <title>MoonPay SDK</title>
                <!--Adds the MoonPay SDK as a script to your HTML file-->
                <script defer src="https://static.moonpay.com/web-sdk/v1/moonpay-web-sdk.min.js"></script> 
            </head>
            <body>
                <!--Initialize the SDK in your application with the flow, environment, variant, and any parameters related to Buy, Sell or Swap.-->
                <script>
                    window.onload = function() {
                        const moonpaySdk = window.MoonPayWebSdk.init({  
                            flow: 'buy',
                            environment: 'sandbox',
                            variant: 'overlay',  
                            params: {  
                                apiKey: 'pk_test_VfrqdFXjXekCEtIc8zijIf50oVJrCaC',
                                theme: 'dark',
                                // baseCurrencyCode: 'eur',
                                // baseCurrencyAmount: '100',
                                // defaultCurrencyCode: 'eth',
                                walletAddress: '0x5AdF7A7A70f7CdD86A9e133925A0b323840EE0B4',
                                externalCustomerId: 'arun'
                            },
                            debug: true
                        });

                        // Show the MoonPay SDK as soon as the page loads
                        moonpaySdk.show();
                    }
                </script>
            </body>
            </html>
        """

        return s