# Skills de proyecto

Skills de terceros vendorizadas en el repo para que estén disponibles en
cualquier sesión de Claude Code, incluidas las sesiones web, donde `/plugin`
no existe y los plugins instalados en el contenedor se pierden al terminar.

| Skill set | Versión | Skills | Origen | Licencia |
|---|---|---:|---|---|
| caveman | 2.7.0 | 20 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | MIT |
| ponytail | 4.10.0 | 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| superpowers | 6.4.2 | 15 | [obra/superpowers](https://github.com/obra/superpowers) | MIT |

Las licencias están en `_licencias/`.

## Qué hace cada uno

- **caveman** — modo de respuesta comprimido: recorta relleno manteniendo la
  sustancia técnica. Cambia el estilo de las respuestas, no lo que hacen.
- **ponytail** — empuja hacia la solución mínima: reutilizar la stdlib y lo
  que ya existe antes de escribir código nuevo.
- **superpowers** — TDD, depuración sistemática, escritura y ejecución de
  planes, verificación antes de dar algo por terminado.

## Sobre la licencia de caveman

El repositorio de caveman es MIT **excepto** los directorios ligados al
motor (`engine/`, `proxy/`, `rewriter/`, `browse/`, `mcp/`, `shrink/`, el
core Go de cavemem y `shared/platform/`), que están bajo Business Source
License 1.1.

Aquí solo se ha copiado `skills/`, que no entra en esa lista y por tanto es
MIT. Nada de lo vendorizado está bajo BSL. Si en el futuro se trae algo de
esos directorios, hay que revisar la BSL antes: prohíbe ofrecer el trabajo
licenciado a terceros como servicio gestionado o embebido.

## Qué NO se ha traído

- `generated/` de caveman: son variantes por agente (aider, codex, gemini,
  hermes, opencode) y solo contienen `pack.json`, ninguna skill.
- El motor, el proxy y los paquetes de caveman: 30 MB que no hacen falta
  para las skills y que además son los directorios bajo BSL.
- El hook de `SessionStart` de superpowers: un hook no es una skill de
  proyecto, va en `settings.json`. Sin él, las skills siguen funcionando;
  lo que se pierde es la carga automática al arrancar.

## Actualizar

No hay enlace vivo con los repos de origen: esto es una copia. Para subir
de versión, en una sesión con el CLI disponible:

```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
# y luego volver a copiar desde
#   /root/.claude/plugins/cache/<marketplace>/<plugin>/<version>/skills/
```

Mismo procedimiento con `DietrichGebert/ponytail` y
`obra/superpowers-marketplace` (ojo: `superpowers@claude-plugins-official`
NO funciona, el plugin no está en ese marketplace).
