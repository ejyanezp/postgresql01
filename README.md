# Lambda Function in Python for AWS Lambda exersices.

# Creating the Lambda Function
* 

# Creating the PostgreSQL Lambda Layer
La librería pertinente para python en un sistema sin una instalación previa de PostgreSQL es ```psycopg2-binary```.

## Procedimiento
* Se asume que Python está instalado en el sistema así como el package manager de Python: ```pip```.
* Si aun no existe, crear una carpeta para todas las Lambda Layers que vayamos a crear en un futuro:
```commandline
mkdir aws-lambda-layers
cd aws-lambda-layers
```
* Crear una carpeta para la lambda layer de PostgreSQL
```commandline
mkdir postgresql
cd postgresql
```
* Crear una carpeta Python:
```commandline
mkdir python
```
* Instalar la librería ```psycopg2-binary``` en la carpeta ```python``` creada anteriormente:
```commandline
pip install psycopg2-binary -t python/
```
* El resultado es un directorio como el siguiente (con código python y librerías nativas de PostgreSQL):
```
eduardo@mars:postgresql $ tree python/
python/
├── psycopg2
│   ├── errorcodes.py
│   ├── errors.py
│   ├── extensions.py
│   ├── extras.py
│   ├── __init__.py
│   ├── _ipaddress.py
│   ├── _json.py
│   ├── pool.py
│   ├── _psycopg.cpython-310-x86_64-linux-gnu.so
│   ├── _pycache_
│   │   ├── errorcodes.cpython-310.pyc
│   │   ├── errors.cpython-310.pyc
│   │   ├── extensions.cpython-310.pyc
│   │   ├── extras.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── _ipaddress.cpython-310.pyc
│   │   ├── _json.cpython-310.pyc
│   │   ├── pool.cpython-310.pyc
│   │   ├── _range.cpython-310.pyc
│   │   ├── sql.cpython-310.pyc
│   │   └── tz.cpython-310.pyc
│   ├── _range.py
│   ├── sql.py
│   └── tz.py
├── psycopg2_binary-2.9.9.dist-info
│   ├── INSTALLER
│   ├── LICENSE
│   ├── METADATA
│   ├── RECORD
│   ├── REQUESTED
│   ├── top_level.txt
│   └── WHEEL
└── psycopg2_binary.libs
    ├── libcom_err-2abe824b.so.2.1
    ├── libcrypto-e63abc84.so.1.1
    ├── libgssapi_krb5-497db0c6.so.2.2
    ├── libk5crypto-b1f99d5c.so.3.1
    ├── libkeyutils-dfe70bd6.so.1.5
    ├── libkrb5-fcafa220.so.3.3
    ├── libkrb5support-d0bcff84.so.0.1
    ├── liblber-9c9bf9ef.so.2.0.200
    ├── libldap-c6646621.so.2.0.200
    ├── libpcre-9513aab5.so.1.2.0
    ├── libpq-e8a033dd.so.5.16
    ├── libsasl2-883649fd.so.3.0.0
    ├── libselinux-0922c95c.so.1
    └── libssl-3e69114b.so.1.1
```
* Comprimir la carpeta ```python```:
```commandline
zip -r -y postgresql_layer.zip python/
```
* Copiar el archivo ```postgresql_layer.zip``` a un bucket ```ccb-lambda-layers``` en AWS S3.
```commandline
aws s3 [profile opcional] cp postgresql_layer.zip s3://ccb-lambda-layers/postgresql_layer.zip --region us-east-1
```
* Crear la lambda layer en la consola web de Lambda. Prestar mucha atención al runtime de la lambda layer, debe coincidir con el de la lambda function.
* Añadir la lambda layer a la lambda function.
* Configurar un evento de pruebas
* Probar la lambda
