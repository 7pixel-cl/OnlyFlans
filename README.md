# Proyecto Django: OnlyFlans

## Descripción

Este proyecto está diseñado para que aprendas a crear un entorno virtual, instalar Django y generar un proyecto Django básico. Sigue los pasos indicados en los requerimientos para completar las tareas y entregar los pantallazos solicitados.

---

## Requerimientos

### Requerimiento 1

1. **Crea un entorno virtual** llamado `onlyflans_env`.
   ```bash
   python -m venv onlyflans_env
   ```
2. Activa el entorno virtual:
   - En **Linux/Mac**:
     ```bash
     source onlyflans_env/bin/activate
     ```
   - En **Windows**:
     ```powershell
     .\onlyflans_env\Scripts\activate
     ```
3. Verifica que la versión de Python usada sea **Python 3**:
   ```bash
   python --version
   ```
4. Realiza un pantallazo de la versión de Python y guárdalo como `requerimiento1_version_python.png` en la carpeta `requerimiento1/`.

---

### Requerimiento 2

1. Asegúrate de que el entorno virtual `onlyflans_env` esté activado.
2. Instala Django:
   ```bash
   pip install django
   ```
3. Verifica que Django se instaló correctamente:
   ```bash
   django-admin --version
   ```
4. Realiza un pantallazo del resultado y guárdalo como `requerimiento2_instalacion_django.png` en la carpeta `requerimiento2/`.

---

### Requerimiento 3

1. Usando `django-admin`, genera un nuevo proyecto llamado `onlyflans`:
   ```bash
   django-admin startproject onlyflans
   ```
2. Navega a la carpeta del proyecto:
   ```bash
   cd onlyflans
   ```
3. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
4. Accede a la URL `http://127.0.0.1:8000/` en tu navegador.
5. Realiza un pantallazo de la página cargada y guárdalo como `requerimiento3_proyecto_activo.png` en la carpeta `requerimiento3/`.

---

## Uso de `requirements.txt`

Después de instalar las dependencias en tu entorno virtual, puedes generar un archivo `requirements.txt` con el siguiente comando:

```bash
pip freeze > requirements.txt
```

Esto creará un archivo que contiene todas las dependencias instaladas. Para que otros puedan recrear tu entorno, asegúrate de incluir `requirements.txt` en tu repositorio.

Cuando otra persona clone tu proyecto, podrá instalar todas las dependencias usando:

```bash
pip install -r requirements.txt
```

---

## Cómo desactivar y eliminar el entorno virtual

### Desactivar el entorno virtual

Para desactivar el entorno virtual después de haber terminado, simplemente ejecuta:

```bash
deactivate
```

### Eliminar el entorno virtual

Si deseas eliminar el entorno virtual, asegúrate de estar en el directorio correcto y luego ejecuta:

- **Linux/Mac**:

  ```bash
  rm -rf onlyflans_env
  ```

- **Windows**:
  ```powershell
  rmdir /s /q onlyflans_env
  ```

---
