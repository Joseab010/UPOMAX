/** @odoo-module **/    

import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from '@odoo/owl';
import { useService } from "@web/core/utils/hooks";

class EJ1Componente extends Component {
    setup() {
        this.state = useState({
            task:{name:"", capacity:"0"},
            taskList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "gym.classes"
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "capacity"])
    }

    addTask(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editTask(task){
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = {...task}
    }

    async saveTask() {
        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task);
        }

        const closeBtn = document.querySelector('#exampleModal [data-bs-dismiss="modal"]');
        if (closeBtn) closeBtn.click();

        this.resetForm();
        await this.getAllTasks();
    }


    resetForm(){
        this.state.task = {name:"", capacity:"0"}
    }

    async deleteTask(task){
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()
    }

    async searchTasks(){
        const text = this.searchInput.el.value
        this.state.taskList = await this.orm.searchRead(this.model, [['name','ilike',text]], ["name", "capacity"])
    }

    async updateCapacity(e, task){
        await this.orm.write(this.model, [task.id], {capacity: e.target.value})
        await this.getAllTasks()
    }    
}
    
EJ1Componente.template = 'owl.EJ1Componente';
registry.category('actions').add('owl.action_EJ1Componente_js', EJ1Componente);