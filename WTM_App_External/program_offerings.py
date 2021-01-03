import google_assistant as ga
from flask import Flask, render_template
from config import (_WTM, _STORY)
import logging

app = Flask( __name__ )


def get_welcome_message(request_payload):
    simple_response = ga.make_simple_response_message(
        _WTM )
    title = "What do you want to know on the Women Techmakers program?"
    items = []

    option_info = ga.make_option_info( "Our Story", "Our Story" )
    item = ga.make_item( option_info, "Our Story ", _STORY,
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "Membership", "Membership" )
    item = ga.make_item( option_info, "Membership ", "Here are more details on the Women Techmakers Membership Program",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "Scholarships", "Scholarships" )
    item = ga.make_item( option_info, "Scholarships",
                         "Here are the various scholarships that you can avail as a part of the Women Techmakers program",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "Meetups", "Meetups" )
    item = ga.make_item( option_info, "Meetups",
                         "Here are the details about Meetups that happen under Women Techmakers program",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "IWD Summit", "IWD Summit" )
    item = ga.make_item( option_info, "IWD Summit", "International Women's Day Global Event Series",
                         "" )
    items.append( item )

    list_card_msg = ga.make_list_card_response_message( title, items )

    msgs = [simple_response, list_card_msg]

    return msgs


def get_unknown_input_response(request_payload):
    simple_response = ga.make_simple_response_message( "Sorry, I missed what you said. Can you say it again?" )
    msgs = [simple_response]

    return msgs


def end_conversation(request_payload):
    simple_response = ga.make_simple_response_message( 'Thank you for talking to me. Have a wonderful day!' )

    msgs = [simple_response]

    return msgs


def get_story(request_payload):
    simple_response = ga.make_simple_response_message( "Kicked off in 2012 as a once-per-year event at I/O by then VP "
                                                       "of Google[x] Megan Smith, Women Techmakers is now led by Head "
                                                       "of Global Programs Natalie Villalobos and a global team of "
                                                       "Googlers who are passionate about empowering women in "
                                                       "technology." )

    title = "Want to know more about the pillars of the program?"
    items = []
    option_info = ga.make_option_info( "visibility", "visibility" )
    item = ga.make_item( option_info, "Visibility ", "What does visibility mean here?", "" )
    items.append( item )

    option_info = ga.make_option_info( "community", "community" )
    item = ga.make_item( option_info, "Community", "What does community mean here?",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "resources", "resources" )
    item = ga.make_item( option_info, "Resources",
                         "What does resources mean here?",
                         "" )
    items.append( item )

    carousel_card_msg = ga.make_list_card_response_message( title, items )
    msgs = [simple_response, carousel_card_msg]
    return msgs


def get_visibility_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Visibility is to showcase the work and passions of women in the technology "
        "industry by providing a platform to celebrate their talents "
        "and spotlight role models. Do you want to know anything else?" )

    msgs = [simple_response]
    return msgs


def get_community_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Community is to create a supportive global group in which women can "
        "connect, be inspired, and encourage each other to realize "
        "their passions.Do you want to know anything else?" )
    msgs = [simple_response]
    return msgs


def get_resources_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Resources is to provide opportunities to develop industry needed skillsets, "
        "aid career development, and support women to become industry "
        "leaders in all phases of their careers. Do you want to know anything else?" )

    msgs = [simple_response]
    return msgs


def get_membership_details(request_payload):
    simple_response = ga.make_simple_response_message( "I can assist you with the membership program." )
    title = "What do you want to know on the membership program?"
    items = []
    option_info = ga.make_option_info( "become_a_member", "become_a_member" )
    item = ga.make_item( option_info, "Become a member ", "How to become a member?", "" )
    items.append( item )

    option_info = ga.make_option_info( "member_benefits", "member_benefits" )
    item = ga.make_item( option_info, "Membership Benefits", "What are the benefits of being a member?",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "career_levels", "career_levels" )
    item = ga.make_item( option_info, "Career Levels",
                         "What are the career levels associated with membership program?",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "skillsets", "skillsets" )
    item = ga.make_item( option_info, "Skillsets", "What are the skillsets that you can acquire by being a member?",
                         "" )
    items.append( item )

    carousel_card_msg = ga.make_list_card_response_message( title, items )

    msgs = [simple_response, carousel_card_msg]

    return msgs


def get_become_member_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Here's how you become a member at Women Techmakers. Do you want to know anything else?" )
    link = ga.make_link_card_message( "this link to become a member",
                                      "https://services.google.com/fb/forms/joinwomentechmakers/" )

    msgs = [simple_response, link]

    return msgs


