/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class PremiosComponente extends Component {
    setup() {
        this.state = useState({
            premio: {
                name: "",
                categoria: "",
                ano: "",
                titulo_serie: false,
                titulo_pelicula: false
            },
            premioList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upomax.premio"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllPremios()
        })
    }

    async getAllPremios() {
        this.state.premioList = await this.orm.searchRead(
            this.model,
            [],
            ["name", "categoria", "ano", "titulo_serie", "titulo_pelicula"]
        )
    }

    addPremio() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editPremio(premio) {
        this.state.activeId = premio.id
        this.state.isEdit = true
        this.state.premio = { ...premio }
    }

    async savePremio() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.premio]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.premio);
        }

        const closeBtn = document.querySelector('#premiosModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllPremios();
    }

    resetForm() {
        this.state.premio = {
            name: "",
            categoria: "",
            ano: "",
            titulo_serie: false,
            titulo_pelicula: false
        }
    }

    async deletePremio(premio) {
        await this.orm.unlink(this.model, [premio.id])
        await this.getAllPremios()
    }

    async searchPremios() {
        const text = this.searchInput.el.value
        this.state.premioList = await this.orm.searchRead(
            this.model,
            [['name', 'ilike', text]],
            ["name", "categoria", "ano", "titulo_serie", "titulo_pelicula"]
        )
    }
}

PremiosComponente.template = 'upomax.PremiosComponente';
registry.category('actions').add('upomax.action_PremiosComponente_js', PremiosComponente);

export default PremiosComponente;