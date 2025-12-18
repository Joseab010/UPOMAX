/** @odoo-module **/

import { registry } from '@web/core/registry';
import { Component, useState } from '@odoo/owl';

class E1Componente extends Component {
    setup() {
        this.state = useState({ value: 1 });
    }
}

E1Componente.template = 'owl.E1Componente';
registry.category('actions').add('owl.action_E1Componente_js', E1Componente);
