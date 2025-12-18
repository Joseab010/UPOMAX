/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class TracksComponente extends Component {
    setup() {
        this.state = useState({
            track: {
                name: "",
                duracion: 0,
                capitulo_id: false,
            },
            trackList: [],
            isEdit: false,
            activeId: false,
            capitulos: [],
        })
        this.orm = useService("orm")
        this.model = "upomax.track"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllTracks()
            await this.loadRelatedData()
        })
    }

    async getAllTracks() {
        this.state.trackList = await this.orm.searchRead(
            this.model,
            [],
            ["name", "duracion", "capitulo_id"]
        )
    }

    async loadRelatedData() {
        this.state.capitulos = await this.orm.searchRead("upomax.capitulo", [], ["name"])
    }

    addTrack() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editTrack(track) {
        this.state.activeId = track.id
        this.state.isEdit = true
        this.state.track = {
            name: track.name,
            duracion: track.duracion,
            capitulo_id: track.capitulo_id ? track.capitulo_id[0] : false,
        }
    }

    async saveTrack() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.track]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.track);
        }

        const closeBtn = document.querySelector('#tracksModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllTracks();
    }

    resetForm() {
        this.state.track = {
            name: "",
            duracion: 0,
            capitulo_id: false,
        }
    }

    async deleteTrack(track) {
        await this.orm.unlink(this.model, [track.id])
        await this.getAllTracks()
    }

    async searchTracks() {
        const text = this.searchInput.el.value
        this.state.trackList = await this.orm.searchRead(
            this.model,
            [['name', 'ilike', text]],
            ["name", "duracion", "capitulo_id"]
        )
    }

    async updateDuracion(e, track) {
        await this.orm.write(this.model, [track.id], { duracion: parseInt(e.target.value) })
        await this.getAllTracks()
    }
}

TracksComponente.template = 'upomax.TracksComponente';
registry.category('actions').add('upomax.action_TracksComponente_js', TracksComponente);

export default TracksComponente;
