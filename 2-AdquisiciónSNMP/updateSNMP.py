import time
from getSNMP import consultaSNMP
total_input_traffic = 0
total_output_traffic = 0

while 1:
    total_input_traffic = int(
        consultaSNMP('comunidadSNMP','localhost', '1.3.6.1.2.1.2.2.1.10.2'))
    total_output_traffic = int(
        consultaSNMP('comunidadSNMP','localhost', '1.3.6.1.2.1.2.2.1.16.2'))

    print ("Entrada=",total_input_traffic," Salida=",total_output_traffic)

    time.sleep(1)