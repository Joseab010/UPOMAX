/** @odoo-module */

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class ReviewsComponente extends Component {
    setup() {
        this.state = useState({
            review: {
                titulo: "",
                calificacion: 5,
                comentario: "",
                like: true,
                id_usuario: false,
                serie_id: false,
                pelicula_id: false
            },
            reviewList: [],
            isEdit: false,
            activeId: false,
            users: [],
            series: [],
            peliculas: [],
        })
        this.orm = useService("orm")
        this.model = "upomax.review"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllReviews()
            await this.loadRelatedData()
        })
    }

    async getAllReviews() {
        this.state.reviewList = await this.orm.searchRead(
            this.model,
            [],
            ["titulo", "calificacion", "comentario", "fecha", "like", "id_usuario", "serie_id", "pelicula_id"]
        )
    }

    async loadRelatedData() {
        this.state.users = await this.orm.searchRead("upomax.usuario", [], ["name"])
        this.state.series = await this.orm.searchRead("upomax.serie", [], ["name"])
        this.state.peliculas = await this.orm.searchRead("upomax.pelicula", [], ["name"])
    }

    addReview() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editReview(review) {
        this.state.activeId = review.id
        this.state.isEdit = true
        this.state.review = {
            titulo: review.titulo,
            calificacion: review.calificacion,
            comentario: review.comentario,
            like: review.like,
            id_usuario: review.id_usuario ? review.id_usuario[0] : false,
            serie_id: review.serie_id ? review.serie_id[0] : false,
            pelicula_id: review.pelicula_id ? review.pelicula_id[0] : false
        }
    }

    async saveReview() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.review]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.review);
        }

        const closeBtn = document.querySelector('#reviewsModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllReviews();
    }

    resetForm() {
        this.state.review = {
            titulo: "",
            calificacion: 5,
            comentario: "",
            like: true,
            id_usuario: false,
            serie_id: false,
            pelicula_id: false
        }
    }

    async deleteReview(review) {
        await this.orm.unlink(this.model, [review.id])
        await this.getAllReviews()
    }

    async searchReviews() {
        const text = this.searchInput.el.value
        this.state.reviewList = await this.orm.searchRead(
            this.model,
            [['titulo', 'ilike', text]],
            ["titulo", "calificacion", "comentario", "fecha", "like", "id_usuario", "serie_id", "pelicula_id"]
        )
    }

    async updateCalificacion(e, review) {
        await this.orm.write(this.model, [review.id], { calificacion: parseInt(e.target.value) })
        await this.getAllReviews()
    }
}

ReviewsComponente.template = 'upomax.ReviewsComponente';
registry.category('actions').add('upomax.action_ReviewsComponente_js', ReviewsComponente);

export default ReviewsComponente;