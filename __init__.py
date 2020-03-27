from mycroft import MycroftSkill, intent_file_handler


class CovidBrazil(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('brazil.covid.intent')
    def handle_brazil_covid(self, message):
        confirmed = ''
        deaths = ''

        self.speak_dialog('brazil.covid', data={
            'confirmed': confirmed,
            'deaths': deaths
        })


def create_skill():
    return CovidBrazil()

