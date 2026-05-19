# Think Python, 3.ª edición

Notebooks de Jupyter y otros materiales de la 3.ª edición de *Think Python: How to Think Like a Computer Scientist*.

Por Allen B. Downey.

Traducción al español por midudev (Miguel Ángel Durán).

Puedes pedir las versiones impresa y electrónica de *Think Python 3e* en
[Bookshop.org](https://bookshop.org/a/98697/9781098155438) y
[Amazon](https://www.amazon.com/_/dp/1098155432?smid=ATVPDKIKX0DER&_encoding=UTF8&tag=oreilly20-20&_encoding=UTF8&tag=greenteapre01-20&linkCode=ur2&linkId=e2a529f94920295d27ec8a06e757dc7c&camp=1789&creative=9325).

La página principal del libro está en [Green Tea Press](http://thinkpython.com).

## Cómo ejecutar este fork

Para que todo funcione correctamente:

1. Instala Python 3 y Jupyter si todavía no los tienes.
2. Instala las herramientas de Jupyter Book si necesitas construir el libro. Este repositorio usa el formato clásico de Jupyter Book, por lo que debes instalar la versión 1.x:

   ```bash
   python -m pip install "jupyter-book<2"
   ```

3. Construye el libro desde la carpeta `chapters`, que contiene los notebooks y la configuración del libro:

   ```bash
   jupyter-book build chapters
   ```

4. Para ejecutar o abrir los notebooks con Jupyter, desde la raíz del repositorio puedes usar:

   ```bash
   jupyter notebook
   ```

   Luego abre el notebook que quieras desde la interfaz del navegador. También puedes usar JupyterLab si lo tienes instalado:

   ```bash
   jupyter lab
   ```

## Licencia

Se conserva la atribución original a Allen B. Downey. La traducción al español fue realizada por midudev (Miguel Ángel Durán).
