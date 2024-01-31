from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from functools import partial
Window.size = (350, 550)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17
    

class ChatBot(MDApp):
    
    scheduled_event = None  # Add this line to store the scheduled event
    responses = {
        "departments": "Here is the list of The Departments in UNP: \n1. Department of Languages and Humanities \n2. Department of Social Science and Philosophy \n3. Department of Mathematics and Natural Sciences \n4. Department of Physical Education",
        "1": "Here is the list of the Faculty Members of The Department of Languages and Humanities: \n \n Department Head: \n1. DE VERA, Allen Magdaleno A., MAEd \n \n Faculty: \n1.  AGUILAR, Irene T., MATFil \n2. ALCONIS, Charito R., MATFil \n3. AMANO, Evelyn D., PhD \n4. BARROGA, Crystal T., BFA \n5.BAUTISTA, Benedict, MATPrA \n6. BENZON, Al C,. MAEd \n7. BERONILLA, Eden B., MATEng \n8. CANOY, Bernadeth F., MATFil \n9. ESPINOZA, Jenny Lou C., MATEng \n10. FABRE, Dichi Rica A., MATEng \n11. FORNEAS, Sherwin V., MARTPrA \n12. MARIÑAS, Esperanza marites V., EdD \n13. NESPEROS, Imelda Q., PhD \n14. PACPACO, Kem Eli R., BSED \n15. PASCUAL, Jaizel L., BA POLSCIE \n16. PASTOR, Ma. Ines B., MATFil \n17. QUELNAN, Francisco R. PhD \n18. RAGUNJAN, Nolito R., MATEng \n19. RAPACON, Emely R., MATFil \n20. RUBIA, Eva Occencia t., MATEng \n21. TAACA, Arnel I., AB Eng \n22. TACTAY, Arlie A., MATEng \n23. TADAL, Judy Ann P.,BEEd \n24. TUBON, Ruthie Charmaine A., BEEd \n25. UNCIANO, Ma. Jesusa R., EdD \n26. URBIS, Novie Ada B., PhD \n27. VIRTUDES, Jocelyn F., MATFil \n28. VISAYA, Michael M., BSE",
        "2": "Here is the list of the Faculty Members of The Department of Social Science and Philosophy: \n \n Regular Faculty: \n \n Faculty Head: \n1. SUYAT, Chase Mark \n \n Members: \n1. ABARQUEZ, Simeon IV \n2. ANYOG, Edison Fermin A. IV \n3. OBRERO, Remigio \n4. PABLICO, Mark Edzel \n5. PANAY, Mamerto JR. \n6. TABIOS, Stephen \n \n Regular Faculty with Admin Function: \n1. ANGELES, Arnulfo JR. \n2. AVILA, Mariano Paterno \n3. BAJET, Dante \n4. BELIZAR, Eleanor \n5. DUMBRIQUE, Jean \n6. GAPATE, Benjie \n7. JARAMILLA, Aldrin \n8. LOPEZ, Randolfo \n9. MATA, Lloyd \n10. UNCIANO, Froilan \n \n Part-Time Faculty: \n1. AMODO, Junior \n2. ANDONGO, Adriane \n3. ANYOG, Edison Fermin A. III \n4. ARCAINA, Jedu \n5. AVILA, Daren Dawn \n6. BALLESTA, Leonel \n7. BATIN, Monina \n8. CACERES, Leevan \n9. CASILDO, Christian \n10. DONATO, Iren Jan B. \n11. MOLINA, Julie May \n12. PADRE, Winston \n13. RAGUDO, Jenalyn \n14. RIGUCIRA, Angelica \n15. RUBIO, Michelle Faith \n16. SALDUA, Lester \n17. SUMAGIT, Marjorie \n18. TABUSO, Benmar \n19. QUILALA, Larianne Nyxa2",
        "3": "Here is the list of the Faculty Members of The Department of Mathematics and Natural Sciences: \n \n Regular Faculty: \n1. ANINAG, Rhommel S., MST Chem \n2. BENITEZ, Mhark jay O., MAME \n3. FORONDA, Honorato L., MAME \n4. LLAGAS, Restituto M. Jr., DME \n5. TACTAY, Tirso P., EdD \n6. MOLINA, Germana Gloria V., PhD \n7. ALMAZAN, Jenny Grace I., MST Chem \n8. CAYABYAB, Mary Loreen V., PhD \n9. EBOJO, Magdalena T., MST Phys \n10. JACOB, Digna A., MAME \n11. MERESEN, Dennese Jane G., PhD \n12. NAVAL, Christa Jesusa S., MAEd Bio \n13. RABANZO, Roselyn P., BS Physics \n14. SIEMBRE, Helen R., MAME \n \n Regular Faculty with Admin Function: \n1. DELA CRUZ, Florence A., MST Phys \n2. TABAN, Joseph G., PhD \n3. TORRES, Jonnel B., MST Chem \n4. CADORNA, Edelyn A., PhD \n5. Rizza P., MAME  \n6. RIBOROSO, Rhosechelle A., PhD \n \n Part-Time Faculty: \n1. BALUSO, Nino \n2. BELLON, Emerson Jay P., BS Math \n3. JAVONILLO, Mick Bryan \n4. RABENA, Isaiah G., BS Physics \n5. RENON, Hushley \n6. SALANG, Marvin \n7. TACATA, Edmar \n8. VALITE, Dale \n9. EBOJO, Maejen Clovelle T., BSEd Bio \n10. EMBAT, Precious R. \n11. INOCELDA, Jonalyn \n12. RAQUENO, Jessa Mae A. \n13. RINEN, Trisha Mae \n14. TAN, Angelyn \n \n Admin Staff: \n1. RONDERO, Marie Ann M.",
        "4": "Here is the list of the Faculty Members of The Department of Physical Education: \n \n Regular Faculty: \n1. BALBUENA, Marie Graciel R., MATPE \n2. ALMAZAN, Chasen \n3. ARRUEJO, Joel M., MATPE \n4. DONATO, Jimmy R., MATPE \n5. LIM, Carmela Vee F., MATPE \n6. PALO, Mark Christian T., MATPE \n7. RABARA, Tito A., MATPE \n8. RAMOS, Jenny Rose R. MAEd \n \n Contractual Faculty: \n1. TUMBAGA, Fitch Voy Y. \n \n Part-Time Faculty: \n1. ACENA, Eva Marie P. \n2. BLANCO, Calvin Klein T. \n3. BUSTARDE, Cristhoper L. \n4. CABALUNA, Elaiza Jhel A. \n5. MANZANO, Michael Joshua A. \n6. NAVARRO, Oliva A. \n7. PASCUA, Shela Lee \n8. REGALADO, Joshua P. \n9. ROMERO, Valerie Keith P. \n10. SISON, Adrian Lloyd P. \n11. TEANO, Romely A. \n \n Office Assistant: \n1. GREGORIO, Gladdys D. \n \n Property Custodian: \n1. SAVELLA, Joel James P. Jr.",
        "info": "This app was developed by: \n Go, Judd\n Riego, Daniel\n Villalun, Christel\n Advincula, Zildjan\n Yacap, Angelica\n Berja, Daryl",
        "yawa": "Pisting Yawa ka! Murag manhole imong burat!"
        }

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def get_response(self, command_label):
        value = command_label.text.lower()
        return self.responses.get(value, 'Invalid keyword. please try again.')

    def response(self, command_label, *args):
        response_text = self.get_response(command_label)
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response_text, size_hint_x=.75))

    def send(self):
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            command_label = Command(text=value, size_hint_x=size, halign=halign)
            screen_manager.get_screen('chats').chat_list.add_widget(command_label)
            self.scheduled_event = Clock.schedule_once(partial(self.response, command_label), 2)
            screen_manager.get_screen('chats').text_input.text = ""  # Clear the text_input

if __name__ == '__main__':
    ChatBot().run()