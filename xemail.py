import smtplib
import random
#En esta variable se guardara el token para enviar correos con gmail
key=""
#Esta funcion inicia los servios de smtplib 
def servicio(host,port,mensaje):
    server=smtplib.SMTP(host,port)
    server.starttls()
    server.login(user="franz0317medina@gmail.com",password=key)
    server.sendmail(from_addr="@gmail.com",to_addrs="@gmail.com",msg=mensaje) # en esta variable introduciremos los correos de quien se envia y a quien va destinado
    server.quit()

#Esta funcion contiene en su interior una lista con los mensajes
def mensaje():
    print("Ingresa c para salir ")
#    mensaje=input("Mensaje : ")
    
    mensaje=["Esto es DX","Somos una comunidad","Quien tiene 88 llaves, pero no puede abrir una sola puerta?","Rabo cortito y orejas largas, corro y salto muy ligerito"]
    r=random.randint(0,len(mensaje)-1)
    return mensaje[r]


def main():
    print("ingresa -c para cancelar el bucle")
    while True:
        op=input("opcion : ")
        if op != "c":
            pass
        else:
            break
        dato=mensaje()
        servicio("smtp.gmail.com",587,dato)
        print("Mensaje exitoso")

if __name__=="__main__":
    main()

    
