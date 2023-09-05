from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 21641812
    API_HASH = "f9e3d59a6e0a6c5186c5ce71ad396819"
    # the name to display in your alive message
    ALIVE_NAME = "@khilpap"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1AZWarzgBu6UIfsH7bFC75ftKISqGBAKtY2gQuGNv-MDpbYf4iq-vdcok__baTyoK59DNQeyj2LA-cEU_FDIQwhQuUoH_5VIgkLTw5XYiIpmyuRPNRkJoaaDnDPW3M0NACeUbSyRV8Fa9Iv_OYk4G8Mze1Vc48dQRkt76Eeru8hJhe6Wh2eTqzITfka-kt_YkO5hP1NRxpsCp3PLFljqNigho6OLZq2N94FHzX6ke53ooTbMlNK8NZj69isq9CaegeKxfuHPLmdwflRbYxambnNnBJeF_57iJs31PGzBDZvbpDCGAPpu_BNq0MWBKEWwHf9McioaxYTTPoln97VGp224ScpuNfjo="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6066923690:AAHQgG7-NaYB1F7CHDkc9_8eTzD6BOYOcdA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
