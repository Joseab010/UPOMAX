/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class PlataformasComponente extends Component {
    setup() {
        this.state = useState({
            plataforma: {
                name: ""
            },
            plataformaList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upomax.plataforma"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllPlataformas()
        })
    }

    async getAllPlataformas() {
        this.state.plataformaList = await this.orm.searchRead(
            this.model,
            [],
            ["name", "series_count", "peliculas_count"]
        )
    }

    addPlataforma() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editPlataforma(plataforma) {
        this.state.activeId = plataforma.id
        this.state.isEdit = true
        this.state.plataforma = { ...plataforma }
    }

    async savePlataforma() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.plataforma]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.plataforma);
        }

        const closeBtn = document.querySelector('#plataformasModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllPlataformas();
    }

    resetForm() {
        this.state.plataforma = {
            name: ""
        }
    }

    async deletePlataforma(plataforma) {
        await this.orm.unlink(this.model, [plataforma.id])
        await this.getAllPlataformas()
    }

    async searchPlataformas() {
        const text = this.searchInput.el.value
        this.state.plataformaList = await this.orm.searchRead(
            this.model,
            [['name', 'ilike', text]],
            ["name", "series_count", "peliculas_count"]
        )
    }
}

PlataformasComponente.template = 'upomax.PlataformasComponente';
registry.category('actions').add('upomax.action_PlataformasComponente_js', PlataformasComponente);

export default PlataformasComponente;