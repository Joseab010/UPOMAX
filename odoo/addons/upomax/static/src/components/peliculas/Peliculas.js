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
        this.csvInput = useRef("csv-input")

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
                
                const peliculas = [];
                for (let i = 1; i < lines.length; i++) {
                    if (lines[i].trim() === '') continue;
                    
                    const values = lines[i].split(',').map(v => v.trim().replace(/^\"|\"$/g, ''));
                    const pelicula = {};
                    
                    headers.forEach((header, index) => {
                        if (header === 'id') return;
                        pelicula[header] = values[index];
                    });
                    
                    if (pelicula.name) {
                        if (pelicula.anio) pelicula.anio = parseInt(pelicula.anio);
                        if (pelicula.duracion) pelicula.duracion = parseInt(pelicula.duracion);
                        if (pelicula.edad_recomendada) pelicula.edad_recomendada = parseInt(pelicula.edad_recomendada);
                        if (pelicula.puntuacion_general) pelicula.puntuacion_general = parseFloat(pelicula.puntuacion_general);
                        peliculas.push(pelicula);
                    }
                }

                if (peliculas.length > 0) {
                    await this.orm.create(this.model, peliculas);
                    alert(`Se importaron ${peliculas.length} películas correctamente`);
                    this.csvInput.el.value = '';
                    await this.getAllPeliculas();
                } else {
                    alert("No se encontraron películas válidas en el CSV");
                }
            } catch (error) {
                alert("Error al importar el CSV: " + error.message);
            }
        };
        reader.readAsText(file);
    }
}

PeliculasComponente.template = 'upomax.PeliculasComponente';
registry.category('actions').add('upomax.action_PeliculasComponente_js', PeliculasComponente);
