/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class PeliculasComponente extends Component {
    setup() {
        this.state = useState({
            pelicula: {
                name: "",
                anio: new Date().getFullYear(),
                duracion: 0,
                edad_recomendada: 13,
                puntuacion_general: 0.0,
                descripcion: ""
            },
            peliculaList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upomax.pelicula"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllPeliculas()
        })
    }

    async getAllPeliculas() {
        this.state.peliculaList = await this.orm.searchRead(
            this.model,
            [],
            ["name", "anio", "duracion", "edad_recomendada", "puntuacion_general"]
        )
    }

    addPelicula() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editPelicula(pelicula) {
        this.state.activeId = pelicula.id
        this.state.isEdit = true
        this.state.pelicula = { ...pelicula }
    }

    async savePelicula() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.pelicula]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.pelicula);
        }

        const closeBtn = document.querySelector('#peliculasModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllPeliculas();
    }

    resetForm() {
        this.state.pelicula = {
            name: "",
            anio: new Date().getFullYear(),
            duracion: 0,
            edad_recomendada: 13,
            puntuacion_general: 0.0,
            descripcion: ""
        }
    }

    async deletePelicula(pelicula) {
        await this.orm.unlink(this.model, [pelicula.id])
        await this.getAllPeliculas()
    }

    async searchPeliculas() {
        const text = this.searchInput.el.value
        this.state.peliculaList = await this.orm.searchRead(
            this.model,
            [['name', 'ilike', text]],
            ["name", "anio", "duracion", "edad_recomendada", "puntuacion_general"]
        )
    }

    async updateDuracion(e, pelicula) {
        await this.orm.write(this.model, [pelicula.id], { duracion: parseInt(e.target.value) })
        await this.getAllPeliculas()
    }
}

PeliculasComponente.template = 'upomax.PeliculasComponente';
registry.category('actions').add('upomax.action_PeliculasComponente_js', PeliculasComponente);
