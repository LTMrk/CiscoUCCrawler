---
doc_id: webex-webex-byova-gateway-python-tools-gecx-audio-lab-readme-md
source_url: https://github.com/webex/webex-byova-gateway-python/blob/main/tools/gecx_audio_lab/README.md
repo: webex/webex-byova-gateway-python
ruta: tools/gecx_audio_lab/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:51.305132+00:00
---

# webex-byova-gateway-python — tools/gecx_audio_lab/README.md

Repositorio: webex/webex-byova-gateway-python

# GECX Audio Lab compatibility entry point

The lab now supports both GECX and AWS Lex and is documented as the
[Voice Agent Audio Lab](../voice_agent_lab/README.md).

The earlier command remains compatible:

```bash
python -m tools.gecx_audio_lab --gateway-config config/config.yaml
```

Prefer the provider-neutral entry point for new usage:

```bash
python -m tools.voice_agent_lab --gateway-config config/config.yaml
```

Existing gitignored GECX overlay files remain accepted with `--config`.

---
> Fuente: https://github.com/webex/webex-byova-gateway-python/blob/main/tools/gecx_audio_lab/README.md (licencia NOASSERTION)
