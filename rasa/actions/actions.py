# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime as dt

class ActionHoras(Action):

    def name(self) -> Text:
        return "action_horas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        time = dt.now()
        s_hour = 's' if time.hour != 1 else ''
        s_minute = 's' if time.minute != 1 else ''
        time_str = f"são {time.hour} hora{s_hour} e {time.minute} minuto{s_minute}"
        dispatcher.utter_message(text=time_str)

        return []
