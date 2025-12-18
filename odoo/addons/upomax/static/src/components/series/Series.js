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
        this.csvInput = useRef("csv-input")

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

    async importCSV() {
        const file = this.csvInput.el.files[0];
        if (!file) {
            alert("Por favor selecciona un archivo CSV");
            return;
        }

        const reader = new FileReader();
        reader.onload = async (e) => {
            try {
                const csv = e.target.result;
                const lines = csv.split('\n');
                const headers = lines[0].split(',').map(h => h.trim());
                
                const series = [];
                for (let i = 1; i < lines.length; i++) {
                    if (lines[i].trim() === '') continue;
                    
                    const values = lines[i].split(',').map(v => v.trim().replace(/^"|"$/g, ''));
                    const serie = {};
                    
                    headers.forEach((header, index) => {
                        if (header === 'id') return;
                        serie[header] = values[index];
                    });
                    
                    if (serie.name) {
                        if (serie.duracion) serie.duracion = parseInt(serie.duracion);
                        if (serie.edad_recomendada) serie.edad_recomendada = parseInt(serie.edad_recomendada);
                        if (serie.puntuacion_general) serie.puntuacion_general = parseFloat(serie.puntuacion_general);
                        series.push(serie);
                    }
                }

                if (series.length > 0) {
                    await this.orm.create(this.model, series);
                    alert(`Se importaron ${series.length} series correctamente`);
                    this.csvInput.el.value = '';
                    await this.getAllSeries();
                } else {
                    alert("No se encontraron series válidas en el CSV");
                }
            } catch (error) {
                alert("Error al importar el CSV: " + error.message);
            }
        };
        reader.readAsText(file);
    }
}

SeriesComponente.template = 'upomax.SeriesComponente';
registry.category('actions').add('upomax.action_SeriesComponente_js', SeriesComponente);

export default SeriesComponente;
