# prisoner
Es un programa escrito en Python 3, que determina si un ciudadano está en la cárcel o está fuera.
Solución al [problema](https://www.codeeval.com/browse/224/).

#### Entrada
Un archivo, donde cada línea representa las coordenadas de la cárcel y las coordenadas del ciudadano, separados por "|" :

```
1 1, 1 4, 3 4, 3 2 | 2 3
1 1, 3 2, 1 4, 3 4 | 3 3
1 1, 1 3, 3 3, 3 1 | 1 2
```

#### Salida
Imprimir por pantalla si es prisionero o ciudadano:

```
Prisoner
Citizen
Prisoner
```

### Crear entorno virtual y activarlo
```bash
virtualenv venv --python=python3.5
source venv/bin/activate
```

#### Instalar requerimientos
```bash
pip install -r requirements.txt
```

### Ejecutar el programa

```bash
python prisoner_citizen.py
```

### Ejecturar las pruebas

```bash
python tests.py
```