def get_member_benefits_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Here are the Women Techmakers membership benefits." )

    items = []
    option_info = ga.make_option_info( "benefit_1", "benefit_1" )
    item = ga.make_item( option_info, "Work how you work ",
                         "Begin unbiasing + increase impact",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "benefit_2", "benefit_2" )
    item = ga.make_item( option_info, "Find a local tech entrepreneurship hub",
                         "Join the Campus community",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "benefit_3", "benefit_3" )
    item = ga.make_item( option_info, "Empower your organization to support women",
                         "Access tools and research to support women in tech",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "benefit_4", "benefit_4" )
    item = ga.make_item( option_info, "Lead, learn and connect locally",
                         "Meet women in tech near you",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "benefit_5", "benefit_5" )
    item = ga.make_item( option_info, "Stay informed",
                         "Updates on women in tech",
                         "" )
    items.append( item )

    list_card_msg = ga.make_carousel_card_message( items )

    msgs = [simple_response, list_card_msg]

    return msgs


def get_benefit_1(request_payload):
    simple_response = ga.make_simple_response_message( 'Help your team identify, quantify, and reduce unconscious '
                                                       'bias and inefficiencies that may exist within your '
                                                       'organization. Do you want to know anything else?' )

    msgs = [simple_response]

    return msgs


def get_benefit_2(request_payload):
    simple_response = ga.make_simple_response_message( 'Find mentorship, connect with peers, and attend events to '
                                                       'power your entrepreneurial ideas in a supportive, '
                                                       'inspiring community. Do you want to know anything else?' )

    msgs = [simple_response]

    return msgs


def get_benefit_3(request_payload):
    simple_response = ga.make_simple_response_message( 'The National Center for Women and Information Technology ('
                                                       'NCWIT) has developed new research-based methods to help women '
                                                       'and allies increase support for women working in the tech '
                                                       'industry. Do you want to know anything else?' )

    msgs = [simple_response]

    return msgs


def get_benefit_4(request_payload):
    simple_response = ga.make_simple_response_message( "Engage with women in tech, raise your personal brand, launch "
                                                       "an app, or change careers through connecting to Women Who "
                                                       "Code global network. Do you want to know anything else?" )

    msgs = [simple_response]

    return msgs

def get_benefit_5(request_payload):
    simple_response = ga.make_simple_response_message( 'Find content, community, and events for aspiring and current '
                                                       'innovators in technology through Women 2.0. Do you want to '
                                                       'know anything else?' )

    msgs = [simple_response]

    return msgs


def get_membership_careerlevel_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Here are the various career levels at Women Techmakers." )

    items = []
    option_info = ga.make_option_info( "early_career", "early_career" )
    item = ga.make_item( option_info, "Early Career ",
                         "0-5 years of industry experience",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "mid_career", "mid_career" )
    item = ga.make_item( option_info, "Mid career",
                         "6-10 years of industry experience",
                         "" )
    items.append( item )

    option_info = ga.make_option_info( "established_career", "established_career" )
    item = ga.make_item( option_info, "Established career",
                         "11+ years of industry experience",
                         "" )
    items.append( item )

    carousel_card_msg = ga.make_carousel_card_message( items )

    msgs = [simple_response, carousel_card_msg]
    return msgs


def get_early_career_details(request_payload):
    simple_response = ga.make_simple_response_message( "You are beginning your career and looking to develop youe "
                                                       "experience and build your network. You've been working for 0-5"
                                                       " years in the industry. Do you want to know anything else?" )

    msgs = [simple_response]

    return msgs


def get_mid_career_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "You create value for your team or clients amd are looking to develop your expertise and "
        "leadership. You have anywhere from 6-10 years worth of experience in your field. Do you want to know anything else?" )

    msgs = [simple_response]

    return msgs


def get_established_career_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "You are experienced in your field and are known in your industry; you are looking for ways "
        "to increase your influence and connect with other senior-level leaders. You have been "
        "working 11+ years in your focus area. Do you want to know anything else?" )

    msgs = [simple_response]

    return msgs


def get_membership_skillset_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "The skillsets that you can acquire by being a member at Women Techmakers are Career Transition, "
        "Communication, Entrepreneurship, Leadership, Networking, Organizational/Team Management, Product/Project "
        "Management and Technical Skills . Do you want to know anything else?" )


    msgs = [simple_response]

    return msgs


def get_scholarship_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "I can assist you with the scholarship program. Which scholarship program do you want to hear about?" )

    items = []
    option_info = ga.make_option_info( "WTM Scholarship", "WTM Scholarship" )
    item = ga.make_item( option_info, "Women Techmakers Scholars Program ", "Through the Women Techmakers Scholars "
                                                                            "program, we are working to further Dr. "
                                                                            "Anita Borg/'s vision of creating gender "
                                                                            "equality in the field of computer "
                                                                            "science, and to encourage and support "
                                                                            "women in tech to become active role "
                                                                            "models and leaders in the field.", "" )
    items.append( item )

    option_info = ga.make_option_info( "Udacity Scholarship", "Udacity Scholarship" )
    item = ga.make_item( option_info, "Women Techmakers Udacity Scholarship",
                         "Women Techmakers is offering fully funded scholarships for a year of access to one of four "
                         "technical online degree programs from Udacity, as well as extra support, special access, "
                         "and connection to the global Women Techmakers community.",
                         "" )
    items.append( item )

    carousel_card_msg = ga.make_carousel_card_message( items )

    msgs = [simple_response, carousel_card_msg]

    return msgs


