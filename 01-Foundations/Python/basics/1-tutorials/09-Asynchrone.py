import time
import asyncio

# def envoyer_sms(nom,phone):
#     print(f"Envoi d'un sms a {nom} au numero {phone}")
#     time.sleep(2)
#     print("Message envoyé avec succes !")

async def envoyer__sms(nom,phone):
    print(f"Envoi d'un sms a {nom} au numero {phone}")
    await asyncio.sleep(2)
    print("Message envoyé avec succes !")

async def main():
    await asyncio.gather(
        envoyer__sms("Julia", "0254786998"),
        envoyer__sms("Jule", "0254998")
    )

asyncio.run(main())