#!/bin/bash
# Script para actualizar el módulo upomax sin reiniciar el contenedor

echo "Actualizando módulo upomax..."
docker compose exec odoo odoo -c /etc/odoo/odoo.conf -d odoo --db_host=db --db_port=5432 --db_user=odoo --db_password=odoo -u upomax --stop-after-init

echo "Módulo upomax actualizado correctamente."