def get_wtm_scholarship_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Read more on Women Techmakers Scholars Program. Do you want to know anything else?" )
    link = ga.make_link_card_message( "this link :",
                                      "https://www.womentechmakers.com/scholars" )

    msgs = [simple_response, link]

    return msgs


def get_udacity_scholarship_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Read more on Women Techmakers Udacity Scholarship. Do you want to know anything else?" )
    link = ga.make_link_card_message( "this link :",
                                      "https://www.womentechmakers.com/udacity" )

    msgs = [simple_response, link]
    return msgs


def get_meetup_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Read more about Women Techmakers Meetups. Do you want to know anything else?" )
    title = "Women Techmakers Meetups"
    subtitle = "WTM"
    image_url = "https://www.google.co.in/search?q=images+women+techmakers&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiIpuLDh7zXAhUQTI8KHTuwDgQQsAQILQ&biw=1680&bih=953#imgrc=Nj9C-4eN8gQATM:"
    formatted_text = "Learn about new and interesting Google platforms, tools, and services, while gathering with " \
                     "other women in technology at a meetup near you. Our Women Techmakers Leads collaborate within " \
                     "Google Developer Groups to ensure we are creating a diverse and inclusive ecosystem around the " \
                     "globe. "

    buttons = ga.make_buttons( "Find an organizer", "https://www.womentechmakers.com/directory" )

    basic_card = ga.make_basic_card_message( title, "", formatted_text, "", buttons )

    msgs = [simple_response, basic_card]

    return msgs


def get_summit_details(request_payload):
    simple_response = ga.make_simple_response_message(
        "Read more about the IWD Summit. Do you want to know anything else?" )
    title = "International Women's Day Global Event Series"
    subtitle = "WTM"
    formatted_text = "By participating in International Women/'s Day you will hear inspiring stories, learn hands-on " \
                     "via design sprints and codelabs, and celebrate women in technology at Google offices around the" \
                     " world. "

    buttons = ga.make_buttons( "All about IWD'17", "https://www.womentechmakers.com/iwd17" )
    image_url = "https://www.google.co.in/search?q=images+women+techmakers&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiIpuLDh7zXAhUQTI8KHTuwDgQQsAQILQ&biw=1680&bih=953#imgrc=Nj9C-4eN8gQATM:"
    basic_card = ga.make_basic_card_message( title, subtitle, formatted_text, image_url, buttons )

    msgs = [simple_response, basic_card]

    return msgs


def ask_based_on_user_choice(request_payload):
    result = request_payload.get( 'result' )
    context = result.get( 'contexts' )
    param = [d['parameters'] for d in context if d['name'] == 'actions_intent_option'][0]
    if param.get( 'OPTION' ) == 'Our Story':
        msgs = get_story( request_payload )
    elif param.get( 'OPTION' ) == 'Membership':
        msgs = get_membership_details( request_payload )
    elif param.get( 'OPTION' ) == 'Scholarships':
        msgs = get_scholarship_details( request_payload )
    elif param.get( 'OPTION' ) == 'Meetups':
        msgs = get_meetup_details( request_payload )
    elif param.get( 'OPTION' ) == 'IWD Summit':
        msgs = get_summit_details( request_payload )
    elif param.get( 'OPTION' ) == 'visibility':
        msgs = get_visibility_details( request_payload )
    elif param.get( 'OPTION' ) == 'community':
        msgs = get_community_details( request_payload )
    elif param.get( 'OPTION' ) == 'resources':
        msgs = get_resources_details( request_payload )
    elif param.get( 'OPTION' ) == 'become_a_member':
        msgs = get_become_member_details( request_payload )
    elif param.get( 'OPTION' ) == 'member_benefits':
        msgs = get_member_benefits_details( request_payload )
    elif param.get( 'OPTION' ) == 'career_levels':
        msgs = get_membership_careerlevel_details( request_payload )
    elif param.get( 'OPTION' ) == 'skillsets':
        msgs = get_membership_skillset_details( request_payload )
    elif param.get( 'OPTION' ) == 'WTM Scholarship':
        msgs = get_wtm_scholarship_details( request_payload )
    elif param.get( 'OPTION' ) == 'Udacity Scholarship':
        msgs = get_udacity_scholarship_details( request_payload )
    elif param.get( 'OPTION' ) == 'early_career':
        msgs = get_early_career_details( request_payload )
    elif param.get( 'OPTION' ) == 'mid_career':
        msgs = get_mid_career_details( request_payload )
    elif param.get( 'OPTION' ) == 'established_career':
        msgs = get_established_career_details( request_payload )
    elif param.get( 'OPTION' ) == 'benefit_1':
        msgs = get_benefit_1( request_payload )
    elif param.get( 'OPTION' ) == 'benefit_2':
        msgs = get_benefit_2( request_payload )
    elif param.get( 'OPTION' ) == 'benefit_3':
        msgs = get_benefit_3( request_payload )
    elif param.get( 'OPTION' ) == 'benefit_4':
        msgs = get_benefit_4( request_payload )
    elif param.get( 'OPTION' ) == 'benefit_5':
        msgs = get_benefit_5( request_payload )

    return msgs
