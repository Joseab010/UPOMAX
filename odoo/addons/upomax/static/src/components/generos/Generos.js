/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class GenerosComponente extends Component {
    setup() {
        this.state = useState({
            genero: {
                name: "",
            },
            generoList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upomax.genero"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllGeneros()
        })
    }

    async getAllGeneros() {
        this.state.generoList = await this.orm.searchRead(
            this.model,
            [],
            ["name", "series_count", "peliculas_count"]
        )
    }

    addGenero() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editGenero(genero) {
        this.state.activeId = genero.id
        this.state.isEdit = true
        this.state.genero = { ...genero }
    }

    async saveGenero() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.genero]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.genero);
        }

        const closeBtn = document.querySelector('#generosModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllGeneros();
    }

    resetForm() {
        this.state.genero = {
            name: "",
        }
    }

    async deleteGenero(genero) {
        await this.orm.unlink(this.model, [genero.id])
        await this.getAllGeneros()
    }

    async searchGeneros() {
        const text = this.searchInput.el.value
        this.state.generoList = await this.orm.searchRead(
            this.model,
            [['name', 'ilike', text]],
            ["name", "series_count", "peliculas_count"]
        )
    }
}

GenerosComponente.template = 'upomax.GenerosComponente';
registry.category('actions').add('upomax.action_GenerosComponente_js', GenerosComponente);

export default GenerosComponente;
