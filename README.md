# skurx.es — web de SKURX SYSTEMS

Este repositorio es el código fuente de **https://skurx.es**. Se publica automáticamente con GitHub Pages: cualquier cambio que llegue a la rama `main` aparece en la web en uno o dos minutos.

## Qué hay en cada archivo

| Archivo | Qué es |
|---|---|
| `index.html` | Estructura y **todos los textos** de la web |
| `styles.css` | Diseño: colores, tipografía, tamaños, versión móvil |
| `fini.js` | Asistente del chat (Fini). **Activado**. Envía las conversaciones a info@skurx.es mediante Web3Forms. Para apagarlo: `enabled: false` |
| `hero-bg.webp` | Fondo de la portada (el planeta con la luz dorada) |
| `cierre-bg.webp` | Foto del cierre (oficina vacía al atardecer) |
| `capacity-funnel.svg` / `capacity-funnel-mobile.svg` | Ilustración de "Qué hacemos" (escritorio / móvil) |
| `og-image.jpg` | Imagen que se ve al compartir el enlace en redes o WhatsApp |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` | Iconos de la pestaña y del móvil |
| `privacidad.html` | Política de privacidad |
| `sectores/` | Una página por sector (inmobiliarias, gestorías, automoción…). Se generan desde `tools/sectores_data.py` |
| `404.html` | Página de error |
| `CNAME` | Conecta el repositorio con el dominio skurx.es (no tocar) |
| `robots.txt`, `sitemap.xml` | Para Google |
| `VISUAL-NOTES.md`, `REFERENCE-CHECK.md` | Reglas de marca que debe respetar cualquier cambio |

## Cómo cambiar un texto

1. Abre `index.html` en GitHub y pulsa el lápiz (Edit).
2. Busca el texto (Ctrl/Cmd + F), cámbialo y pulsa **Commit changes**.
3. En uno o dos minutos está en skurx.es.

Cada cambio queda guardado en el historial (pestaña *Commits*), así que siempre se puede volver a una versión anterior.

## Si cambias `styles.css` o `fini.js`

En `index.html` (y en `privacidad.html` y `404.html` para los estilos) esos archivos se cargan con una versión, por ejemplo `fini.js?v=20260926b`. Cuando los modifiques, cambia ese número (por ejemplo, a la fecha del día). Así los navegadores descargan la versión nueva al momento en vez de usar la que tenían guardada.

## Idiomas

- El español es la fuente: `index.html` y `privacidad.html` se editan a mano; el contenido de las 12 páginas de sector está en `tools/sectores_data.py`.
- Cada idioma adicional tiene sus textos en `tools/i18n_<código>.py` y sus sectores en `tools/sectores_data_<código>.py`, y se publica en su carpeta (`/en/`, `/ca/`, `/fr/`, `/de/`, `/nl/`).
- Después de cualquier cambio de textos, ejecuta `python3 tools/build_site.py`. Regenera las páginas de sector, las versiones en otros idiomas (con Fini), el selector de idioma, las etiquetas `hreflang` y el `sitemap.xml`. Si algún texto en español queda sin traducir, el script se detiene sin escribir nada y dice cuál: añádelo a `tools/i18n_<código>.py` de cada idioma.
- No edites a mano las páginas de otros idiomas ni las de sector: el script las sobrescribe. Si los textos están al día, ejecutarlo no cambia ningún archivo.
- Para añadir un idioma: copia `i18n_en.py` y `sectores_data_en.py` con el nuevo código, traduce los valores, añade el código a `LANGS` y `VISIBLE` en `tools/build_site.py` y sus textos de Fini en `fini-i18n.js` y `tools/add-fini-lang.py`.
- Idiomas visibles (desplegable, buscadores, sitemap): español, inglés, catalán, francés, alemán y neerlandés. El serbio (skurx.es/sr/) sigue publicado pero oculto y no se regenera.
- Fini está en los 6 idiomas: `fini.js` en español y `fini-i18n.js` en los demás. Las conversaciones llegan a info@skurx.es.
