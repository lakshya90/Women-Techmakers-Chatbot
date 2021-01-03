def make_simple_response_message(text_to_speech):
    """ This is a valid rich message"""
    return {
        "type": "simple_response",
        "platform": "google",
        "textToSpeech": text_to_speech
    }


def make_basic_card_message(title, subtitle, formatted_text, image_url, buttons):
    return {
        "type": "basic_card",
        "platform": "google",
        "title": title,
        "subtitle": subtitle,
        "formattedText": formatted_text,
        "image": {
            "url": image_url
        },
        "buttons": [
            buttons
        ]
    }


def make_carousel_card_message(items):
    return {
        "type": "carousel_card",
        "platform": "google",
        "items": items
    }


def make_link_card_message(title, open_url_action):
    return {
        "type": "link_out_chip",
        "platform": "google",
        "destinationName": title,
        "url": open_url_action
    }


def make_list_card_response_message(title, items):
    return {
        "type": "list_card",
        "platform": "google",
        "title": title,
        "items": items
    }


def make_suggestion_chips_message(suggestions):
    return {
        "type": "suggestion_chips",
        "platform": "google",
        "suggestions": suggestions
    }


def make_buttons(title, open_url_action):
    return {
        "title": title,
        "openUrlAction": {
            "url": open_url_action
        }
    }


def make_item(option_info, title, description, image_url):
    return {
        "optionInfo": option_info,
        "title": title,
        "description": description,
        "image": {
            "url": image_url
        }
    }


def make_option_info(key, synonyms):
    return {
        "key": key,
        "synonyms": [
            synonyms
        ]
    }


def make_suggestion(title):
    return {
        "title": title
    }
