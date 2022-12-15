Para poder visualizar adecuadamente este proyecto es necesario instalar un entorno virtual el cual 
contenga las librerías declaradas en el script.py

from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import joblib
from pathlib import Path
import math
import folium

Adicionalmente, no se debe mover la ruta de ningún archivo debido a que esto podría romper la secuencia del script.