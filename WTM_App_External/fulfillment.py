import json
import os
import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask import request, jsonify
from flask import make_response, Response
import program_offerings as po
import json
import logging

app = Flask( __name__ )


@app.route( '/fulfillment', methods=['GET', 'POST'] )
def index():
    request_payload = request.get_json()
    app.logger.info( 'Request: %s', request_payload )
    print json.dumps( request_payload, indent=4 )

    action = request_payload.get( 'result' ).get( 'action' )

    print action
    msgs = option[action]( request_payload )
    response_payload = make_response( msgs )

    app.logger.info( 'Response: %s', response_payload )
    print response_payload

    return jsonify( response_payload )


def make_response(messages):
    return {
        "speech": "",
        "messages": messages
    }


option = {
    'input.welcome': po.get_welcome_message,
    'input.user.choice': po.ask_based_on_user_choice,
    'input.unknown': po.get_unknown_input_response,
    'quit.conversation': po.end_conversation,

}
if __name__ == '__main__':
    app.run()
