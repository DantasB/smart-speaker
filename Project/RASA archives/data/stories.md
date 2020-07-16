## happy path  1             <!-- name of the story - just for debugging -->
* cumprimentar
  - utter_cumprimentar
* sentimento_bem               <!-- user utterance, in the following format: * intent{"entity_name": value} -->
  - utter_feliz

## sad path 1               <!-- this is already the start of the next story -->
* cumprimentar
  - utter_cumprimentar             <!-- action of the bot to execute -->
* sentimento_mal
  - utter_triste

## say goodbye
* despedir
  - utter_despedir

## bot challenge
* desafio_bot
  - utter_iamabot
