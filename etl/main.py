from extract import extract
from transform import main
from load import Save_Dw



if __name__ == "__main__":
    try:
        print("!Iniciando Pipeline!")
        
        extract()
        main()
        #Save_Dw()
        
        print("Pipeline Terminado Correctamente!!!")
    except Exception as ex:
        print(f"Ocurrio un Problema")