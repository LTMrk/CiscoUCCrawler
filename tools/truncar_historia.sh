#!/usr/bin/env bash
# Colapsa la historia a un unico commit raiz conservando el arbol actual.
#
# POR QUE. El 96% del repositorio es salida regenerable: 15.806 documentos
# y 553 MB de markdown que se pueden volver a rastrear. La historia de esa
# salida son ~2.700 commits de "docs(incremental)" que nadie consulta, y
# cuesta 281 MiB de pack. Lo unico irreemplazable es logs/manifest.json.
#
# LO QUE NO HACE, Y ES LO QUE MAS CONFUNDE:
#
#   - Guardar la historia vieja en una RAMA o una ETIQUETA no ahorra nada.
#     Los objetos siguen alcanzables y el pack sigue pesando igual. Por eso
#     aqui el archivo es un BUNDLE, un fichero fuera de git.
#   - GitHub no recoge la basura cuando uno quiere. Tras el force-push los
#     objetos quedan inalcanzables, pero el tamano que muestra GitHub puede
#     tardar en bajar. Lo que si baja de inmediato es lo que descarga un
#     clon nuevo, que es lo que le importa al ETL.
#   - No empuja nada. Imprime el comando para que lo des tu.
#
# USO. Necesita un clon COMPLETO; el del ETL es superficial a proposito.
#
#     git clone https://github.com/LTMrk/CiscoUCCrawler.git
#     cd CiscoUCCrawler
#     bash tools/truncar_historia.sh            # informe, no toca nada
#     bash tools/truncar_historia.sh --aplicar  # crea el commit local
set -euo pipefail

RAMA="${RAMA:-main}"
BUNDLE="${BUNDLE:-../CiscoUCCrawler-historia-$(date +%Y%m%d).bundle}"
APLICAR=0
[ "${1:-}" = "--aplicar" ] && APLICAR=1

if [ -f "$(git rev-parse --git-dir)/shallow" ]; then
  echo "ERROR: clon superficial. La truncadura necesita la historia entera," >&2
  echo "       que es justo lo que se va a archivar. Clona sin --depth." >&2
  exit 1
fi

git rev-parse --verify --quiet "$RAMA" >/dev/null || {
  echo "ERROR: no existe la rama '$RAMA'. Pasala con RAMA=<nombre>." >&2
  exit 1
}

git diff --quiet && git diff --cached --quiet || {
  echo "ERROR: hay cambios sin commitear. Limpia el arbol primero." >&2
  exit 1
}

commits=$(git rev-list --count "$RAMA")
pack=$(git count-objects -vH | sed -n 's/^size-pack: //p')
echo "Rama:     $RAMA"
echo "Commits:  $commits"
echo "Pack:     $pack"
echo "Bundle:   $BUNDLE"
echo

if [ "$APLICAR" -eq 0 ]; then
  echo "Informe solamente. Con --aplicar se haria:"
  echo "  1. bundle de la historia completa en $BUNDLE"
  echo "  2. commit huerfano con el arbol actual de $RAMA"
  echo "  3. imprimir el force-push, que lo das tu"
  exit 0
fi

echo "1/3 Archivando la historia completa..."
git bundle create "$BUNDLE" --all
git bundle verify "$BUNDLE" >/dev/null
echo "    $(du -h "$BUNDLE" | cut -f1) en $BUNDLE"
echo "    Guardalo FUERA del repositorio. Si lo subes como rama o etiqueta,"
echo "    los objetos vuelven a ser alcanzables y no se ahorra nada."

echo "2/3 Creando el commit huerfano..."
arbol=$(git rev-parse "$RAMA^{tree}")
mensaje="chore: colapsar la historia del corpus

El arbol es identico al de $(git rev-parse --short "$RAMA"). Se colapsan
$commits commits, casi todos \"docs(incremental)\" de salida regenerable,
que costaban $pack de pack.

La historia anterior esta archivada en un bundle fuera del repositorio.
No se conserva como rama ni como etiqueta a proposito: eso mantendria los
objetos alcanzables y no ahorraria nada."
nuevo=$(git commit-tree "$arbol" -m "$mensaje")
git branch -f "${RAMA}-truncada" "$nuevo"
echo "    $nuevo en la rama ${RAMA}-truncada"

echo "3/3 Comprobando que el arbol es identico..."
if git diff --quiet "$RAMA" "${RAMA}-truncada"; then
  echo "    OK: ningun fichero cambia."
else
  echo "ERROR: el arbol NO coincide. No empujes nada." >&2
  git diff --stat "$RAMA" "${RAMA}-truncada" >&2
  exit 1
fi

cat <<FIN

Listo en local. Para publicarlo, y solo tu puedes:

    git push --force-with-lease origin ${RAMA}-truncada:${RAMA}

Despues, en un clon nuevo, comprueba que el pack ha bajado:

    git clone https://github.com/LTMrk/CiscoUCCrawler.git /tmp/comprobar
    git -C /tmp/comprobar count-objects -vH | grep size-pack

Si alguien tiene un clon viejo, tendra que volver a clonar: su main y el
nuevo no comparten ningun commit.
FIN
