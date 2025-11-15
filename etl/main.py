import logging
from extract import extract
from transform import main
from load import Save_Dw

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    filename='logs.log',
                    filemode='a')

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    try:
        logger.info('Iniciando Pipeline')
        
        extract()
        logger.info('Extraccion Terminada')
        main()
        logger.info('Transformacion Terminada')
        Save_Dw()
        logger.info('Insercion Terminada')
        
        logger.info('Pipeline Terminado Correctamente!!!')
    except Exception as ex:
        logger.error(f'Error en el pipeline {ex}', exc_info=True)