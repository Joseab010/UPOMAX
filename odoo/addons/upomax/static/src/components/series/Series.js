/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class SeriesComponente extends Component {
    setup() {
        this.state = useState({
            serie: {
                name: "",
                fecha_emision: "",
                fecha_finalizacion: "",
                duracion: 0,
                edad_recomendada: 13,
                puntuacion_general: 0.0
            },
            serieList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upomax.serie"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllSeries()
        })
    }

    async getAllSeries() {
        this.state.serieList = await this.orm.searchRead(
            this.model,
            [],
            ["name", "fecha_emision", "duracion", "edad_recomendada", "puntuacion_general"]
        )
    }

    addSerie() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editSerie(serie) {
        this.state.activeId = serie.id
        this.state.isEdit = true
        this.state.serie = { ...serie }
    }

    async saveSerie() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.serie]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.serie);
        }

        const closeBtn = document.querySelector('#seriesModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllSeries();
    }

    resetForm() {
        this.state.serie = {
            name: "",
            fecha_emision: "",
            fecha_finalizacion: "",
            duracion: 0,
            edad_recomendada: 13,
            puntuacion_general: 0.0
        }
    }

    async deleteSerie(serie) {
        await this.orm.unlink(this.model, [serie.id])
        await this.getAllSeries()
    }

    async searchSeries() {
        const text = this.searchInput.el.value
        this.state.serieList = await this.orm.searchRead(
            this.model,
            [['name', 'ilike', text]],
            ["name", "fecha_emision", "duracion", "edad_recomendada", "puntuacion_general"]
        )
    }

    async updateDuracion(e, serie) {
        await this.orm.write(this.model, [serie.id], { duracion: parseInt(e.target.value) })
        await this.getAllSeries()
    }
}

SeriesComponente.template = 'upomax.SeriesComponente';
registry.category('actions').add('upomax.action_SeriesComponente_js', SeriesComponente);

export default SeriesComponente;
