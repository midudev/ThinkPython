# Think Python, 3.ª edición

Materiales, notebooks de Jupyter y versión web en español de la 3.ª edición de *Think Python: How to Think Like a Computer Scientist*, de Allen B. Downey.

Traducción al español por [midudev](https://midu.dev) (Miguel Ángel Durán).

## Enlaces

- Repositorio del proyecto: [libropython.es](https://libropython.es)
- Página original del libro: [Green Tea Press](http://thinkpython.com)
- Versión impresa y electrónica en inglés: [Bookshop.org](https://bookshop.org/a/98697/9781098155438) y [Amazon](https://www.amazon.com/_/dp/1098155432?smid=ATVPDKIKX0DER&_encoding=UTF8&tag=oreilly20-20&_encoding=UTF8&tag=greenteapre01-20&linkCode=ur2&linkId=e2a529f94920295d27ec8a06e757dc7c&camp=1789&creative=9325)

## Requisitos

- Python 3
- `pip`
- Jupyter Notebook o JupyterLab, si quieres abrir los notebooks localmente
- Jupyter Book y Playwright, si quieres construir la versión web y el PDF

## Instalación

Desde la raíz del repositorio, instala las herramientas necesarias:

```bash
python3 -m pip install jupyter notebook jupyterlab jupyter-book playwright
python3 -m playwright install chromium
```

Si ya tienes Jupyter instalado, puedes instalar solo lo necesario para construir el libro:

```bash
python3 -m pip install jupyter-book playwright
python3 -m playwright install chromium
```

## Construir el libro

1. Entra en la carpeta de Jupyter Book:

   ```bash
   cd jb
   ```

2. Ejecuta el script de construcción:

   ```bash
   ./build.sh
   ```

3. Revisa los archivos generados:

   - HTML: `jb/_build/html/index.html`
   - PDF: `jb/_build/html/think-python-es.pdf`
   - Archivos estáticos para producción: `jb/_build/html/`

## Abrir los notebooks

Desde la raíz del repositorio, puedes abrir los notebooks con Jupyter Notebook:

```bash
jupyter notebook
```

También puedes usar JupyterLab:

```bash
jupyter lab
```

Después, abre desde el navegador el capítulo o notebook que quieras consultar.

## Estructura del proyecto

- `chapters/`: notebooks originales por capítulo.
- `jb/`: configuración y fuentes de Jupyter Book.
- `jb/build.sh`: script para generar la versión web y el PDF.
- `jb/_build/html/`: salida generada para publicar el libro.

## Licencia

Se conserva la atribución original a Allen B. Downey. La traducción al español fue realizada por [midudev](https://midu.dev) (Miguel Ángel Durán).

Esta obra está bajo una [Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional](https://creativecommons.org/licenses/by-nc-sa/4.0/).
