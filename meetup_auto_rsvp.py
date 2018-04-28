import requests


with open('.key') as f:
    KEY = f.read()


with open('groups') as f:
    GROUPS = f.readlines()


def auto_rsvp():
    for group in GROUPS:

        if not group.startswith('#'):

            events = requests.get(
                f'https://api.meetup.com/2/events'
                    f'?group_urlname={group}'
                    f'&key={KEY}'
                    f'&sign=true'
                    f'&rsvp=none'
            ).json()
            print(events)

            for event in events['results']:

                response = requests.post(
                    f'https://api.meetup.com/2/rsvp'
                    f'?event_id={event["id"]}'
                    f'&key={KEY}'
                    f'&sign=true'
                    f'&rsvp=yes'
                ).json()
                print(response)


auto_rsvp()