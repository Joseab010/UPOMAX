/** @odoo-module **/    

import { registry } from '@web/core/registry';
import { Component, useState } from '@odoo/owl';

class E2Componente extends Component {
    setup() {
        this.state = useState({value:1});
    }

}
    
E2Componente.template = 'owl.E2Componente';
registry.category('actions').add('owl.action_E2Componente_js', E2Componente);