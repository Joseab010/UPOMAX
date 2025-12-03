FROM odoo:19.0

USER root

# Paquetes base + fuentes
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl xz-utils \
    fontconfig xfonts-75dpi xfonts-base fonts-dejavu-core \
    libxrender1 libxext6 libx11-6 \
  && rm -rf /var/lib/apt/lists/*

# 1) Instala libjpeg62-turbo (no existe en noble, lo tomamos de Debian)
#    Usamos la build estable de Debian (funciona en noble).
RUN set -eux; \
  curl -fL -o /tmp/libjpeg62-turbo.deb \
    http://ftp.de.debian.org/debian/pool/main/libj/libjpeg-turbo/libjpeg62-turbo_2.1.5-4_amd64.deb && \
  apt-get update && apt-get install -y /tmp/libjpeg62-turbo.deb || (apt-get -f install -y && apt-get install -y /tmp/libjpeg62-turbo.deb) && \
  rm -f /tmp/libjpeg62-turbo.deb

# 2) Instala wkhtmltox 0.12.6.1-3 (with patched qt) para jammy/bookworm
#    (ambos .deb valen una vez resuelto libjpeg62-turbo)
RUN set -eux; \
  curl -fL -o /tmp/wkhtmltox.deb \
    https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.jammy_amd64.deb && \
  apt-get update && apt-get install -y --allow-downgrades /tmp/wkhtmltox.deb || \
    (apt-get -f install -y && apt-get install -y --allow-downgrades /tmp/wkhtmltox.deb) && \
  ln -sf /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf && \
  ln -sf /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage && \
  rm -f /tmp/wkhtmltox.deb

USER odoo
